import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('b6e342c505c7672621eba45c14ee1332', config_dict)

bot = telebot.TeleBot("1124179786:AAEChjgdygfmN-3D288f7xqF8jSQ0M26Jb8", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)

    wthr = observation.weather

    temperature = wthr.temperature('celsius')["temp"]

    answer = 'В городе "' + message.text + '"' + ' сейчас ' + str(wthr.detailed_status) + '\n'

    answer += 'Температура на улице равна ' + str(temperature) + '\n'

    if temperature < 10:
        answer += 'На улице холодно, стоит надеть куртку'
    elif temperature < 15:
        answer += 'На улице свежо, кофта будет не лишней'
    else:
        answer += 'На улице тепло, можно идти в футболке'

    # Бот отвечает на сообщения, с ссылкой на сообщение
    # bot.reply_to(message, message.text)

    # Бот отвечает на сообщения без ссылки
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)