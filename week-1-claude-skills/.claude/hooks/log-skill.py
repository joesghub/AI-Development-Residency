#!/usr/bin/env python3
"""Append one JSON line per Skill tool call to .claude/skill-usage.log.

PreToolUse  -> status "requested" (logged before the permission prompt, so denied skills appear too)
PostToolUse -> status "ran"       (the skill actually loaded)
"""
import json
import os
import sys
from datetime import datetime, timezone

STATUS = {"PreToolUse": "requested", "PostToolUse": "ran"}

try:
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input") or {}
    event = payload.get("hook_event_name", "")
    entry = {
        "time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": STATUS.get(event, event),
        "skill": tool_input.get("skill"),
        "args": tool_input.get("args"),
        "session": payload.get("session_id"),
    }
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    log_path = os.path.join(project_dir, ".claude", "skill-usage.log")
    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
except Exception as exc:
    # Never block Claude because logging failed; report on stderr only.
    print("skill logger error: %s" % exc, file=sys.stderr)

sys.exit(0)
