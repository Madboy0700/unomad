# UnuRobot

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](./LICENSE)
[![Translation status](https://hosted.weblate.org/widgets/unurobot/-/bot/svg-badge.svg)](https://hosted.weblate.org/engage/unurobot/)

Telegram Bot that allows you to play the popular card game UNO via inline queries. The bot currently runs as [@UnuRobot](http://t.me/UnuRobot).

To run the bot yourself, you will need:

- Python (tested with 3.7+)
- The [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) module
- [Pony ORM](https://ponyorm.com/)

## Setup

- Get a bot token from [@BotFather](http://t.me/BotFather) and change configurations in `config.json`.
- Convert all language files from `.po` files to `.mo` by executing the bash script `compile.sh` located in the `locales` folder.
  Another option is: `find . -maxdepth 2 -type d -name 'LC_MESSAGES' -exec bash -c 'msgfmt {}/unobot.po -o {}/unobot.mo' \;`.
- Use `/setinline` and `/setinlinefeedback` with BotFather for your bot.
- Use `/setcommands` and submit the list of commands in commandlist.txt
- Install requirements (using a `virtualenv` is recommended): `pip install -r requirements.txt`

You can change some gameplay parameters like turn times, minimum amount of players and default gamemode in `config.json`.
Current gamemodes available: Classic, Fast (Sanic), Wild, Text and 7-0. Check the details with the `/modes` command.

Then run the bot with `python3 bot.py`.

Code documentation is minimal but there.

## Translating

- Our translations are being done at our [Weblate](https://hosted.weblate.org/projects/unurobot/bot/) project.
  You can contribute to the currently supported languages or translate to a new language.
