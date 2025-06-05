from datetime import datetime
from typing import Any

from app.utils.formatting import format_datetime

def dump_with_formatted_datetime(obj: Any) -> dict:
    """
    DTO or ORM → dict 변환 시 datetime 필드 포맷을 yyyy-MM-dd HH:mm:ss로 맞춰줌
    """
    if hasattr(obj, "model_dump"):
        raw = obj.model_dump(mode="json")
    elif hasattr(obj, "dict"):
        raw = obj.dict()
    else:
        raw = dict(obj)

    for k, v in raw.items():
        if isinstance(v, datetime):
            raw[k] = format_datetime(v)
    return raw
