import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import config
bot = telebot.TeleBot(config.token)
player1 = 'Clown'
player2 = 'Witcher'
def inline_buttons_stone():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Turn left', callback_data='Stone left')
    btn2 = InlineKeyboardButton('Turn right', callback_data='Stone right')
    markup.add(btn1, btn2)
    return markup
def inline_buttons_sage():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Enter a dungeon', callback_data='Dungeon')
    btn2 = InlineKeyboardButton('Go to the forest', callback_data='Forest')
    markup.add(btn1, btn2)
    return markup
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text:
        bot.send_message(message.chat.id, f"{player1} and {player2} were walking through the forest and met a stone. There was a message on it:", reply_markup=inline_buttons_stone())
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'Stone left':
        bot.send_message(call.from_user.id, 'Congratulation, U died')
    if call.data == 'Stone right':
        bot.send_message(call.from_user.id, 'U reached Sage')
        bot.send_photo(call.from_user.id, 'https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8a627ec10b57f4f2/5eb7cdc16509f3370a5a93b7/V_AGENTS_587x900_sage.png')
        bot.send_message(call.from_user.id, f'{player1} and {player2} met a Sage and he told them:', reply_markup=inline_buttons_sage())
    if call.data == 'Dungeon':
        bot.send_message(call.from_user.id, 'U was killed by a Skeleton')
    if call.data == 'Forest':
        bot.send_message(call.from_user.id, 'U left the cursed forest and WON THIS GAME!!!')
        bot.send_photo(call.from_user.id, 'https://static.vecteezy.com/system/resources/previews/010/976/287/original/golden-cup-3d-red-ribbon-winner-1st-place-minimal-gold-winners-stars-on-podium-champion-award-ceremony-concept-in-cartoon-style-trophy-render-isolated-on-white-background-game-or-education-free-vector.jpg')
        bot.send_audio(call.from_user.id, open('LOVV66, SEEMEE - Новая эра.mp3', 'rb'))
bot.polling(none_stop=True)
