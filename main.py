from pyrogram import filters,Client
from pyrogram.types import ReplyKeyboardMarkup
import uvloop,randomr
from vars import *



uvloop.install ()
#speed up using uvloop

bot = Client (
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

#special keyboard for  user
@bot.on_message ( filters.command ( 'start' ) & filters.private )
async def keyboardfunc (bot,message) :
    await message.reply (
        text='lets play ,'
             'Now enter your choice using option below...',
        reply_markup=ReplyKeyboardMarkup (
            [
                [
                    'rock'
                ],
                [
                    'paper'
                ],
                [
                    'scissor'
                ],
                [
                     '                                   exit'
                ]

            ]
        ) )

selections = ['rock','paper','scissor']
userscore: int = 0
computerscore: int = 0

#method for getting user message
@bot.on_message (filters.private)
async def getmsg (bot,message) :
    #chat_id=message.chat.id
    #message_id=message.id
    computer = random.choice ( selections )
    user=(message.text)
    if user == 'exit' :
        message.reply(exit ( 'you stoped game....' ))
    await message.reply ( 'I choose  ' + computer )
    if user == computer :
        await message.reply( "its tie  😐" )
    elif user == 'rock' :
        if computer == 'paper' :
            await message.reply( "you lose 🤭" )
            global computerscore
            computerscore += 1
        elif computer == 'scissor' :
            await message.reply( 'you win  😏' )
            global userscore
            userscore += 1
    if user == 'paper' :
        if computer == 'scissor' :
            await message.reply( "you lose   🤭" )
            computerscore += 1
        elif computer == 'rock' :
            await message.reply( 'you win 😏 ' )
            userscore += 1
    if user == 'scissor' :
        if computer == 'paper' :
            await message.reply( 'you lose  🤭' )
            computerscore += 1
        elif computer == 'rock' :
            await message.reply( 'you lose   🤭' )
            computerscore += 1
    #await bot.delete_messages(chat_id,message_id,)
    await message.reply( 'next .. choose rock paper or scissor 😌' )

#score to be added soon........
bot.run()
