## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCBYwRQfIzDA6U4J1NOFVfWY6fw6AAyFrzibQdJS8hySWjIoVi_4yzYxdORoAEh8YkrXdE2GicuC0olIvcBH_xxEgmzRR8yjxl-VvlUojGfLdxJP-dwLW-iP4DgcYFwPLfbBCNjZEmY_Bd6zOC9VPcnuKqK3oTF0segNRv-pVexC61_Dm-VapSUPCdogJt6X9sxtPpBZh6R5Pwkp3htL3Ku9pyKLlD3vmIw8q_YgBfhkJ98IrLrLTLtAiDMkHShBXlZ1EOQ4CfsWxe2o3nJfaMHChh3ECQkNLL7FlPdDfW17jeYIW0WBI-c0MCJAXBXAgi6vJEwnqdOXM02sNFmu1PNbdErCQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5192831405:AAGxZq9Iu7Y73GgDK-y5aknGXp27x6jNI38")
BOT_NAME = getenv("BOT_NAME", "MASOOM LOVER MUSIC")
API_ID = int(getenv("API_ID", "8260758")
API_HASH = getenv("API_HASH", "f1978dac0dafe758700fac54d207b26f")
OWNER_NAME = getenv("OWNER_NAME", "𓆩𝐈𝐍𝐃🇮🇳𓆪 ❥ ̶͢ ̶ͨ ̶ͧ ̶ͭ ̶ͤ❤⃝⃝𝐑𝐔𝐂𝐇𝐈𝐓𓆩♡𓆪🥀』")
OWNER_USERNAME = getenv("OWNER_USERNAME", "MASOOM_B0Y")
ALIVE_NAME = getenv("ALIVE_NAME", "𓆩𝐈𝐍𝐃🇮🇳𓆪 ❥ ̶͢ ̶ͨ ̶ͧ ̶ͭ ̶ͤ❤⃝⃝𝐂𝐇𝐈𝐑𝐀𝐆𓆩♡𓆪🥀』")
BOT_USERNAME = getenv("MASOOM_LOVER_BOT")
ASSISTANT_NAME = getenv("𓆩𝐈𝐍𝐃🇮🇳𓆪 𝐌𝐀𝐒𝐎𝐎𝐌 𝐋𝐎𝐕𝐄𝐑")
GROUP_SUPPORT = getenv("FULL_ON_MOJJ_MASTI")
UPDATES_CHANNEL = getenv("TEAM_IND_OFFICIAL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/0e22ed23875c1f98861d1.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/60e58cb38d433b6d3f9be.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/masoomboyop/RUCHIT-VC-PLAYER")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/895084a68fa3fa0f67cbf.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/2670c0b1767f27e638a03.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/19674366d407d51acd3c3.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/5bd68e986a4f3678186f6.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/3a7e32a3e55b4000bbd8c.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/fd0e674f8cc7f56e824d5.png")
