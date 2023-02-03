from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import telebot

config_dict = config.get_default_config()
config_dict['language'] = 'ru'
owm = OWM('Your key "https://t.me/BotFather"', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("1853857581:AAHlSj1TNlhrCTTqSxQ4d0aWO-FPDXi5SlM", parse_mode=None)
@bot.message_handler(content_types=['text'])

def send_welcome(message):
	place = message.text
	try:
		observation = mgr.weather_at_place(place)
		w = observation.weather
		bot.send_message(message.chat.id, 'В городе/стране ' + place + ' сейчас ' + str(w.temperature('celsius')['temp']) + ' градуса(ов) по цельсию')
		bot.send_message(message.chat.id, 'Ветер ' + str(w.wind()['speed']) + ' метров в секунду')
		bot.send_message(message.chat.id, 'На улице сейчас ' + w.detailed_status)
	except:
		bot.send_message(message.chat.id, 'Данные введены некорректно!')

bot.polling(none_stop = True)
