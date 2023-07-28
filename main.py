from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import utils
from secret import TELEGRAM_TOKEN
from text_gear import *
from consts import *
from utils import *
from translation import *
from audio import *

logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_f(msg: types.Message):
    logging.debug("Start start_function")
    await bot.send_message(msg.from_user.id, HELLO_MESSAGE)
    logging.debug("Start help_function")
    await bot.send_message(msg.from_user.id, create_help_message())


@dp.message_handler(commands=['help'])
async def help_f(msg: types.Message):
    logging.debug("Start help_function")
    await bot.send_message(msg.from_user.id, create_help_message())


@dp.message_handler(commands=['grammar'])
async def grammar_f(msg: types.Message):
    logging.debug("Start grammar_function")
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(utils.GrammarStates.WAIT_TEXT[0])
    await bot.send_message(msg.from_user.id, GRAMMAR_MESSAGE)


@dp.message_handler(state=GrammarStates.WAIT_TEXT)
async def grammar_wait_text_f(msg: types.Message):
    logging.debug("Start grammar_wait_function")
    uid = msg.from_user.id
    res = grammar_errors(msg.text)
    if res is None:
        logging.error("grammar_wait_text_f data 404")
        await bot.send_message(uid, GRAMMAR_ERROR_MESSAGE)
    else:
        await bot.send_message(uid, create_errors_message(res))
    state = dp.current_state(user=uid)
    await state.reset_state()


@dp.message_handler(commands=['suggest'])
async def suggest_f(msg: types.Message):
    logging.debug("Start suggest_function")
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(utils.SuggestStates.WAIT_SUGGEST_TEXT[0])
    await bot.send_message(msg.from_user.id, SUGGEST_MESSAGE)


@dp.message_handler(state=SuggestStates.WAIT_SUGGEST_TEXT)
async def suggest_wait_text_f(msg: types.Message):
    logging.debug("Start suggest_wait_function")
    uid = msg.from_user.id
    res = suggest_errors(msg.text)
    if res is None:
        logging.error("suggest_wait_text_f data 404")
        await bot.send_message(uid, SUGGEST_ERROR_MESSAGE)
    else:
        await bot.send_message(uid, create_suggest_message(res))
    state = dp.current_state(user=uid)
    await state.reset_state()


@dp.message_handler(commands=['translation_ru'])
async def translation_f(msg: types.Message):
    logging.debug("Start translation_function")
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(utils.TranslationStates.WAIT_TRANSLATION_RU_TEXT[0])
    await bot.send_message(msg.from_user.id, TRANSLATION_RU_MESSAGE)


@dp.message_handler(state=TranslationStates.WAIT_TRANSLATION_RU_TEXT)
async def translation_wait_text_f(msg: types.Message):
    logging.debug("Start translation_wait_function")
    uid = msg.from_user.id
    res = translation(msg.text)
    if res is None:
        logging.error("translation_wait_text_f data 404")
        await bot.send_message(uid, TRANSLATION_RU_ERROR_MESSAGE)
    else:
        await bot.send_message(uid, res)
    state = dp.current_state(user=uid)
    await state.reset_state()


@dp.message_handler(commands=['translation_en'])
async def translation2_f(msg: types.Message):
    logging.debug("Start translation2_function")
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(utils.TranslationEnStates.WAIT_TRANSLATION_EN_TEXT[0])
    await bot.send_message(msg.from_user.id, TRANSLATION_EN_MESSAGE)


@dp.message_handler(state=TranslationEnStates.WAIT_TRANSLATION_EN_TEXT)
async def translation2_wait_text_f(msg: types.Message):
    logging.debug("Start translation2_wait_function")
    uid = msg.from_user.id
    res = translation2(msg.text)
    if res is None:
        logging.error("translation2_wait_text_f data 404")
        await bot.send_message(uid, TRANSLATION_EN_ERROR_MESSAGE)
    else:
        await bot.send_message(uid, res)
    state = dp.current_state(user=uid)
    await state.reset_state()


@dp.message_handler(commands=['detect'])
async def detect_text_f(msg: types.Message):
    logging.debug("Start detect_text_function")
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(utils.DetectTextStates.WAIT_DETECT_TEXT_TEXT[0])
    await bot.send_message(msg.from_user.id, DETECT_TEXT_MESSAGE)


@dp.message_handler(state=DetectTextStates.WAIT_DETECT_TEXT_TEXT)
async def detect_text_wait_text_f(msg: types.Message):
    logging.debug("Start detect_text_wait_function")
    uid = msg.from_user.id
    res = detect_text(msg.text)
    if res is None:
        logging.error("detect_text_wait_text_f data 404")
        await bot.send_message(uid, DETECT_TEXT_ERROR_MESSAGE)
    else:
        await bot.send_message(uid, res)
    state = dp.current_state(user=uid)
    await state.reset_state()


@dp.message_handler(commands=['audio'])
async def audio_f(msg: types.Message):
    logging.debug("Start audio_function")
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(utils.AudioStates.WAIT_AUDIO_TEXT[0])
    await bot.send_message(msg.from_user.id, AUDIO_MESSAGE)


@dp.message_handler(state=AudioStates.WAIT_AUDIO_TEXT)
async def audio_wait_text_f(msg: types.Message):
    logging.debug("Start audio_wait_function")
    uid = msg.from_user.id
    res = audio(msg.text)
    if res is None:
        logging.error("audio_wait_text_f data 404")
        await bot.send_message(uid, AUDIO_ERROR_MESSAGE)
    else:
        await bot.send_message(uid, res)
    state = dp.current_state(user=uid)
    await state.reset_state()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
