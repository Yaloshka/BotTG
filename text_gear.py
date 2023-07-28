import requests
import logging
from secret import TEXT_GEAR_API_KEY

SERVER = "https://api.textgears.com/"
DEFAULT_PARAMS = {
    "language": "ru-RU",
    "key": TEXT_GEAR_API_KEY
}


def grammar_errors(text):
    logging.debug(f"Start grammar_errors with text: {text}")
    url = SERVER + "grammar"
    params = DEFAULT_PARAMS.copy()
    params["text"] = text
    response = requests.get(url, params=params)
    logging.debug(f"url: {response.url}, result: {response.text}")
    if not response:
        logging.error(f"Error! Request broke: {response.status_code}, {response.content}")
        return
    data = response.json()
    if not data["status"]:
        logging.error(f"Error! query error: {response.status_code}, {response.content}")
        return
    return data["response"]


def suggest_errors(text):
    logging.debug(f"Start suggest_errors with text: {text}")
    url = SERVER + "suggest"
    params = DEFAULT_PARAMS.copy()
    params["text"] = text
    response = requests.get(url, params=params)
    logging.debug(f"url: {response.url}, result: {response.text}")
    if not response:
        logging.error(f"Error! Request broke: {response.status_code}, {response.content}")
        return
    data = response.json()
    if not data["status"]:
        logging.error(f"Error! query error: {response.status_code}, {response.content}")
        return
    return data["response"]







