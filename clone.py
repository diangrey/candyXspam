import telebot
import threading
import time
import random

# ========== CONFIG ==========
CLONE_BOT_TOKEN = "8406077185:AAHOJ22GH7Hzp4l_KyHESE1Xa4_FLJI_Y3k"
MAIN_OWNER_ID = 5311223486
SPAM_DELAY = 0.1

# ========== BOT INIT ==========
bot = telebot.TeleBot(CLONE_BOT_TOKEN, parse_mode="HTML")

# ========== DATA ==========
from data import ABUSE, FLIRT, SRAID, HRAID, PORMS

# ========== CLONE OWNER ==========
CLONE_OWNER_ID = None  # will be set on first /start

# ========== SPAM CONTROL (PER CHAT) ==========
spam_active = {}   # chat_id : True / False

# ========== PERMISSION ==========
def is_allowed(uid):
    return uid == CLONE_OWNER_ID or uid == MAIN_OWNER_ID

# ========== SPAM LOOP ==========
def start_spam(message, data_list):
    chat_id = message.chat.id

    if not message.reply_to_message:
        bot.reply_to(message, "❌ Reply to a user")
        return

    target = message.reply_to_message.from_user
    mention = f"<a href='tg://user?id={target.id}'>{target.first_name}</a>"

    spam_active[chat_id] = True

    while spam_active.get(chat_id):
        bot.send_message(
            chat_id,
            f"{mention} {random.choice(data_list)}"
        )
        time.sleep(SPAM_DELAY)

# ========== START ==========
@bot.message_handler(commands=["start"])
def start_cmd(message):
    global CLONE_OWNER_ID

    if CLONE_OWNER_ID is None:
        CLONE_OWNER_ID = message.from_user.id

    bot.reply_to(
        message,
        "🤖 Clone Bot Started\n\n"
        f"Owner ID: {CLONE_OWNER_ID}\n"
        "Spam delay: 0.1s"
    )

# ========== ABUSE ==========
@bot.message_handler(commands=["abuse"])
def abuse_cmd(message):
    if not is_allowed(message.from_user.id):
        return
    threading.Thread(
        target=start_spam,
        args=(message, ABUSE),
        daemon=True
    ).start()

# ========== FLIRT ==========
@bot.message_handler(commands=["flirt"])
def flirt_cmd(message):
    if not is_allowed(message.from_user.id):
        return
    threading.Thread(
        target=start_spam,
        args=(message, FLIRT),
        daemon=True
    ).start()

# ========== SRAID ==========
@bot.message_handler(commands=["sraid"])
def sraid_cmd(message):
    if not is_allowed(message.from_user.id):
        return
    threading.Thread(
        target=start_spam,
        args=(message, SRAID),
        daemon=True
    ).start()

# ========== HRAID ==========
@bot.message_handler(commands=["hraid"])
def hraid_cmd(message):
    if not is_allowed(message.from_user.id):
        return
    threading.Thread(
        target=start_spam,
        args=(message, HRAID),
        daemon=True
    ).start()

# ========== PORM ==========
@bot.message_handler(commands=["porm"])
def porm_cmd(message):
    if not is_allowed(message.from_user.id):
        return
    threading.Thread(
        target=start_spam,
        args=(message, PORMS),
        daemon=True
    ).start()

# ========== STOP (PER CHAT) ==========
@bot.message_handler(commands=["stop"])
def stop_cmd(message):
    if not is_allowed(message.from_user.id):
        return

    chat_id = message.chat.id
    if spam_active.get(chat_id):
        spam_active[chat_id] = False
        bot.reply_to(message, "🛑 Spam stopped in this chat")
    else:
        bot.reply_to(message, "⚠️ No spam running here")

# ========== RUN ==========
print("Clone bot running...")
bot.infinity_polling()
