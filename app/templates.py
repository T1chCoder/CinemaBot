from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import types
import config
from . import actions
from aiogram.fsm.state import StatesGroup, State

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

    async def send_message(self, message):
        await actions.clear_messages(message)
        if self.markup:
            markup = self.markup
        else:
            markup = ReplyKeyboardRemove()
        self.text = self.text.replace("!", r"\!").replace(".", r"\.")
        sent_message = await message.answer(self.text, reply_markup=markup, parse_mode='MarkdownV2')
        actions.add_message(sent_message)
        config.Data.page = self.__class__
        actions.add_message(message)

    async def handle(self, message):
        await self.send_message(message)

class CommandView:
    text = None
    redirect_to = None

    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp

    def handle(self, router: Router):
        @router.message(Command(self.text))
        async def command_view_handler(message: Message, state: FSMContext):
            if self.redirect_to:
                state_pg = False
                state_views = StateView.__subclasses__()

                if self.redirect_to in state_views:
                    state_pg = True

                if state_pg:
                    await self.redirect_to(bot=self.bot, dp=self.dp).handle(message, state)
                else:
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
            async def reply_keyboard_button_view_handler(message: Message, state: FSMContext):
                if self.redirect_to:
                    state_pg = False
                    state_views = StateView.__subclasses__()

                    if self.redirect_to in state_views:
                        state_pg = True

                    if state_pg:
                        await self.redirect_to(bot=self.bot, dp=self.dp).handle(message, state)
                    else:
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
        async def inline_keyboard_button_view_handler(callback_query: CallbackQuery, state: FSMContext):
            if self.redirect_to:
                state_pg = False
                state_views = StateView.__subclasses__()

                if self.redirect_to in state_views:
                    state_pg = True

                if state_pg:
                    await self.redirect_to(bot=self.bot, dp=self.dp).handle(callback_query.message, state)
                else:
                    await self.redirect_to(bot=self.bot, dp=self.dp).handle(callback_query.message)

class StateView(StatesGroup):
    transitions = []
    success_val = None
    success_message = None
    redirect_to = None
    data = {}

    def __init__(self, bot, dp):
        self.bot = bot 
        self.dp = dp

        for transition in self.transitions:
            field = transition["field"]
            if not hasattr(self.__class__, field):
                setattr(self.__class__, field, State(field))

        for id, transition in enumerate(self.transitions):
            function_title = f"handle_transition_{transition['field']}"
            code = None
            
            if len(self.transitions) - 1 == id:
                initial = """pass"""
            else: 
                initial = f"""await state.set_state(self.{self.transitions[id + 1]['field']}) 
            await self.send_message(message, text="{self.transitions[id + 1]['text']}: ")"""

            code = f"""
def {function_title}(self, router: Router):
    @router.message(self.{transition['field']})
    async def transition_{transition['field']}_handler(message: Message, state: FSMContext):
        await state.update_data({transition['field']}=message.text)
        if {len(self.transitions) - 1} == {id}:
            data = await state.get_data()
            self.success_val = self.success(data)
            await state.clear()
            config.Data.echo = True
            self.success_message = message
            await self.redirect_to_page()
        else:
            {initial}
"""

            if code:
                exec(code, globals(), locals())
            
            func = locals()[function_title]
            setattr(self, function_title, types.MethodType(func, self))

    async def redirect_to_page(self):
        if self.success_val:
           await  self.redirect_to(bot=self.bot, dp=self.dp).handle(self.success_message, text=self.success_val["message"], data=self.success_val["items"])

    async def send_message(self, message, text):
        await actions.clear_messages(message)
        text = text.replace("!", r"\!").replace(".", r"\.")
        sent_message = await message.answer(text, parse_mode='MarkdownV2')
        actions.add_message(sent_message)
        config.Data.page = self.__class__
        actions.add_message(message)

    async def handle(self, message, state):
        await state.set_state(getattr(self, self.transitions[0]["field"]))
        await self.send_message(message, text=self.transitions[0]["text"] + ": ")
        config.Data.echo = False

class ListView:
    text = None
    markup = None
    data = []

    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp

    def create_markup(self):
        if self.data:
            inline_buttons = []
            
            for item in self.data: 
                inline_buttons.append([InlineKeyboardButton(text=item["text"], callback_data=item["callback_data"])])
            
            self.markup = InlineKeyboardMarkup(inline_keyboard=inline_buttons)

    async def send_message(self, message):
        await actions.clear_messages(message)
        if self.markup:
            markup = self.markup
        else:
            markup = ReplyKeyboardRemove()
        self.text = self.text.replace("!", r"\!").replace(".", r"\.")
        sent_message = await message.answer(self.text, reply_markup=markup, parse_mode='MarkdownV2')
        actions.add_message(sent_message)
        config.Data.page = self.__class__
        actions.add_message(message)

    async def handle(self, message, text, data):
        self.data = data
        self.text = text
        self.create_markup()
        await self.send_message(message)