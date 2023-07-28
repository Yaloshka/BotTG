from aiogram.utils.helper import Helper, HelperMode, ListItem


class GrammarStates(Helper):
    mode = HelperMode.snake_case
    WAIT_TEXT = ListItem()


class SuggestStates(Helper):
    mode = HelperMode.snake_case
    WAIT_SUGGEST_TEXT = ListItem()


class TranslationStates(Helper):
    mode = HelperMode.snake_case
    WAIT_TRANSLATION_RU_TEXT = ListItem()


class TranslationEnStates(Helper):
    mode = HelperMode.snake_case
    WAIT_TRANSLATION_EN_TEXT = ListItem()


class DetectTextStates(Helper):
    mode = HelperMode.snake_case
    WAIT_DETECT_TEXT_TEXT = ListItem()


class AudioStates(Helper):
    mode = HelperMode.snake_case
    WAIT_AUDIO_TEXT = ListItem()