# Split the fetched component names into batch files for parallel agents.
#
#   python3 scripts/make_batches.py /path/to/docs/reactbits [batch_size]
#
# One subagent per batch file. Nine components each keeps a child's context
# small enough to read the sources and still write honest docs.

import glob
import json
import os
import sys


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else "docs/reactbits"
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 9

    names = sorted(
        os.path.basename(p)[:-5] for p in glob.glob(os.path.join(out, "raw", "*.json"))
    )
    batches = os.path.join(out, "batches")
    os.makedirs(batches, exist_ok=True)

    for i in range(0, len(names), size):
        open(os.path.join(batches, f"batch-{i // size:02d}.json"), "w").write(
            json.dumps(names[i : i + size], indent=1)
        )

    print(f"components: {len(names)} | batches: {(len(names) + size - 1) // size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
