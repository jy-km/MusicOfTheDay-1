import os
import random
import disnake
from discord_slash import SlashCommand
from disnake import FFmpegPCMAudio
from disnake.ext import commands


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='`', intents=intents)
slash = SlashCommand(bot, sync_commands=True)
#test_guilds = ['']

@bot.event
async def on_ready():
  await bot.change_presence(status = disnake.Status.online, activity = disnake.Game('Camellia Bangers'))
  print('The bot is ready to go.')


music_links = [
    "https://www.youtube.com/watch?v=4kcpZpytqEo",
    "https://www.youtube.com/watch?v=lc4nTM6M9KY&t=0s",
    "https://www.youtube.com/watch?v=XXDNPX-oYCI",
    "https://www.youtube.com/watch?v=p9ex56FXdSE",
    "https://www.youtube.com/watch?v=o1OMXNJ9mHM"
]
game_links = [
    "https://www.youtube.com/watch?v=DjztpU8yVAo",
    "https://www.youtube.com/watch?v=OQQPnGEr_eg",
    "https://www.youtube.com/watch?v=toeWQFnyFFQ",
    "https://www.youtube.com/watch?v=cvRjbZlACek"
]
music_files = [
  "bigshot.wav",
  "burning_aquamarine.wav",
  "tremendous.wav",
  "world_revolving.wav",
  "OOPARTS.ogg"
]

my_secret = os.environ["DISCORD_BOT_SECRET"]

# @bot.command(aliases=['u'])
# async def used(ctx):
#   global times_used
#   times_used = 0
#   await ctx.send(times_used)
#   times_used += 1
  
@slash.slash(name="Test", description="asdfl;kj")
async def test(ctx):
  await ctx.send("asdf;lkj")

@bot.command(aliases=['p'])
async def ping(ctx):
  await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
  if round(bot.latency * 1000) == 69:
    await ctx.send('sus')
  #times_used += 1

@bot.command(aliases=['g'])
async def game(ctx):
    game_link = random.choice(game_links)
    await ctx.send("Here is the gaming videos of the month, hope you enjoy!")
    await ctx.send(game_link)
    if game_link == "https://www.youtube.com/watch?v=DjztpU8yVAo":
        await ctx.send("The game is ADOFAI and the song is Once Again by Cansol(player:Nephrolepis).")
    elif game_link == "https://www.youtube.com/watch?v=OQQPnGEr_eg":
        await ctx.send("The game is ADOFAI and the song is Feral by Meganeko(player:BWen).")
    elif game_link == "https://www.youtube.com/watch?v=toeWQFnyFFQ":
        await ctx.send("The game is DJMAX and the song is Road Of Death by NieN(player:REMILIA).")
    elif game_link == "https://www.youtube.com/watch?v=cvRjbZlACek":
        await ctx.send(
            "The game is Arcaea and the song is Tempestissimo by t+pazolite(player:BengaleeHS)."
        )
    #times_used += 1


@bot.command(aliases=['m'])
async def music(ctx):
    music_link = random.choice(music_links)

    await ctx.send("Here is the music of the month, hope you enjoy!")
    await ctx.send(music_link)
    if music_link == "https://www.youtube.com/watch?v=4kcpZpytqEo":
        await ctx.send("The music is Burning Aquamarine by Camellia.")
    elif music_link == "https://www.youtube.com/watch?v=lc4nTM6M9KY&t=0s":
        await ctx.send("The music is ΩΩPARTS by Camellia.")
    elif music_link == "https://www.youtube.com/watch?v=XXDNPX-oYCI":
        await ctx.send("The music is TremENDouS by Camellia.")
    elif music_link == "https://www.youtube.com/watch?v=p9ex56FXdSE":
        await ctx.send(
            "The music is THE WORLD REVOLVING (Camellia Remix) by Camellia(of course)."
        )
    elif music_link == "https://www.youtube.com/watch?v=o1OMXNJ9mHM":
        await ctx.send("The Music is BIG SHOT (Camellia Remix) by Camellia.")
    #times_used += 1


@bot.command(aliases=['v'])
async def vote(ctx):
    embed = disnake.Embed(
        title="Vote your favorite music of the month!",
        url=
        "https://docs.google.com/forms/d/1ck-gKrJdIS3s6NicjVAfstvPvgKIiNYU-Xm2o5_duaw/edit#settings",
        description="Please choose and type one of the following:",
        color=0x109319)

    embed.set_author(
        name="Music of the Month",
        icon_url=
        "https://www.journaldujapon.com/wp-content/uploads/2019/05/Camellia.jpg"
    )

    embed.add_field(name="Choose 1 for Burning Aquamarine by Camellia",
                    value="1 for Burning Aquamarine by Camellia",
                    inline=True)
    embed.add_field(name="Choose 2 for ΩΩPARTS by Camellia",
                    value="2 for ΩΩPARTS by Camellia",
                    inline=True)
    embed.add_field(name="Choose 3 for TremENDouS by Camellia",
                    value="3 for TremENDouS by Camellia",
                    inline=True)
    embed.add_field(
        name="Choose 4 for THE WORLD REVOLVING (Camellia Remix) by Camellia",
        value="4 for THE WORLD REVOLVING (Camellia Remix) by Camellia",
        inline=True)
    embed.add_field(name="Choose 5 for BIG SHOT(Camellia Remix) by Camellia",
                    value="5 for BIG SHOT(Camellia Remix) by Camellia",
                    inline=True)

    embed.set_footer(text="Please, click the link to go to the Google Form.")

    ctx.author.display_name

    ctx.author.avatar_url

    await ctx.send(embed=embed)
    #times_used += 1

