from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import config
from . import actions


class TemplateView:
    text = None
    page = None
    command = None
    message = None
    markup = None
    header = None

    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp
        self.create_markup()

    def create_markup(self):
        views = TemplateView.__subclasses__()
        reply_keyboard_buttons = ReplyKeyboardButtonView.__subclasses__()
        inline_keyboard_buttons = InlineKeyboardButtonView.__subclasses__()

        view_list = views[:]
        reply_button_list = reply_keyboard_buttons[:]
        inline_button_list = inline_keyboard_buttons[:]

        for view in views:
            view_list.extend(view.__subclasses__())
        for reply_button in reply_keyboard_buttons:
            reply_button_list.extend(reply_button.__subclasses__())
        for inline_button in inline_keyboard_buttons:
            inline_button_list.extend(inline_button.__subclasses__())

        for view in view_list:
            reply_keyboard_buttons = []
            inline_keyboard_buttons = []

            for reply_button in reply_button_list:
                if view in reply_button.pages:
                    reply_keyboard_buttons.append(
                        [KeyboardButton(text=reply_button.text)]
                    )
            for inline_button in inline_button_list:
                if view in inline_button.pages:
                    inline_keyboard_buttons.append(
                        [
                            InlineKeyboardButton(
                                text=inline_button.text,
                                callback_data=inline_button.callback_data,
                            )
                        ]
                    )

            reply_keyboard_markup = ReplyKeyboardMarkup(
                resize_keyboard=True, keyboard=reply_keyboard_buttons
            )
            inline_keyboard_markup = InlineKeyboardMarkup(
                inline_keyboard=inline_keyboard_buttons
            )

            if reply_keyboard_markup.keyboard:
                view.markup = reply_keyboard_markup
            elif inline_keyboard_markup.inline_keyboard:
                view.markup = inline_keyboard_markup

    async def send(self, message):
        await actions.clear_messages()
        if self.markup:
            markup = self.markup
        else:
            markup = ReplyKeyboardRemove()
        sent_message = await message.answer(self.text, reply_markup=markup)
        actions.add_message(sent_message)
        config.Data.page = self.__class__
        actions.add_message(message)

    async def handle(self, message):
        await self.send(message)


class CommandView:
    text = None
    redirect_to = None

    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp

    def handle(self, router: Router):
        @router.message(Command(self.text))
        async def command_view_handler(message: Message):
            if self.redirect_to:
                await self.redirect_to(bot=self.bot, dp=self.dp).handle(message)


class ReplyKeyboardButtonView:
    text = None
    pages = []
    redirect_to = None

    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp

    def handle(self, router: Router):
        if config.Data.page in self.pages:

            @router.message(F.text == self.text)
            async def reply_keyboard_button_view_handler(message: Message):
                if self.redirect_to:
                    await self.redirect_to(bot=self.bot, dp=self.dp).handle(message)


class InlineKeyboardButtonView:
    text = None
    pages = []
    redirect_to = None
    callback_data = None

    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp
        
    def handle(self, router: Router):
        @router.callback_query(lambda c: c.data == self.callback_data)
        async def inline_keyboard_button_view_handler(callback_query: CallbackQuery):
            if self.redirect_to:
                await self.redirect_to(bot=self.bot, dp=self.dp).handle(
                    callback_query.message
                )
