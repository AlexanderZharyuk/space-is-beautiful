# SPACE IS BEAUTIFUL

This repository contains scripts for downloading photos from NASA and SpaceX sites and telegram bot that posts with countless photos in your telegram group.

## Setting up your development environment

All used libraries in the specified **requirements.txt** file
To install the library in the environment, write the command:

```
pip install -r requirements.txt
```

For the script to work, you definitely need to create a `.env` file, which should contain your credential data:

```
TELEGRAM_BOT_TOKEN={YOUR-TELEGRAM-BOT-TOKEN}
TELEGRAM_GROUP_ID={YOUR-TELEGRAM-GROUP-ID}
NASA_API_KEY={YOUR-NASA-API-KEY}
POST_DELAY={POST DELAY IN SECOND}
DOWNLOAD_DIR={NAME OF DIRECTORY-WHERE-IMAGES-WILL BE STORED}
```

### Description of files and work with them
1. **donwload_apod.py**

This script downloads 30 photos of the day from the NASA website. Use without arguments
```
python3 download_apod.py
```
2. **download_epic.py**
This script downloads photos of the Earth at different times. Use without arguments
```
python3 download_epic.py
```
3. **fetch_spacex_last_launch.py**
This script downloads photos from a SpaceX rocket launch. Taken 1 argument - the launch identifier, if it is not specified when considering the program - it produces photos with the last launch.
An example of running a script:
```
python3 fetch_spacex_last_launch.py 67
```
4. **telegram_bot.py**
This script is responsible for posts by the bot to the group. By default, a post is made every 4 hours, if you want to set your own time - set the `POST_DELAY` variable in the `.env` file.
The bot launch by command:
```
python3 telegram_bot.py
```
All pictures after the scripts work are placed in the folder that you specified in the `.env` file and set `DOWNLOAD_DIR`.

## The author

* [Alexander Zharyuk](https://gist.github.com/AlexanderZharyuk)
