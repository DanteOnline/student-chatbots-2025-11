import json
from datetime import datetime
from pathlib import Path


def append_trace(state: dict, message: str) -> list:
    return [*state["trace"], message]


def save_trace(result, prefix="trace"):
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = logs_dir / f"{prefix}_{timestamp}.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return out
