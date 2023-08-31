from config import * # Importamos el token del archivo config y sus funciones
import telebot # Importamos libreria de la API de Telegram
import time as tm # Importamos para usar sleep en el codigo

# Instanciamos nuestro bot
bot = telebot.TeleBot(API_TOKEN)

# Comando /start para iniciar el bot
@bot.message_handler(commands=['start'])
def cmd_welcome(message):
    msg = "<b>Hola " + message.chat.first_name + " ¿En que puedo ayudarte?</b>"
    bot.reply_to(message, msg, parse_mode="html")
    bot.send_message(message.chat.id, "<b>Para conocer los comandos envia:/help</b>", parse_mode="html")

# Comando ayuda
@bot.message_handler(commands=['help'])
def cmd_help(message):
    comando = "Para iniciar nuestro bot lo puedes hacer con : /start" "\n"
    comando += "Si necesitas revisar los comandos o ayuda Envia: /help" "\n"
    comando += "Para instalar un proyector lo puedes hacer con: /Proyector" "\n"
    bot.send_message(message.chat.id, "<b>"+ comando +"</b>", parse_mode='html')

# Comando proyecto
@bot.message_handler(commands=['proyector'])
def cmd_proyector(message):
    bot.send_message(message.chat.id, "<b>Sigue los paso y podras conectar tu proyector</b>", parse_mode='html')
    bot.send_message(message.chat.id, "<b>Cuando estes listo Envia: </b>/listo", parse_mode='html')

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

# Respuesta Mensajes sin comandos
@bot.message_handler(content_types=['text'])
def message_texto(message):
    if message.text.startswith('/'):
        bot.send_message(message.chat.id, "<b>Lo sentimos, comando no reconocido prueba enviar: /help para cono conocer los comandos</b>")
    else:
        bot.send_message(message.chat.id, "<b>Lo siento aun no puedo entenderte</b>")

# MAIN ##################################
# Funcion escuchadora del bot
if __name__ == '__main__':
    print('BOT INICIADO.....')
    bot.infinity_polling()
    print('BOT FINALIZADO......')