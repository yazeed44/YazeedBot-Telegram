from telegram.ext import Updater
import logging
import PrivateConstants
from telegram.ext import CommandHandler

import YoutubeMp3


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm Yazeed's personal bot. Pleased to make your "
                                                                  "acquaintance")


def main():
    updater = Updater(token=PrivateConstants.TELEGRAM_API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    youtube_mp3_handler = CommandHandler('youtubemp3', YoutubeMp3.youtube_mp3)
    dispatcher.add_handler(youtube_mp3_handler)

    updater.start_polling()


if __name__ == "__main__":
    main()
