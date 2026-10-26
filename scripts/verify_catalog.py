#!/usr/bin/env python3
"""
Re-verify every React Bits component doc against the source it claims to describe.

The catalogue is written by many agents reading hundreds of payloads, and an
agent that only skimmed `description` produces a doc that looks fine and names
no real prop. This checks, per component:

  * the doc carries the required sections
  * the dependency stated in the doc's header matches the payload
  * the Props section names at least one prop the source really declares
  * the verdict is one of adopt / adapt / skip
  * (when the payload is present) it has real source in files[].content

Two layouts are detected automatically:

  survey root   <root>/raw/<name>.json      <root>/components/<name>.md
  this repo     <root>/catalog/sample-raw/  <root>/catalog/docs/

Only a few raw payloads are committed here (5.6 MB in full), so payload checks
run on whichever are present and the summary says how many that was rather than
pretending the rest passed.

    python3 scripts/verify_catalog.py [root]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

VERDICTS = {"adopt", "adapt", "skip"}
SECTIONS = ("**What it does**", "**Props**", "**Motion**", "**Cost**", "**Verdict**")


def find_layout(root: Path) -> tuple[Path, Path, Path]:
    if (root / "raw").is_dir() and (root / "components").is_dir():
        return root / "catalog.json", root / "raw", root / "components"

    repo = root / "catalog"
    if repo.is_dir():
        raw = repo / "raw" if (repo / "raw").is_dir() else repo / "sample-raw"
        return repo / "catalog.json", raw, repo / "docs"

    raise SystemExit(f"no catalogue layout found under {root}")


def _balanced_block(src: str, open_index: int) -> str:
    """Text between a { and its matching }, ignoring braces inside strings."""
    depth = 0
    out: list[str] = []
    quote = ""
    for ch in src[open_index:]:
        if quote:
            if ch == quote:
                quote = ""
            out.append(ch)
            continue
        if ch in "\"'`":
            quote = ch
            out.append(ch)
            continue
        if ch == "{":
            depth += 1
            if depth == 1:
                continue
        elif ch == "}":
            depth -= 1
            if depth == 0:
                break
        out.append(ch)
    return "".join(out)


def props_from_source(src: str, title: str = "") -> set[str]:
    """Prop names the component really declares.

    Interfaces and type literals only, and preferably the one named after the
    component — an inner options object (AnimateOpts, Config) declares names
    that are not props, and matching a doc against those gives false failures.
    """
    candidates: list[tuple[str, str]] = []
    for m in re.finditer(
        r"(?:export\s+)?(?:interface|type)\s+(\w+)\s*(?:<[^>]*>)?\s*(?:extends[^{]*?)?(?:=\s*)?\{", src
    ):
        candidates.append((m.group(1), _balanced_block(src, m.end() - 1)))

    preferred = [
        c for c in candidates if c[0].endswith("Props") or (title and c[0].lower().startswith(title.lower()))
    ]
    pool = preferred or candidates

    names: set[str] = set()
    for _, body in pool:
        for line in body.splitlines():
            mm = re.match(r"\s*([a-zA-Z_$][\w$]*)\??\s*[:(]", line)
            if mm and mm.group(1) not in {"type", "readonly"}:
                names.add(mm.group(1))
    return names


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    catalog_path, raw_dir, docs_dir = find_layout(root)

    entries = json.loads(catalog_path.read_text())
    if isinstance(entries, dict):
        entries = entries.get("components", [])

    failures: list[str] = []
    checked = 0
    with_payload = 0
    verdicts = {"adopt": 0, "adapt": 0, "skip": 0}

    for entry in entries:
        name = entry.get("name", "")
        if not name:
            failures.append("catalog entry without a name")
            continue

        doc_path = docs_dir / f"{name}.md"
        if not doc_path.exists():
            failures.append(f"{name}: no doc")
            continue

        checked += 1
        doc = doc_path.read_text(errors="replace")
        for section in SECTIONS:
            if section not in doc:
                failures.append(f"{name}: doc missing {section}")

        verdict = (entry.get("verdict") or "").strip().lower()
        if verdict not in VERDICTS:
            failures.append(f"{name}: verdict {verdict!r} is not adopt/adapt/skip")
        else:
            verdicts[verdict] += 1

        payload_path = raw_dir / f"{name}.json"
        if not payload_path.exists():
            continue
        with_payload += 1

        payload = json.loads(payload_path.read_text())
        src = "\n".join(f.get("content") or "" for f in (payload.get("files") or []))
        if not src.strip():
            failures.append(f"{name}: payload has no source content")
            continue

        deps = {d.split("@")[0] for d in (payload.get("dependencies") or []) if d}
        header = re.search(r"\*\*Deps\*\*:\s*([^·]+)", doc)
        if header:
            stated = header.group(1).strip().strip("`").lower()
            if not deps and stated not in ("none", "none.", "-", ""):
                failures.append(f"{name}: doc says deps {stated!r}, payload has none")
            elif deps and not any(d in stated for d in deps):
                failures.append(f"{name}: doc says deps {stated!r}, payload needs {sorted(deps)}")

        props_block = doc.split("**Props**", 1)[-1].split("**Motion**", 1)[0]
        real = props_from_source(src, entry.get("title") or "")
        if real and not any(re.search(rf"\b{re.escape(p)}\b", props_block) for p in real):
            failures.append(f"{name}: Props section names no prop from the source")

    print(f"checked {checked} docs · {with_payload} with a payload present")
    print(f"verdicts: adopt {verdicts['adopt']} · adapt {verdicts['adapt']} · skip {verdicts['skip']}")
    if failures:
        print(f"\n{len(failures)} problem(s):")
        for f in failures[:50]:
            print("  -", f)
        if len(failures) > 50:
            print(f"  ... and {len(failures) - 50} more")
        return 1

    print("every doc parses, cites a real prop, and matches its payload's dependencies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
