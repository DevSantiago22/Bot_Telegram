# -*- coding: utf-8 -*-
from config import * # Importamos el token del archivo config
import telebot # Importamos libreria de la API de Telegram
import time as tm
import pathlib as pl
import numpy as np

# Instanciamos nuestro bot
bot = telebot.TeleBot(API_TOKEN)
# Variable diccionario para informacion temporal

# Comando /start para iniciar el bot
@bot.message_handler(commands=['start'])
def cmd_welcome(message):
    msg = "Hola yo soy chatbot ¿En que puedo ayudarle?"
    bot.reply_to(message, msg)

# Comando ayuda
@bot.message_handler(commands=['help'])
def cmd_help(message):
    comando = "/start" "\n"
    comando += "/help" "\n"
    comando += "/Proyector" "\n"
    bot.send_message(message.chat.id, comando, parse_mode='html')

# Comando proyecto
@bot.message_handler(commands=['proyector'])
def cmd_proyector(message):
    bot.send_message(message.chat.id, "<b>Sigue los paso y podras conectar tu proyector</b>", parse_mode='html')
    bot.send_message(message.chat.id, "<b>Cuando estes listo:</b> Envia /listo", parse_mode='html')
    rout = "img/"
    directory = pl.Path(rout)
    photo = []
    for x in directory.iterdir():
        photo.append(np.array(x.name, dtype="object"))
        print(photo)
    cmd_listo(message, photo)

# Comando listo 
@bot.message_handler(commands=['listo'])
def cmd_listo(message, photo):
    for i in photo:
        url = "img/" + photo[i]
        print(url)
        i = i + 1
        image = open(url, 'rb')
        bot.send_photo(message.chat.id, image, "<b>Paso 1:</b>", parse_mode='html')

    

# Respuesta Mensajes sin comandos
@bot.message_handler(content_types=['text'])
def message_texto(message):
    if message.text.startswith('/'):
        bot.send_message(message.chat.id, "Lo sentimos comando no disponible")
    else:
        bot.send_message(message.chat.id, "Prueba texto")

# MAIN ##################################
# Funcion escuchadora del bot
if __name__ == '__main__':
    print('BOT INICIADO.....')
    bot.infinity_polling()
    print('BOT FINALIZADO......')