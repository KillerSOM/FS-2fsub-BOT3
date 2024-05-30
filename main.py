#from bot import Bot

#Bot().run()
from bot import Bot

if __name__ == "__main__":
    bot = Bot()

    # Register force sub command handlers
    from force_sub import add_forcesub, delete_all_forcesub, get_forcesub
    bot.add_handler(add_forcesub)
    bot.add_handler(delete_all_forcesub)
    bot.add_handler(get_forcesub)

    bot.run()

