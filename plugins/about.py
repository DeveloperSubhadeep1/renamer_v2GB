# Copyright (C) 2023 DX_MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN"

import os 
from pyrogram import Client, filters
from config import Config
token = Config.BOT_TOKEN
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Origional BOT :- <a href='https://t.me/BixbyRena'>Gangster Baby</a>\nCreater :- <a href='https://t.me/dxziyan'>Ziyan</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- KOYEB\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/dxziyan'>Ziyan</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/dxziyan'>**Ziyan**</a> ❤️",quote=True)
