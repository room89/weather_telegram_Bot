import logging

import telegram
from telegram.ext import Updater, CommandHandler

from secdist import secdist


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
bot_log_file_handler = logging.FileHandler('bot.log')
logger.addHandler(bot_log_file_handler)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def error(bot: telegram.bot.Bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def hello(bot: telegram.bot.Bot, update: telegram.update.Update):
    logger.debug(f'type of args: {type(bot)} {type(update)}')
    logger.debug(f'{type(update.message)}')
    message: telegram.message.Message = update.message
    logger.debug(f'{message.chat}')
    update.message.reply_text('Hello')


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(secdist['bot']['token'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('hello', hello))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
