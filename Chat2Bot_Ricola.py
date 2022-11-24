import telebot
import cyrtranslit


words = ['блядь',
         'на пох',
         'хуи',
         'на хуй',
         'на хуи',
         'блят',
         'блеат',
         'бля',
         'взьеб',
         'вьеб',
         'вжопу',
         'высрал',
         'вжопе',
         'гавню',
         'гнида',
         'засран',
         'дибил',
'бляд',
'бля',
'взьеб',
'вьеб',
'вжопу',
'высер',
'высрал',
'высран',
'выродк',
'выродок',
'вжопе',
'гавню',
'говню',
'гомик',
'гомосек',
'гандон',
'гондон',
'гнида',
'залуп',
'дибил',
'мудил',
'нахер',
'обосал',
'педик',
'пидар',
'пздц',
'пох',
'суки',
'ублюдок',
'ублюдки'
  ]
from nltk.tokenize import word_tokenize

bot = telebot.TeleBot('5121709294:AAHvvFfhQJVtCCMAldaBuZSeUFIyyUQ-LVA')

@bot.message_handler(commands=['privet'])
def privet(message):
    mess = f'Privet, <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    x=message.text.lower()
    a = cyrtranslit.to_cyrillic(x, "ru")

    text_tokens = word_tokenize(a)
    tokens_without_sw = [" ".join([word for word in text_tokens if not word in words])]
    bot.send_message(message.chat.id, tokens_without_sw, parse_mode='html')

    # print(a)

bot.polling(none_stop=True)


