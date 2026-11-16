# -*- coding: utf-8 -*-
"""校园课程表助手 命令行主程序。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from storage import load_courses, save_courses  # noqa: E402

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def add_course():
    """录入一门课程。"""
    name = input("课程名称：").strip()
    if not name:
        print("课程名称不能为空。")
        return
    day = input("星期（1-7，1 表示周一）：").strip()
    if not day.isdigit() or not (1 <= int(day) <= 7):
        print("星期输入无效，应在 1-7 之间。")
        return
    period = input("节次（如 1-2 节）：").strip()
    place = input("上课地点：").strip()
    teacher = input("授课教师：").strip()

    courses = load_courses()
    courses.append({
        "name": name,
        "day": int(day),
        "period": period,
        "place": place,
        "teacher": teacher,
    })
    save_courses(courses)
    print("课程已保存。")


def list_week():
    """按星期列出全部课程。"""
    courses = load_courses()
    if not courses:
        print("暂无课程记录。")
        return
    for index, day in enumerate(WEEKDAYS, start=1):
        today = [c for c in courses if c["day"] == index]
        if not today:
            continue
        print(f"\n{day}")
        for c in today:
            print(f"  {c['period']}  {c['name']}  @ {c['place']}  教师：{c['teacher']}")


def remove_course():
    """按序号删除课程。"""
    courses = load_courses()
    if not courses:
        print("暂无课程记录。")
        return
    list_week()
    idx = input("输入要删除的课程序号（从 1 开始）：").strip()
    if not idx.isdigit() or not (1 <= int(idx) <= len(courses)):
        print("序号无效。")
        return
    removed = courses.pop(int(idx) - 1)
    save_courses(courses)
    print(f"已删除：{removed['name']}")


def main():
    menu = {
        "1": ("录入课程", add_course),
        "2": ("查看周课程表", list_week),
        "3": ("删除课程", remove_course),
        "4": ("退出", None),
    }
    while True:
        print("\n===== 校园课程表助手 =====")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        choice = input("请选择操作：").strip()
        if choice == "4":
            print("再见！")
            break
        action = menu.get(choice, (None, None))[1]
        if action is None:
            print("无效选择，请重试。")
        else:
            action()


if __name__ == "__main__":
    main()
