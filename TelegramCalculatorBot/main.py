import telebot

bot = telebot.TeleBot("")

users = []  # Тут был бы список или бд, который сохранялся


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.chat.id not in users:
        bot.send_message(message.chat.id,
                         "Привет, чтобы начать введите пароль через команду '/password', после вам будет доступен "
                         "калькулятор.\nЧтобы им воспользоваться введите 'solve' и через пробел выражение.")
    else:
        bot.send_message(message.chat.id,
                         "Рад снова вас видеть!")


@bot.message_handler(commands=['password'])
def password(message):
    if message.text == "/password 12345":
        users.append(message.chat.id)
        bot.send_message(message.chat.id,
                         "Добро пожаловать! Теперь у вас есть доступ к 'solve'")
    else:
        bot.send_message(message.chat.id,
                         "Неверный пароль, попробуйте снова.")


@bot.message_handler()
def solve(message):
    if "solve " in message.text and message.chat.id in users:
        try:
            x = message.text.replace('solve ', '')
            message.text = compile(x, 'string', 'eval')
        except SyntaxError:
            bot.send_message(message.chat.id,
                             "Выражение введено не верно, попробуйте еще раз.")
        try:
            answer = str(eval(message.text))
            bot.send_message(message.chat.id,
                             "Ответ будет " + answer)
        except NameError and TypeError:
            bot.send_message(message.chat.id,
                             "Выражение введено не верно, попробуйте еще раз.")
        except ZeroDivisionError:
            bot.send_message(message.chat.id,
                             "На ноль делить нельзя, попробуйте снова.")
    else:
        bot.send_message(message.chat.id,
                         "Вы не авторизованы, введите пожалуйста пароль.")


bot.infinity_polling()
