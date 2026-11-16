# -*- coding: utf-8 -*-
"""课程数据的本地 JSON 读写。"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "schedule.json"


def load_courses():
    """读取全部课程，文件不存在时返回空列表。"""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_courses(courses):
    """把课程列表写回本地 JSON 文件。"""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)
