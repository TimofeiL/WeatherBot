# WeatherBot
Бот который показывает погоду в любом городе, стране, населенном пункте.
Бот работает при помощи сервиса openweathermap.org.

В коде в переменной "Owm_key" надо указать API ключ который надо получить
заходим на сайт https://openweathermap.org/ и там надо зарегистрироваться
когда вы зарегистрировались переходите во вкладку API KEYS и там создаёте
новый ключ и называете его как душе угодно, после чего копируете его и 
вставляете в ваш код.

В переменной "Telegram_key" надо указать ключ телеграм бота которого нужно
создать, для этого переходим к боту botFather https://t.me/BotFather и 
создаёте бота при помощи команды /newbot, указываете имя и nickname.
В итоге получаете ключ и копируете его в код.

Для того чтобы всё заработало нужно установить нужные модули:
pip install pyowm
pip install pyTelegramBotAPI

Запускаем код находим нашего бота, botFather даёт ссылку на него и радуемся!