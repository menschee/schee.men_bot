import telebot
from telebot import types

API_TOKEN = '6407889799:AAHKALxy5JoajOLUV-LnK5mPx8SJJXJwcAU'
bot = telebot.TeleBot(API_TOKEN)

# Function to handle inline query results
@bot.inline_handler(lambda query: query.query.lower() == 'toncoin')
def query_text(inline_query):
    try:
        # Image url
        image_url = 'https://github.com/menschee/schee.men_bot/blob/main/qr.png?raw=true'

        # Creating Inline keyboard markup (two buttons with URLs)
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Tonkeeper', url='https://app.tonkeeper.com/transfer/EQCM2ReRAEkCGaAM33ZUx-_vAj0qPgI5TeBQtIp1tjjFe1aa')
        btn2 = types.InlineKeyboardButton('Tonhub', url='https://tonhub.com/transfer/EQCM2ReRAEkCGaAM33ZUx-_vAj0qPgI5TeBQtIp1tjjFe1aa?amount=1000000000')
        keyboard.add(btn1, btn2)

        # Creating text with the image and keyboard
        photo = types.InlineQueryResultPhoto(
            id='1',
            photo_url=image_url,
            reply_markup=keyboard,
            thumbnail_url=image_url,
            caption='To send me Toncoin, use one of the buttons below or copy this address:\n\n`EQCM2ReRAEkCGaAM33ZUx-_vAj0qPgI5TeBQtIp1tjjFe1aa`',
            parse_mode='MarkdownV2'
        )

        # Answering inline query with the created article
        bot.answer_inline_query(inline_query.id, [photo])

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    bot.infinity_polling()
