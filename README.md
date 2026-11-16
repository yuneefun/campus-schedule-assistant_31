# 校园课程表助手（campus-schedule-assistant_31）

一个面向在校生的轻量级课程表助手：在本地录入与查看每周课程安排，数据保存在本地 JSON 文件，无需注册、不依赖网络。

## 功能特性

- 课程录入：记录课程名称、星期、节次、上课地点与授课教师；
- 周视图查看：按周一至周日切换查看当周课程；
- 课程删除：按序号移除不再需要的课程；
- 本地保存：课程数据写入 `data/schedule.json`，不上传云端。

## 环境依赖

- Python 3.8 及以上；
- 无第三方依赖，标准库即可运行。

## 快速开始

1. 克隆仓库：

   ```bash
   git clone https://github.com/yuneefun/campus-schedule-assistant_31.git
   cd campus-schedule-assistant_31
   ```

2. 运行程序：

   ```bash
   python src/schedule.py
   ```

3. 按菜单提示录入课程，选择“查看周课程表”即可按星期浏览。

## 数据格式

课程保存在 `data/schedule.json`，每条记录包含：

| 字段 | 含义 |
| --- | --- |
| name | 课程名称 |
| day | 星期，1-7 对应周一至周日 |
| period | 节次 |
| place | 上课地点 |
| teacher | 授课教师 |

## 项目结构

```
campus-schedule-assistant_31/
├── src/            # 源代码
├── data/           # 本地课程数据
├── docs/           # 贡献指南、分支规范、变更记录
├── .github/        # Issue 与 Pull Request 模板
├── README.md
├── LICENSE
└── requirements.txt
```

## 贡献

欢迎提交 Issue 与 Pull Request。参与方式与分支规范见 [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) 与 [`docs/BRANCHING.md`](docs/BRANCHING.md)。

## 许可证

本项目基于 [MIT License](LICENSE) 开源。

## 联系方式

如有使用问题或改进建议，欢迎在 Issue 区留言。
