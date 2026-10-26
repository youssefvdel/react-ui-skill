#!/usr/bin/env python3
"""
Aggregate all component markdown files in docs/reactbits/components/
into CATALOG.md and catalog.json.
"""

import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPONENTS_DIR = os.path.join(ROOT, "components")
CATALOG_MD = os.path.join(ROOT, "CATALOG.md")
CATALOG_JSON = os.path.join(ROOT, "catalog.json")

def parse_md(path):
    text = open(path, "r", encoding="utf-8").read()
    name = os.path.basename(path).replace(".md", "")
    
    title_m = re.search(r"^#\s+(.+)$", text, re.M)
    title = title_m.group(1).strip() if title_m else name
    
    reg_m = re.search(r"\*\*Registry\*\*:\s*`?([^`·\n]+)`?", text)
    registry = reg_m.group(1).strip() if reg_m else name
    
    deps_m = re.search(r"\*\*Deps\*\*:\s*([^·\n]+)", text)
    deps = deps_m.group(1).strip() if deps_m else "none"
    
    files_m = re.search(r"\*\*Files\*\*:\s*(.+)$", text, re.M)
    files = files_m.group(1).strip() if files_m else ""
    
    does_m = re.search(r"\*\*What it does\*\*\s*—\s*(.+?)(?=\n\*\*|\Z)", text, re.S)
    what_does = does_m.group(1).strip().replace("\n", " ") if does_m else ""
    
    motion_m = re.search(r"\*\*Motion\*\*\s*—\s*(.+?)(?=\n\*\*|\Z)", text, re.S)
    motion = motion_m.group(1).strip().replace("\n", " ") if motion_m else ""
    
    cost_m = re.search(r"\*\*Cost\*\*\s*—\s*(.+?)(?=\n\*\*|\Z)", text, re.S)
    cost = cost_m.group(1).strip().replace("\n", " ") if cost_m else ""
    
    fit_m = re.search(r"\*\*Fit for [^*]+\*\*\s*—\s*(.+?)(?=\n\*\*|\Z)", text, re.S)
    fit = fit_m.group(1).strip().replace("\n", " ") if fit_m else ""
    
    verdict_m = re.search(r"\*\*Verdict\*\*\s*—\s*(adopt|adapt|skip)(?:\s*—\s*(.+))?", text, re.I | re.S)
    verdict = verdict_m.group(1).lower() if verdict_m else "skip"
    reason = verdict_m.group(2).strip().replace("\n", " ") if (verdict_m and verdict_m.group(2)) else ""
    
    return {
        "name": name,
        "title": title,
        "registry": registry,
        "deps": deps,
        "files": files,
        "what_does": what_does,
        "motion": motion,
        "cost": cost,
        "fit": fit,
        "verdict": verdict,
        "reason": reason,
    }

def main():
    files = sorted(glob.glob(os.path.join(COMPONENTS_DIR, "*.md")))
    items = [parse_md(f) for f in files]
    
    with open(CATALOG_JSON, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)
        
    adopts = [i for i in items if i["verdict"] == "adopt"]
    adapts = [i for i in items if i["verdict"] == "adapt"]
    skips = [i for i in items if i["verdict"] == "skip"]
    
    lines = [
        "# React Bits Component Catalog for ARKRETE",
        f"Total components surveyed: **{len(items)}**",
        f"- **Adopt**: {len(adopts)}",
        f"- **Adapt**: {len(adapts)}",
        f"- **Skip**: {len(skips)}",
        "",
        "## Recommended for Adoption",
        "| Component | Deps | Best Fit | Reason |",
        "|---|---|---|---|",
    ]
    for i in adopts:
        lines.append(f"| **{i['title']}** | `{i['deps']}` | {i['fit'][:70]} | {i['reason'][:90]} |")
        
    lines.extend([
        "",
        "## Adaptable (Needs tuning / stripping heavy deps / restyling)",
        "| Component | Deps | Best Fit | Reason |",
        "|---|---|---|---|",
    ])
    for i in adapts:
        lines.append(f"| **{i['title']}** | `{i['deps']}` | {i['fit'][:70]} | {i['reason'][:90]} |")
        
    with open(CATALOG_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
        
    print(f"Catalog generated: {len(items)} components ({len(adopts)} adopt, {len(adapts)} adapt, {len(skips)} skip)")

if __name__ == "__main__":
    main()
