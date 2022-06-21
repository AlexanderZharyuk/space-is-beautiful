# SPACE IS BEAUTIFUL

Данный репозиторий хранит в себе скрипты по скачиванию фотографий с сайтов NASA и SpaceX, а также телеграм бота, делающего посты с этими фотографиями в вашу телеграм-группу.

## Предустановка

Все используемые библиотеки указаны в файле **requirements.txt**
Для установки библиотек в виртуальное окружение используйте команды:

```
pip install -r requirements.txt
```

Для работы скрипта вам потребуется создать .env файл, в котором должны находиться ваши настройки скриптов:

```
TELEGRAM_BOT_TOKEN={YOUR-TELEGRAM-BOT-TOKEN}
TELEGRAM_GROUP_ID={YOUR-TELEGRAM-GROUP-ID}
NASA_API_KEY={YOUR-NASA-API-KEY}
POST_DELAY={POST-DELAY-IN-SECONDS}
DOWNLOAD_DIR={DIRNAME-WHERE-IMAGES-WILL-SAVE}
```

### Описание скриптов и работа с ними
1. **donwnload_apod**

Данный скрипт скачивает 30 фотографий дня с сайта NASA. Запускается без аргументов командой:
``` 
python3 download_apod.py
```
2. **download_epic**
Данный скрипт скачивает фотографии Земли в разное время. Запускается без аргументов командой:
``` 
python3 download_epic.py
```
3. **fetch_spacex_last_launch**
Данный скрипт скачивает фотографии с запуска ракет SpaceX. Принимает 1 аргумент - идентификатор запуска, если при запуске программы его не указать - выдаст фотографии с последнего запуска.
Пример запуска скрипта:
```
python3 fetch_spacex_last_launch.py 67
```
4. **telegram_bot**
Данный скрипт отвечает за посты ботом в группу. По дефолту пост делается раз в 4 часа, если вы хотите поставить свое время - настройте переменную `POST_DELAY` в `.env` файле.
Запуск бота осуществляется командой:
``` 
python3 telegram_bot.py
```
Все картинки после работы скриптов сохраняются в папку, которую вы указали в `.env`-файле в переменной `DOWNLOAD_DIR`.
## Создано при поддержке

* [DEVMAN](https://dvmn.org/) - Обучающая платформа

## Авторы

* [Alexander Zharyuk](https://gist.github.com/AlexanderZharyuk)