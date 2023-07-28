HELLO_MESSAGE = f"Приветствую, я Бот, который поможет тебе в обработки любого текста!)"


GRAMMAR_MESSAGE = "Введите текст, который вы хотите проверить на ошибки:"
SUGGEST_MESSAGE = "Введите текст, который вы хотите кректировать:"
TRANSLATION_RU_MESSAGE = "Введите текст, который вы хотите перевести на русский:"
TRANSLATION_EN_MESSAGE = "Введите текст, который вы хотите перевести на английский:"
DETECT_TEXT_MESSAGE = "Введите текст, чтобы узнать язык, на котором он написан:"
AUDIO_MESSAGE = "Введите текст, который вы хотите озвучить:"

GRAMMAR_ERROR_MESSAGE = "При обработке текста произошла неизвестная ошибка."
SUGGEST_ERROR_MESSAGE = "При обработке автокорекции текста произошла неизвестная ошибка."
TRANSLATION_RU_ERROR_MESSAGE = "При переводе текста произошла неизвестная ошибка."
TRANSLATION_EN_ERROR_MESSAGE = "При переводе текста произошла неизвестная ошибка."
DETECT_TEXT_ERROR_MESSAGE = "При определении языка произошла неизвестная ошибка."
AUDIO_ERROR_MESSAGE = "При озвучивании произошла не верная ошибка."

HELP_DICT = {
    "start": "Выводит приветственное сообщение.",
    "help": "Выводит это сообщение.",
    "grammar": "Запускает навык обработки текста на ошибки.",
    "suggest": "Запускает навык автокоррекции текста.",
    "translation_ru": "Запускает навык перевод языка на русский.",
    "translation_en": "Запускает навык перевод языка на английский.",
    "detect": "Запускает навык определение языка.",
    "audio": "Запускается навык озвучивание текста."
}


def create_help_message():
    text = "Вот, что я могу:\n"
    for command in HELP_DICT:
        text += f"/{command} - {HELP_DICT[command]}\n"
    return text


def create_errors_message(data):
    if not data:
        return "Ошибки не обнаружены!"
    ans = "Обнаружены ошибки:\n"
    for i, error in enumerate(data["errors"], 1):
        variants = ", ".join(error['better'])
        ans += f"{i}) {error['bad']}\n Варианты исправления:\n {variants}.\n"
    return ans


def create_suggest_message(data):
    if not data:
        return "Что-то пошло не так:("
    ans = data["corrected"]
    if 'suggestions' in data and data['suggestions']:
        ans += '\nВозможны также следующие врианты исправления:\n'
    for i, error in enumerate(data["suggestions"], 1):
        variants = ", ".join(error['next_word'])
        ans += f"{i}) {variants}.\n"
    return ans








