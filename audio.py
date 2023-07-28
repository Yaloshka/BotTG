import requests
import logging


def audio(text):
    url = "https://voicerss-text-to-speech.p.rapidapi.com/"
    querystring = {"key": text}
    payload = {
        "src": "Hello, world!",
        "hl": "ру-ру",
        "r": "0",
        "c": "mp3",
        "f": "8khz_8bit_mono"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "a47e041d52msh94f55e31ed11f8bp1c4ec5jsnf6d8a4a17af0",
        "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers, params=querystring)
    if not response:
        logging.error(f"Error! Request broke: {response.status_code}, {response.content}")
        return
    data = response.json()
    if not data:
        logging.error(f"Error! query error: {response.status_code}, {response.content}")
        return
    return data[0]["audio"]