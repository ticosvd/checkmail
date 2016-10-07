from __future__ import  print_function
import time
import config
import checknewemail
import telebot

bot=telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def autochecka(message):
     mes_check=checknewemail.CheckNewEmail(config.username,config.password,config.serverimap)
     bot.send_message(message.chat.id,mes_check)
     print(mes_check+'\n')
#     time.sleep(60)


@bot.message_handler(commands=['check'])

def checka(message):
     mes_check=checknewemail.CheckNewEmail(config.username,config.password,config.serverimap)
     bot.send_message(message.chat.id,mes_check)
     print(mes_check+'\n')


#def repeat_all_messages(message):
#    bot.send_message(message.chat.id,message.text)

if __name__=='__main__':
    bot.polling(none_stop=True)
