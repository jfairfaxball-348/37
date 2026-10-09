#!/usr/bin/env python3
"""Minimal repository consistency and local-Markdown-link checker; not a proof."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "LICENSE",
    "docs/RESEARCH_PIPELINE.md", "docs/SESSION_PROTOCOL.md",
    "docs/ENUMERATION_DESIGN.md", "docs/NOVELTY_STANDARD.md",
    "research/STATE.json", "research/NEXT_SESSION.md",
    "research/CLAIMS.md", "research/CANDIDATES.md",
    "research/DECISION_LOG.md", "research/NOVELTY_LEDGER.md",
    "research/EXPERIMENT_LEDGER.md", "research/PROGRESS_AUDITS.md",
    "research/AI_USE.md", "research/sessions/P000_BOOTSTRAP.md",
    "research/prompts/P000_INPUT.md",
    "scripts/enumerate.py", "tests/test_enumerate.py",
    ".github/workflows/research.yml",
]
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


def main() -> int:
    problems = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            problems.append("missing: " + rel)
    state_path = ROOT / "research/STATE.json"
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            next_path = state.get("next_prompt")
            if not isinstance(next_path, str) or not (ROOT / next_path).is_file():
                problems.append("state next_prompt is missing")
            else:
                prompt = (ROOT / next_path).read_text(encoding="utf-8")
                if state.get("next_session") not in prompt:
                    problems.append("next prompt does not identify state.next_session")
            if state.get("repository") != "jfairfaxball-348/37":
                problems.append("state repository mismatch")
        except (ValueError, TypeError) as error:
            problems.append("invalid state: " + str(error))
    for page in ROOT.rglob("*.md"):
        if ".git" in page.parts:
            continue
        content = page.read_text(encoding="utf-8")
        for match in LINK.finditer(content):
            raw = match.group(1).strip().split(" ", 1)[0].strip("<>")
            if not raw or raw.startswith("#"):
                continue
            parts = urlsplit(raw)
            if parts.scheme or parts.netloc or raw.startswith("mailto:"):
                continue
            target = (page.parent / unquote(parts.path)).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.exists():
                problems.append(str(page.relative_to(ROOT)) + ": broken link " + raw)
    if problems:
        for problem in problems:
            print("FAIL: " + problem)
        return 1
    print("PASS: scaffold files, state pointer and local Markdown links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

