#!/usr/bin/env python3
"""Recompute every number in n8n-template-study.md from the raw dataset.

Run: python3 recount.py
Exits non-zero if summary.jsonl and findings.jsonl disagree.

WHAT THIS DOES NOT CATCH: it verifies arithmetic against the stored scan, not
the scan itself. If the checker's rules are wrong, every number here is
confidently wrong in the same direction. It also cannot tell you whether the
templates changed after they were scanned.
"""
import json, collections, statistics, sys

rows = [json.loads(l) for l in open('data/summary.jsonl') if l.strip()]
fnd  = [json.loads(l) for l in open('data/findings.jsonl') if l.strip()]
n = len(rows)

ids = set(r['id'] for r in rows)
assert len(ids) == n, f"duplicate ids: {n - len(ids)}"

total_findings = sum(r.get('findingCount', 0) for r in rows)
if total_findings != len(fnd):
    print(f"FAIL: summary says {total_findings} findings, findings.jsonl has {len(fnd)}")
    sys.exit(1)

defect = sum(1 for r in rows if r.get('findingCount', 0) > 0)
counts = collections.Counter()
for r in rows:
    for rule in set(r.get('rules') or []):
        counts[rule] += 1

print(f"workflows scanned      {n}")
print(f"library size (index)   {len(json.load(open('data/index.json')))}")
print(f"nodes                  {sum(r.get('nodeCount',0) for r in rows)}")
print(f"findings               {len(fnd)}")
print(f"with >=1 defect        {defect}  ({100*defect/n:.1f}%)")
print(f"clean                  {n-defect}")
print(f"median findings        {statistics.median([r.get('findingCount',0) for r in rows]):.0f}")
print()
for rule, c in counts.most_common():
    print(f"{rule:24s} {c:5d}  {100*c/n:5.1f}%")
print("\nOK: summary and findings agree.")
