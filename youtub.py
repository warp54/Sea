import discord
import asyncio
import openpyxl
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import os
import sys
import json
from selenium import webdriver

countG = 0
client = discord.Client()
players = {}
queues= {}
musiclist=[]
mCount=1
searchYoutube={}
searchYoutubeHref={}

def check_queue(id):
    if queues[id]!=[]:
        player = queues[id].pop(0)
        players[id] = player
        del musiclist[0]
        player.start()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='Testing', type=1))



@client.event
async def on_message(message):

    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요")

    if message.content.startswith("!들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)
        print("들어와")
        print(voice_client)
        print("들어와")
        if voice_client== None:
            await client.send_message(message.channel, '들어왔습니다')
            await client.join_voice_channel(channel)
        else:
            await client.send_message(message.channel, '봇이 이미 들어와있습니다.')




    if message.content.startswith("!나가"):
            server = message.server
            voice_client = client.voice_client_in(server)
            print("나가")
            print(voice_client)
            print("나가")
            if voice_client == None:
                await client.send_message(message.channel,'봇이 음성채널에 접속하지 않았습니다.') 
                pass
            else:
                await client.send_message(message.channel, '나갑니다') 
                await voice_client.disconnect()


    if message.content.startswith("!재생"):

        server = message.server
        voice_client = client.voice_client_in(server)
        msg1 = message.content.split(" ")
        url = msg1[1]
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player.is_playing())
        players[server.id] = player
        await client.send_message(message.channel, embed=discord.Embed(description="playing"))
        print(player.is_playing())
        player.start()        

    if message.content.startswith("!일시정지"):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="시간은 멈췄다..."))
        players[id].pause()

    if message.content.startswith("!다시재생"):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="다시 시간은 흐른다!"))
        players[id].resume()

    if message.content.startswith("!멈춰"):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="The World!"))
        players[id].stop()
        print(players[id].is_playing())


client.run('NjE3MDA3MTY4NzA0NzQxMzc2.XWpNuw.ki3syVNXBQ8ERu52MemBcTUEiag')        