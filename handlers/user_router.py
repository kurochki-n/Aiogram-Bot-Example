from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext

from . import localization as loc, keyboards as kb
from .states import States
from middlewares.check_sub import CheckSubscription


router = Router()
router.message.middleware.register(CheckSubscription())
router.callback_query.middleware.register(CheckSubscription())


@router.message(Command("command"))
async def command_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text=loc.start_message(), reply_markup=kb.reply_keyboard())
    await state.clear()

    
@router.message(F.text == "text")
async def text_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text=loc.start_message(), reply_markup=kb.inline_keyboard())
    await state.set_state(States.my_state)


@router.callback_query(F.data == "data")
async def calldack_query_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_reply_markup(text=loc.start_message(), reply_markup=kb.inline_keyboard())
    await state.clear()
    

@router.message(StateFilter(States.my_state))
async def my_state_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text=loc.start_message(), reply_markup=kb.inline_webapp_keyboard())
    await state.clear()

    






