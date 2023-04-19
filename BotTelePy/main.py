#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.


from getResultWeb import Game82VN
from callAttackResult import CallBookmaker
from docAllMessage import AllBody
from saveFileData import SaveDataWinLose

import logging, time, requests
from collections import defaultdict
from typing import DefaultDict, Optional, Set
from telegram import __version__ as TG_VER


try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ExtBot,
    TypeHandler,
    MessageHandler,
    filters
   
)


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


class ChatData:

    def __init__(self) -> None:
        self.clicks_per_message: DefaultDict[int, int] = defaultdict(int)


# The [ExtBot, dict, ChatData, dict] is for type checkers like mypy
class CustomContext(CallbackContext[ExtBot, dict, ChatData, dict]):
    def __init__(self, application: Application, chat_id: int = None, user_id: int = None):
        super().__init__(application=application, chat_id=chat_id, user_id=user_id)
        self._message_id: Optional[int] = None

    @property
    def bot_user_ids(self) -> Set[int]:
        """Custom shortcut to access a value stored in the bot_data dict"""
        return self.bot_data.setdefault("user_ids", set())

    @property
    def message_clicks(self) -> Optional[int]:
        """Access the number of clicks for the message this context object was built for."""
        if self._message_id:
            return self.chat_data.clicks_per_message[self._message_id]
        return None

    @message_clicks.setter
    def message_clicks(self, value: int) -> None:
        """Allow to change the count"""
        if not self._message_id:
            raise RuntimeError("There is no message associated with this context object.")
        self.chat_data.clicks_per_message[self._message_id] = value

    @classmethod
    def from_update(cls, update: object, application: "Application") -> "CustomContext":
        context = super().from_update(update, application)
        if context.chat_data and isinstance(update, Update) and update.effective_message:
            # pylint: disable=protected-access
            context._message_id = update.effective_message.message_id
        return context


async def start(update: Update, context: CustomContext) -> None:
    await update.message.reply_html(
        "This button was clicked <i>0</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="button")
        ),
    )


async def count_click(update: Update, context: CustomContext) -> None:
    context.message_clicks += 1
    await update.callback_query.answer()
    await update.effective_message.edit_text(
        f"This button was clicked <i>{context.message_clicks}</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="button")
        ),
        parse_mode=ParseMode.HTML,
    )


async def print_users(update: Update, context: CustomContext) -> None:
    await update.message.reply_text(
        "The following user IDs have used this bot: "
        f'{", ".join(map(str, context.bot_user_ids))}'
    )


async def track_users(update: Update, context: CustomContext) -> None:
    if update.effective_user:
        context.bot_user_ids.add(update.effective_user.id)


def sendToChannel(update: Update, context: CustomContext, idChat: int, message: str) -> None:
    context.bot.send_message(idChat, text=message)


async def run_bot(update: Update, context: CustomContext) -> None:
    print("doing something...")


async def get_id_chat(update: Update, context: CustomContext):
    idChat = context._chat_id
    await context.bot.send_message(idChat, text=f"ID Chat: {idChat}")
 

async def handle_text(update: Update, context: CustomContext):
    text = update
    messageText = text.channel_post.text
    idChat = context._chat_id
    response_text = f"ID Chat: {idChat}"
    print(response_text)
    

async def error(update: Update, context: CustomContext):
    logging.error(f'[!!!]Error: {context.error}')
  

def main() -> None:
    """Run the bot."""
    context_types = ContextTypes(context=CustomContext, chat_data=ChatData)
    application = Application.builder().token(open("Token.txt","r").read()).context_types(context_types).build()
    application.add_handler(TypeHandler(Update, track_users), group=-1)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("runbot", run_bot))
    application.add_handler(CommandHandler("idchat", get_id_chat))
    application.add_handler(CallbackQueryHandler(count_click))
    application.add_handler(CommandHandler("print_users", print_users))
    application.add_handler(MessageHandler(filters.ALL, handle_text))
    application.add_error_handler(error)
    application.run_polling(1.8)
    application.idle()


if __name__ == "__main__":
    main()

    