from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from . import actions, templates, middlewares
import config

router = Router()

router.message.outer_middleware(middlewares.TestMiddleware())

async def register_views(router: Router):
    command_view_subclasses = templates.CommandView.__subclasses__()
    reply_keyboard_button_view_subclasses = templates.ReplyKeyboardButtonView.__subclasses__()
    inline_keyboard_button_view_subclasses = templates.InlineKeyboardButtonView.__subclasses__()

    command_views = command_view_subclasses[:]
    reply_keyboard_button_views = reply_keyboard_button_view_subclasses[:]
    inline_keyboard_button_views = inline_keyboard_button_view_subclasses[:]

    for command_view_subclass in command_view_subclasses:
        command_views.extend(command_view_subclass.__subclasses__())
    for reply_keyboard_button_view_subclass in reply_keyboard_button_view_subclasses:
        reply_keyboard_button_views.extend(reply_keyboard_button_view_subclass.__subclasses__())
    for inline_keyboard_button_view_subclass in inline_keyboard_button_view_subclasses:
        inline_keyboard_button_views.extend(inline_keyboard_button_view_subclass.__subclasses__())

    for command_view in command_views:
        command_view = command_view(config.bot, config.dp)
        command_view.handle(router)
    for reply_keyboard_button_view in reply_keyboard_button_views:
        reply_keyboard_button_view = reply_keyboard_button_view(config.bot, config.dp)
        reply_keyboard_button_view.handle(router)
    for inline_keyboard_button_view in inline_keyboard_button_views:
        inline_keyboard_button_view = inline_keyboard_button_view(config.bot, config.dp)
        inline_keyboard_button_view.handle(router)


reply_keyboard_buttons = templates.ReplyKeyboardButtonView.__subclasses__()
commands = templates.CommandView.__subclasses__()

reply_button_list = reply_keyboard_buttons[:]
command_list = commands[:]
restricted_text_list = []

for reply_button in reply_keyboard_buttons:
    reply_button_list.extend(reply_button.__subclasses__())
for command in commands:
    command_list.extend(command.__subclasses__())

for reply_button in reply_button_list:
     restricted_text_list.append(reply_button.text)
for command in command_list:
    restricted_text_list.append(f"/{command.text}")

@router.message(lambda message: not message.text in restricted_text_list)
async def echo(message: Message):
    actions.add_message(message)