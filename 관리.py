import discord
import asyncio
import random

from discord.utils import get

intents = discord.Intents.all()
intents.typing = True
intents.presences = True

client = discord.Client(intents = intents)


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')

@client.event
async def on_message(message):

#=============================짱돌아 청소==========================#

    if message.content.startswith("짱돌아 청소 "):   # 명령어를 적고 한칸 띄워주세요
        purge_number = message.content.replace("짱돌아 청소 ", "")   # 윗줄 명령어와 똑같이 해주세요
        check_purge_number = purge_number.isdigit()

        if check_purge_number == True:
            await message.channel.purge(limit=int(purge_number) + 1)
            msg = await message.channel.send(f"**{purge_number}개**의 메시지를 삭제했습니다.")
            await asyncio.sleep(3)   # ←초후에 ~개의 메시지를 삭제했습니다도 지워집니다
            await msg.delete()
        if message.content == ("짱돌아 청소"):
            await message.channel.send("뭐라는거야 몇개의 채팅을 삭제하라는거야..")  # 숫자를 입력하지 않았을때
    if message.content == "짱돌아 청소":
        await message.channel.send (f"뭐라는거야 몇개의 채팅을 삭제하라는거야..(뒤에다가 삭제항 채팅의 개수를 써..)") 

#=========================================================================#




client.run("OTQxODg3MDI0MDgyODQ1Njk3.GB2kdo.2ZYmgYd0Kjd649t9tGRGn_IQOLsQO6mmf0dkSM") # 토큰 적는곳