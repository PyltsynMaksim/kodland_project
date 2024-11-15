import telebot
from telebot import types

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

# Установим начальное сообщение с кнопками
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ['Раскид', 'Позиции', 'Спрей', 'Тайминги']
keyboard.add(*buttons)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Спрей':
        # Укажите путь к вашему GIF-файлу
        gif_path = 'E:\m10\Include\content\spray.gif'  # Путь
        with open(gif_path, 'rb') as gif:
            bot.send_animation(message.chat.id, gif)
            ###
    elif message.text == 'Тайминги':
        # Создаем меню для 'Тайминги'
        timing_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        timing_buttons = ['Dust2', 'Mirage', 'Назад']  # Добавляем кнопку 'Назад'
        timing_keyboard.add(*timing_buttons)
        bot.send_message(message.chat.id, "Выберите карту для таймингов:", reply_markup=timing_keyboard)
    elif message.text == 'Dust2':
        # Укажите путь для изображения Dust2 или таймингов для Dust2
        image_path = 'E:\m10\Include\content\Dust2TimingCounterTerrorist.jpg'  #путь к изображению
        image_path2 = 'content/E:\m10\Include\content\Dust2TimingTerrorist.jpg'  #путь к изображению
        with open(image_path, image_path2, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'Mirage':
        # Укажите путь для изображения Mirage или таймингов для Mirage
        image_path = 'E:\m10\Include\content\MirageTimingCT.png'  #путь к изображению
        image_path2 = 'E:\m10\Include\content\MirageTimingTerrorist.jpg'  #путь к изображению
        with open(image_path, image_path2, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)
        ###
    elif message.text == 'Позиции':
        # Создаем новое меню для 'Позиции'
        position_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        position_buttons = ['Dust2', 'Mirage', 'Назад']  # Добавляем кнопку 'Назад'
        position_keyboard.add(*position_buttons)
        bot.send_message(message.chat.id, "Выберите карту:", reply_markup=position_keyboard)
    elif message.text == 'Dust2':
        # Укажите путь к изображению для Dust2
        image_path = 'E:\m10\Include\content\dust2.jpg'  #путь к изображению
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'Mirage':
        # Укажите путь к изображению для Mirage
        image_path = 'E:\m10\Include\content\mirage.jpg'  #путь к изображению
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Нажмите одну из кнопок!", reply_markup=keyboard)

    
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
