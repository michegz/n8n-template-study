# Pinned evidence

- `template-4295.json` - live pull of https://api.n8n.io/api/templates/workflows/4295
  fetched 2026-08-19, HTTP 200. Used to verify the "Automated Lead Scraper" example:
  a node named `Manual Trigger` exists, the connections map references `Start`,
  the workflow has 6 nodes, and 4 of them are orphaned.
  Node names as fetched: Manual Trigger, Run Apify Scraper, Clean Data,
  Export to Google Sheets, Variables, Sticky Note.

The primary dataset lives in `../data/` (`summary.jsonl`, `findings.jsonl`,
`index.json`). Every number in the study is recomputable from `summary.jsonl`
with `../recount.py`.
