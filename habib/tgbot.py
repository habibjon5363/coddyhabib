# pip install pyTelegramBotAPI 
 
 
# имя бота coddyhabib 
 
# никнейм бота coddyhabibBot 
 
# ссылка бота https://t.me/coddyhabibBot 
#  TOKEN = 5999737407:AAHroigNIAHfenI2ipMYOLMiylY7nm7VEl4 
 
import telebot 
from telebot import types 
 
# импортируем из библиотеки time метод sleep 
from time import sleep 
import random 
import webbrowser
 
TOKEN = "5999737407:AAHroigNIAHfenI2ipMYOLMiylY7nm7VEl4" 
# если добавляем из файла конфига, то вот так 
# moySuperBot = telebot.TeleBot(config.TOKEN) 
 
moySuperBot = telebot.TeleBot(TOKEN) 
 
 
# команда старт отправлена боту 
@moySuperBot.message_handler(commands=["start"]) 
def obrabotchikKomandiStart(message): 
    sti = open("hello.webp", "rb") 
    moySuperBot.send_sticker(message.chat.id, sti) 
 
    # создаем клавиатуру с двумя кнопками 
    raskladka1 = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    levayaKnopka = types.KeyboardButton("Ну как дела?") 
    pravayaKnopka = types.KeyboardButton("кинь кубик") 
    raskladka1.add(levayaKnopka, pravayaKnopka) 
 
    # создаем видимость что бот печатает 
    moySuperBot.send_chat_action(message.chat.id, "typing") 
    sleep(2) 
    moySuperBot.send_message( 
        message.chat.id, 
        "Привет, {0.first_name}. \n Это <b>{1.first_name}</b> бот. Меня создал Сергей".format( 
            message.from_user, moySuperBot.get_me() 
        ), 
        parse_mode="html", 
        reply_markup=raskladka1, 
    ) 

@moySuperBot.message_handler(commands=["show"])
def komanashow(message):
    moySuperBot.send_message(message.chat.id, message.from_user.is_bot)

@moySuperBot.message_handler(commands=["myid"])
def moyid(message):
    moySuperBot.send_message(message.chat.id, message.from_user.id)

@moySuperBot.message_handler(commands=['site'])
def site(message):
    sleep(0.5)
    moySuperBot.send_chat_action(message.chat.id, "typing")
    moySuperBot.send_message(message.chat.id, 'в этой школе я обучался')
    sleep(1)
    webbrowser.open('https://coddyschool.com/')
 
 
@moySuperBot.message_handler(content_types=["text"]) 
def lalala(message): 
    if message.chat.type == "private": 
        if message.text == "hi": 
            moySuperBot.send_message(message.chat.id, "Salom") 
        elif message.text == "poka": 
            moySuperBot.send_message(message.chat.id, "i tebe poka") 
        else: 
            otvet1 = "даже не знаю что ответить .." 
            otvet2 = "поговорим об этом позже" 
            otvet3 = "и что это значит?" 
            otvet4 = "мне нечего сказать" 
            otvet5 = "пока еще я не на столько умен" 
            nechegoSkazat = [otvet1, otvet2, otvet3, otvet4, otvet5] 
            moySuperBot.send_chat_action(message.chat.id, "typing") 
            sleep(1) 
            moySuperBot.send_message(message.chat.id, random.choice(nechegoSkazat)) 
            # отправка такого же текста как написал клиент 
            # moySuperBot.send_message(message.chat.id, message.text) 
 
 
# запуск бота 
moySuperBot.polling(none_stop=True)