import telebot
import time

# Укажите токен вашего бота и ID администратора
BOT_TOKEN = "7058049208:AAEOjf-NWmsQKYiQSiJaQx5EZeBdt6a1eKI"
ADMIN_ID = 1360417852

# Создаем экземпляр бота
bot = telebot.TeleBot(BOT_TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Привет! Отправь сюда свой вопрос, и он будет передан анонимно.")

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    question = message.text
    # Пересылаем сообщение администратору
    bot.send_message(ADMIN_ID, f"Новый анонимный вопрос: {question}")
    bot.reply_to(message, "Ваш вопрос отправлен. Спасибо!")

# Запуск бота с обработчиком ошибок
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        time.sleep(5)  # Ждем 5 секунд перед повторным запуском
