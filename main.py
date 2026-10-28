import os
from flask import Flask, request
import telebot

BOT_TOKEN = "8878410135:AAH6d_kukgjRYErNrUWgXg3jhDIKXG1hyIg"
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot is LIVE on Render!\n\nGold Signals Ready!\n\nCommands:\n/price - Check Gold Price\n/signal - Test Signal\n/help - Help")

@bot.message_handler(commands=['price'])
def price(message):
    bot.reply_to(message, "💰 XAUUSD: 2650.00\n📈 Trend: BULLISH\n\n(Demo price - we will connect real API next)")

@bot.message_handler(commands=['signal'])
def signal(message):
    bot.reply_to(message, "📈 GOLD BUY SIGNAL\nEntry: 2650\nSL: 2645\nTP: 2660\n\nTest signal working!")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Bot Commands:\n/start - Start bot\n/price - Gold price\n/signal - Test signal")

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def home():
    return 'Gold Signal Bot Running on Render - OK', 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
