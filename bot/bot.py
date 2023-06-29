from django.conf import settings
from django.core.management.base import BaseCommand
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler


class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **options):
        app = Client(
            name='mybot',
            api_id=settings.TG_API_ID,
            api_hash=settings.TG_API_HASH,
            bot_token="6207495158:AAFaw81_BaW2bVMae73wuZcjsrGqVO--0ZE"
        )

        @app.on_message(filters.command("start"))
        def start_command(_, message):
            message.reply_text("Hello! I'm your Telegram bot.")

        message_handler = MessageHandler(start_command)
        app.add_handler(message_handler)

        app.run()


command = Command()
command.handle()
