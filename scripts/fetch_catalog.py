# Fetch the React Bits registry and every TS+Tailwind component payload.
#
#   python3 scripts/fetch_catalog.py /path/to/docs/reactbits
#
# Steps 1-3 of the reactbits-catalog skill. Bulk raw bytes, so plain HTTP, not
# web_extract: the payload is source code and must not be summarised.

import concurrent.futures as futures
import glob
import gzip
import json
import os
import sys
import urllib.request

BASE = "https://reactbits.dev/r"


def get(url: str, timeout: int = 90) -> bytes:
    req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    # urllib does not decompress transparently when Accept-Encoding is set
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    return data


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else "docs/reactbits"
    raw = os.path.join(out, "raw")
    os.makedirs(raw, exist_ok=True)

    registry = json.loads(get(f"{BASE}/registry.json"))
    names = [i["name"] for i in registry["items"] if i["name"].endswith("-TS-TW")]
    print(f"registry items: {len(registry['items'])} | TS+TW components: {len(names)}")

    def one(name: str) -> str:
        path = os.path.join(raw, f"{name}.json")
        if os.path.exists(path) and os.path.getsize(path) > 0:
            return "cached"
        try:
            open(path, "wb").write(get(f"{BASE}/{name}.json", 60))
            return "ok"
        except Exception as exc:  # noqa: BLE001 - report, do not abort the sweep
            return f"fail {name}: {exc}"

    with futures.ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(one, names))

    # stragglers: retry serially, the CDN throttles concurrent bursts
    for result in [r for r in results if r.startswith("fail")]:
        one(result.split(":", 1)[0].replace("fail ", ""))

    parsed = 0
    for name in names:
        path = os.path.join(raw, f"{name}.json")
        try:
            if json.load(open(path)).get("files"):
                parsed += 1
        except Exception:  # noqa: BLE001
            pass

    on_disk = len(glob.glob(os.path.join(raw, "*.json")))
    print(f"files on disk: {on_disk} | fetched and parseable: {parsed} / {len(names)}")
    print("next: python3 scripts/make_batches.py", out)
    return 0 if parsed == len(names) else 1


if __name__ == "__main__":
    raise SystemExit(main())
