# 🤖 Radhe-Style Telegram Bot

A **fun, multi-command Telegram bot** built in Python, featuring owner/sudo system and safe, reply/mention-based messaging. Ready for deployment on **Render** or local environment.

---

## ⚡ Features

- Fun commands with **reply or mention support**:
  - `/abuse` - Fun abuse messages
  - `/birthday` - Send birthday wishes
  - `/hraid` - Hraid messages
  - `/emoji` - Send emojis
  - `/porm` - Fun porm messages
  - `/lraid` - Love raid messages
  - `/sraid` - Super raid messages

- **Owner & Sudo system**:
  - `/addsudo` - Add sudo user (Owner only)
  - `/remsudo` - Remove sudo user (Owner only)
  - `/sudolist` - List sudo users (Owner only)
  - `/stop` - Stop the bot (Owner/Sudo only)

- `/help` - Shows all commands and descriptions
- Delay of **0.1 seconds** between messages to prevent spam
- Single-file deployment, easy to maintain

---

## 🛠 Requirements

- Python 3.10+ recommended
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)

```bash
pip install -r requirements.txt
