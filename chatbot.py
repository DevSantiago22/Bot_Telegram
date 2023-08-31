# -*- coding: utf-8 -*-
from config import * # Importamos el token del archivo config
import telebot # Importamos libreria de la API de Telegram
import time as tm # Importamos para usar sleep en el codigo
import os # Importamos para poder listar y recorrer las imagenes

# Instanciamos nuestro bot
bot = telebot.TeleBot(API_TOKEN)

# Comando /start para iniciar el bot
@bot.message_handler(commands=['start'])
def cmd_welcome(message):
    msg = "Hola " + message.chat.first_name + " ¿En que puedo ayudarte?"
    bot.reply_to(message, msg)
    bot.send_message(message.chat.id, "<b>Envia el comando /help para consultar los comandos</b>", parse_mode="html")

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

# Comando pdf
@bot.message_handler(commands=['pdf'])
def cmd_pdf(message):
    pdf = open('pdf/Conexion proyector.pdf', 'rb')
    bot.send_document(message.chat.id, pdf)

# Comando listo 
@bot.message_handler(commands=['listo'])
def cmd_listo(message):
    image = rout_photo()
    response = list_response()
    x = 0
    for i in image:
        respuesta = response[x]
        foto = "img/" + i
        abrir = open(foto, 'rb')
        bot.send_photo(message.chat.id, abrir, "<b>"+respuesta+"</b>", parse_mode="html")
        x = x + 1
        tm.sleep(6)
    bot.send_message(message.chat.id, "<b>Fue un placer ayudarte, puedes consultar el pdf con /pdf</b>", parse_mode="html")

# Funcion que lista y devuelve las respuestas del bot
def list_response():
    with open('otros/respuestas.txt') as file_object:
        object = file_object.readlines() 
    return object

# Funcion que se encarga de listar las fotos a enviar
def rout_photo():
    directorio = "img/"
    contenido = os.listdir(directorio)
    img = []
    for ficheros in contenido:
        if os.path.isfile(os.path.join(directorio, ficheros)) and ficheros.endswith('.jpg'):
            img.append(ficheros)
    return img

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