#!/usr/bin/env python3
"""Split the 218 catalogue entries into re-audit batches for parallel agents."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "reauth"
OUT.mkdir(exist_ok=True)
for old in OUT.glob("batch-*.json"):
    old.unlink()

entries = json.loads((ROOT / "catalog.json").read_text())
PER = 19
count = math.ceil(len(entries) / PER)

for i in range(count):
    chunk = entries[i * PER : (i + 1) * PER]
    payload = [
        {
            "name": e["name"],
            "title": e["title"],
            "deps": e["deps"],
            "verdict": e["verdict"],
            "raw": f"docs/reactbits/raw/{e['name']}.json",
            "doc": f"docs/reactbits/components/{e['name']}.md",
        }
        for e in chunk
    ]
    (OUT / f"batch-{i + 1:02d}.json").write_text(json.dumps(payload, indent=1))

print(f"{len(entries)} entries -> {count} batches in {OUT}")