@bot.command(aliases=['j'])
async def join(ctx):
  voice_channel = ctx.author.voice.channel
  music_file = random.choice(music_files)
  if voice_channel != None:
    if voice_channel:
      vc = await voice_channel.connect()
      vc.play(FFmpegPCMAudio(source = music_file))
      if music_file == "bigshot.wav":
        await ctx.send("The music is BIG SHOT(Camellia Remix) by Camellia.")
      elif music_file == "burning_aquamarine.wav":
        await ctx.send("The music is Burning Aquamarine by Camellia.")
      elif music_file == "tremendous.wav":
        await ctx.send("The music is TremENDouS by Camellia.")
      elif music_file == "world_revolving.wav":
        await ctx.send(
            "The music is THE WORLD REVOLVING (Camellia Remix) by Camellia(of course)."
        )
      elif music_file == "OOPARTS.ogg":
        await ctx.send("The Music is ΩΩPARTS by Camellia.")
    else:
      await ctx.send(str(ctx.author.name) + " is not in a channel.")
  #times_used += 1

@bot.command(aliases=['s'])
async def stop(ctx):
    voice = disnake.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently the audio ain't stopping lol")
    #times_used += 1

@bot.command(aliases=['c'])
async def cont(ctx):
    voice = disnake.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Currently the audio ain't playing lol")
    #times_used += 1
    
@bot.command(aliases=['l'])
async def leave(ctx):
  voice = disnake.utils.get(bot.voice_clients, guild=ctx.guild)
  if voice.is_connected():
    await voice.disconnect()
    await ctx.send("It got kicked off")
  else:
    await ctx.send("The bot ain't connected to the vc lol")
  #times_used += 1

@bot.command(aliases=['r'])
async def rec(ctx, user: disnake.Member, *, message=None):
    rec_link = random.choice(music_links)
    if rec_link == "https://www.youtube.com/watch?v=4kcpZpytqEo":
        rec_title = ("The music is Burning Aquamarine by Camellia.")
    elif rec_link == "https://www.youtube.com/watch?v=lc4nTM6M9KY&t=0s":
        rec_title = ("The music is ΩΩPARTS by Camellia.")
    elif rec_link == "https://www.youtube.com/watch?v=XXDNPX-oYCI":
        rec_title = ("The music is TremENDouS by Camellia.")
    elif rec_link == "https://www.youtube.com/watch?v=p9ex56FXdSE":
        rec_title = (
            "The music is THE WORLD REVOLVING (Camellia Remix) by Camellia(of course)."
        )
    elif rec_link == "https://www.youtube.com/watch?v=o1OMXNJ9mHM":
        rec_title = ("The Music is BIG SHOT (Camellia Remix) by Camellia.")
    await user.send(rec_link)
    await user.send(rec_title)
    await ctx.send("Sent music successfully")
    #times_used += 1

@bot.command(aliases=['a'])
async def assist(ctx):
    embed = disnake.Embed(
        title="Music of the Month Aid",
        color=0x109319)

    embed.set_author(
        name="Music of the Month",
        icon_url=
        "https://www.journaldujapon.com/wp-content/uploads/2019/05/Camellia.jpg"
    )

    embed.add_field(name="ping(p)",
                    value="Just a function to figure out the latency of the bot and your computer!",
                    inline=True)
    embed.add_field(name="help(h)",
                    value="You are looking at this command.",
                    inline=True)
    embed.add_field(name="game(g)",
                    value="A function to recommend you gaming videos that are related to various Rhythm Games!",
                    inline=True)
    embed.add_field(name="music(m)",
                    value="A command for recommending music(the most major function of this bot(changed monthly)",
                    inline=True)
    embed.add_field(
                    name="vote(v)",
                    value="A function to vote your favorite piece of music!",
                    inline=True)
    embed.add_field(
                    name ="join(j)",
                    value = "A function available in voice channels so that you can listen to selected pieces of music!",
                    inline=True)
    embed.add_field(
                    name ="stop(s)",
                    value = "A function available in voice channels so that you can pause after listening to music!",
                    inline=True)
    embed.add_field(
                    name ="cont(c)",
                    value = "A function available in voice channels so that you can continue to listen to music after stopping it!",
                    inline=True)
    embed.add_field(
                    name="Soon™",
                    value="Soon™",
                    inline=True)

    embed.set_footer(text="The prefix is `, and it won't work if you don't put that before the command.")

    ctx.author.display_name

    ctx.author.avatar_url

    await ctx.send(embed=embed)
    #times_used += 1

# @bot.command(aliases=['t'])
# async def test(ctx, msg):
#   await ctx.send("asdf;lkjasdf;lkjasdf;lkasdf;lkjsd")
#   def test():
#     return msg.author == ctx.author and msg.channel == ctx.channel and \
#     msg.content.lower() in ["y", "n"]

#   msg = await bot.wait_for("message", check=test)
#   if msg.content.lower() == "y":
#     await ctx.send("You said yes!")
#   else:
#     await ctx.send("You said no!")

bot.run('OTEyNzU3OTU0MDM2NTIzMDE5.YZ0mFg.JcreHFpBsTKr5Xd44BuHxUdVu7M')