from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pyrogram import Client
from pyrogram.types import Message
from .bot import Command
from django.conf import settings


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        app = Client(
            name='mybot',
            api_id=settings.TG_API_ID,
            api_hash=settings.TG_API_HASH,
            bot_token="6207495158:AAFaw81_BaW2bVMae73wuZcjsrGqVO--0ZE"
        )

        # Forward the incoming message to the bot
        with app:
            message = Message(
                client=app,
                message_id=request.POST['message_id'],
                chat=app.get_chat(request.POST['chat_id']),
                from_user=app.get_users(request.POST['from_user_id']),
                date=request.POST['date'],
                text=request.POST['text']
            )

            Command.start_command(app, message)

    return HttpResponse()


