from spambot import BOT_TOKEN, OWNER_ID
import telebot
import random
import threading
import time
def start_clone(bot_token, clone_owner_id):
    bot = telebot.TeleBot(bot_token, parse_mode="HTML")
    spam_active = {}

    # simple spam loop example
    def spam_loop(message, data_list):
        chat_id = message.chat.id
        target = message.reply_to_message.from_user
        mention = f"<a href='tg://user?id={target.id}'>{target.first_name}</a>"
        spam_active[chat_id] = True
        while spam_active.get(chat_id):
            bot.send_message(chat_id, f"{mention} {random.choice(data_list)}")
            time.sleep(0.1)

    @bot.message_handler(commands=["start"])
    def start_cmd(m):
        bot.reply_to(m, f"👑 Clone Bot by @radhe_spam_bot \n\nOwner: {clone_owner_id}")

    threading.Thread(target=bot.infinity_polling).start()
    print(f"Clone started for owner {clone_owner_id}")
