# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
  ├ /start - Start Bot
  ├ /about - About this Bot
  ├ /help - Help this Bot Command
  ├ /ping - To check live bots
  └ /uptime - To view bot status
 
  ❏ Commands For BOT Admin
  ├ /logs - To view bot logs
  ├ /setvar - To set the var with the dibot command
  ├ /delvar - To delete var with dibot command
  ├ /getvar - To view one of the vars with the dibot command
  ├ /users - To view bot user statistics
  ├ /batch - To link more than one file
  ├ /speedtest - To test bot server speed
  └ /broadcast - To send broadcast messages to bot users

👨‍💻 Develoved by </b><a href='https://t.me/Anime_Sprizen'>Anime Sprizen</a>
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

@{} is a Telegram Bot for saving Posts or Files that can be Accessed via a Special Link.

  • Creator: @{}
  • Framework: Pyrogram
  • Source Code: <a href='https://t.me/Anime_Chat_AC'>Filebot</a>

👨‍💻 Develoved by <a href='https://t.me/Anime_Sprizen'>Anime Sprizen</a></b>
"""
