import requests
import json
import discord
from discord.ext import commands

TOKEN = ""
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print ("Bot is ready.")




@client.event
async def on_message(message):
    if message.content.startswith("!track"):
        tracking_id=str(message.content[7:])
        url="http://api.uscwe.wangruan.net/api/track/list"
        tracking_sns={"sns": str(tracking_id)}
        headers={
            "Host": "api.uscwe.wangruan.net",
            "Connection": "keep-alive",
            "Content-Length": "22",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": "http://youjianj.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "DNT": "1",
            "Content-Type": "application/json",
            "Referer": "http://youjianj.com/web/html/search.html?sns="+str(tracking_id),
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
        }
        try:
            r = requests.post(url,data=json.dumps(tracking_sns),headers=headers)
            #print(r.text)
            track_info=json.loads(r.text)
            track_info=track_info["Data"][0]["rows"]
            embed = discord.Embed(
                    title="运单号 >>  "+ tracking_id+ "       **Latest Status >> ** "+track_info[0]["Remark"],
                    description = "Detail Info:",
                    color= discord.Color.blue(),
                )
            embed.set_author(name="SkrNotify Tracking Bot",icon_url="https://pbs.twimg.com/profile_images/1115749378160037888/oPz9ZxOu_400x400.jpg",url="http://youjianj.com/web/html/search.html?sns="+str(tracking_id))
            count=0
            for i in track_info:
                embed.add_field(name=i["Adddate"],value="Status: "+i["Remark"],inline=False)
            embed.set_footer(text= "©Powered By SkrNotify",icon_url="https://pbs.twimg.com/profile_images/1115749378160037888/oPz9ZxOu_400x400.jpg")
            await message.author.send(embed=embed)
            print("DM sent!")
            return
        except:
            print("Invalid input! Ingored!")
    else:
        return

        
client.run(TOKEN)
