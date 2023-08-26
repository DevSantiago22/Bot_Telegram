# -*- coding: utf-8 -*-
from config import * # Importamos el token del archivo config
import telebot # Importamos libreria de la API de Telegram

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
    comando += "/foto" "\n"
    bot.send_message(message.chat.id, comando, parse_mode='html')

# Comando foto
@bot.message_handler(commands=['foto'])
def cmd_foto(message):
    foto = open('img/prueba.jpg', 'rb')
    bot.send_photo(message.chat.id, foto, "Prueba 1")

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