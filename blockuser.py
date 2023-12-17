import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='++', intents=intents)

blocked_roles = {686934992152297513} # บทบาทที่กันไม่ให้เข้า สามารถ Copy Id Role @everyone ได้
exempted_users = {951901025713934376, 837294095335817226} # กำหนด User Id คนที่สามารถเชื่อมต่อได้

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel and any(role.id in blocked_roles for role in member.roles) and member.id not in exempted_users:
            embed = discord.Embed(
                title="การเข้าร่วม Voice Channel ถูกบล็อก",
                description=f"คุณไม่ได้รับอนุญาตให้เข้าร่วม Voice Channel `{after.channel.name}!`\n กรุณาติดต่อแอดมิน: **Pimsickgirl**",
                color=discord.Color.red()
            )
            await member.send(embed=embed)
            await member.move_to(None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


bot.run('TOKEN HERE')