from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import telebot

Owm_key = '' # АРI ключ Зарегистрируйтесь:"https://openweathermap.org/" и создайте API KEY:"https://home.openweathermap.org/api_keys"
Telegram_key = '' # Ключ от бота который вы должны создать "https://t.me/BotFather"

config_dict = config.get_default_config()
config_dict['language'] = 'ru' # Язык
owm = OWM(Owm_key, config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot(Telegram_key, parse_mode=None)
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
