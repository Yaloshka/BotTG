import requests
import logging


def translation(text):
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to[0]": "ru", "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}
    payload = [{"Text": text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "a47e041d52msh94f55e31ed11f8bp1c4ec5jsnf6d8a4a17af0",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    if not response:
        logging.error(f"Error! Request broke: {response.status_code}, {response.content}")
        return
    data = response.json()
    if not data:
        logging.error(f"Error! query error: {response.status_code}, {response.content}")
        return
    return data[0]["translations"][0]["text"]


def translation2(text):
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to[0]": "en", "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}
    payload = [{"Text": text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "a47e041d52msh94f55e31ed11f8bp1c4ec5jsnf6d8a4a17af0",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    if not response:
        logging.error(f"Error! Request broke: {response.status_code}, {response.content}")
        return
    data = response.json()
    if not data:
        logging.error(f"Error! query error: {response.status_code}, {response.content}")
        return
    return data[0]["translations"][0]["text"]


def detect_text(text):
    url = "https://microsoft-translator-text.p.rapidapi.com/Detect"
    querystring = {"api-version": "3.0"}
    payload = [{"Text": text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "a47e041d52msh94f55e31ed11f8bp1c4ec5jsnf6d8a4a17af0",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    if not response:
        logging.error(f"Error! Request broke: {response.status_code}, {response.content}")
        return
    data = response.json()
    if not data:
        logging.error(f"Error! query error: {response.status_code}, {response.content}")
        return
    return data[0]["language"]
