# 轻芒杂志 马克内容自动同步

解析轻芒杂志-马克文章、内容及笔记 API, 定时同步到其他平台。

API 示例: https://qingmang.me/users/11/feed/

## 当前版本

当前版本特性：

- 简单配置，仅限一个人使用
- 可用 QingMang -> Flomo
- Telegram BOT 不可用

## 环境

`python 3`

## 使用

1. `python --version` 检查 Python 3 版本环境；
2. 通过`pip`根据`requirements.txt`安装相关依赖；
3. 如果第一次使用，项目目录下需要手动创建 `db` 文件夹；
4. 根据[配置](#配置)设置自己的 `flomo_api` 和 `qingmang_api`；
5. `python console_start.py`

## 配置

程序相关配置主要位于 `config.py`

- `delay`: 每次同步新内容的间隔时间，单位秒；
- `FLOMO_API`: FLOMO 发送内容 API
- `QINGMANG_RSS_API `: 轻芒杂志 已马克内容及笔记 API
- `message_template`: 可自定义消息的格式



## 已知 bug

