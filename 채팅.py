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
    game = discord.Game('배고파서 뭐 먹을려고') # ~~ 하는중
    await client.change_presence(status=discord.Status.online, activity=game)

############################명령어 시작#############################################

@client.event
async def on_message(message):

    if message.content == "짱돌아 dannnnwm":
        await message.channel.send (f"명단우 멍청이 ㅋ")
    if message.content == "짱돌아":
        await message.channel.send (f"ㅇ..?")
    if message.content == "짱돌아 뭐해":
        await message.channel.send(random.choice(['배고파서 뭐 먹으려구..', '노래 들으려구 노래 찾는중이였는데..' ,'Zzz' ,'다른 서버방장 도와주고 있었는데 ㅎ' ,'ㅇ? 너랑 채팅 하잖아'])) 
    if message.content == "짱돌아 머해":
        await message.channel.send(random.choice(['배고파서 뭐 먹으려구..', '노래 들으려구 노래 찾는중이였는데..' ,'Zzz..' ,'다른 서버방장 도와주고 있었는데 ㅎ' ,'ㅇ? 너랑 채팅 하잖아'])) 
    if message.content == "짱돌아 ㅎㅇ":
        await message.channel.send (f"ㅎㅇ..")
    if message.content == ("짱돌아 안녕"):    
        await message.channel.send (f"안녕")
    if message.content == "짱돌아 안농":
        await message.channel.send (f"ㅓ..안녕(안녕이라는 뜻이겠지..?)")
    if message.content == "짱돌아 안냥":
        await message.channel.send (f"ㅓ..안녕(안녕이라는 뜻이겠지..?)")
    if message.content == "짱돌아 얀넝":
        await message.channel.send (f"ㅓ..안녕(안녕이라는 뜻이겠지..?)")
    if message.content == "짱돌아 앙녕":
        await message.channel.send (f"ㅓ..안녕(안녕이라는 뜻이겠지..?)")
    if message.content == "짱돌아 안넝":
        await message.channel.send (f"ㅓ..안녕(안녕이라는 뜻이겠지..?)")
    if message.content == "짱돌아 ㅂㅇ":
        await message.channel.send (f"ㅂㅇ..")
    if message.content == "짱돌아 바이":
        await message.channel.send (f"ㅂㅇ..")
    if message.content == "짱돌아 ㅂㅂ":
        await message.channel.send (f"ㅂㅇ..")
    if message.content == "짱돌아 ㅃㅃ":
        await message.channel.send (f"ㅂㅇ..")
    if message.content == "짱돌아 배고파":
        await message.channel.send (f"초밥 먹을래?")
    if message.content == "짱돌아 배고파..":
        await message.channel.send (f"초밥 ㄱㄱ?")
    
    if message.content == "짱돌아 배고파...":
        await message.channel.send (f"초밥 맛집있는데 가자!")
    if message.content == "짱돌아 배고프다":
        await message.channel.send (f"초밥?")
    if message.content == "짱돌아 뭐 먹어?":
        await message.channel.send (f"춰밟먹눈준..(우물)")
    if message.content == "짱돌아 뭐 먹을려고?":
        await message.channel.send (f"아..오늘은 광어초밥이 땡기는데..")
    if message.content == "짱돌아 뭐 먹을껀데?":
        await message.channel.send (f"회 먹을까 생각중")
    if message.content == "짱돌아 심심해":
        await message.channel.send (f"..나도")
    if message.content == "짱돌아 닥쳐":
        await message.channel.send (f"?")
    if message.content == "짱돌아 자?":
        await message.channel.send (f"Zzzz...")
    if message.content == "짱돌아 자니?":
        await message.channel.send (f"Zzz..")
    if message.content == "짱돌아 ㅗ":
        await message.channel.send (f"ㅗㅗ")
    if message.content == "짱돌아 ㅗㅗ":
        await message.channel.send (f"ㅗㅗㅗ")
    if message.content == "짱돌아 ㅗㅗㅗ":
        await message.channel.send (f"ㅗㅗㅗㅗ")
    if message.content == "짱돌아 ㅗㅗㅗㅗ":
        await message.channel.send (f"ㅗㅗㅗㅗㅗ")
    if message.content == "짱돌아 ㅗㅗㅗㅗㅗ":
        await message.channel.send (f"ㅗㅗㅗㅗㅗㅗ")
    if message.content == "짱돌아 ㅗㅗㅗㅗㅗㅗ":
        await message.channel.send (f"ㅗㅗㅗㅗㅗㅗㅗㅗ")
    if message.content == "짱돌아 ㅗㅗㅗㅗㅗㅗㅗ":
        await message.channel.send (f"딱대")
    if message.content == "짱돌아 사랑해":
        message = await message.channel.send("으..")
        await asyncio.sleep(0.1) #초
        await message.edit(content="나도..:heart:") #수정될 메시지
        await asyncio.sleep(0.2) #초
    if message.content == "짱돌아 ㅎㅎ":
        await message.channel.send (f"ㅎ..")
    if message.content == "짱돌아 인사":
        message = await message.channel.send("ㅗㅗ")
        await asyncio.sleep(0.1) #초
        await message.edit(content="안") #수정될 메시지
        await asyncio.sleep(0.2) #초
        await message.edit(content="녕") #수정될 메시지
        await asyncio.sleep(0.2) #초

    if message.content == "노멘션안녕":
        await message.channel.send ("{} 님 안녕하세요".format(message.author))




client.run("OTQxODg3MDI0MDgyODQ1Njk3.GB2kdo.2ZYmgYd0Kjd649t9tGRGn_IQOLsQO6mmf0dkSM") # 토큰 적는곳