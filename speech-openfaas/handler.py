import speech_recognition as sr
import os
import sys
import requests
import wget
from translation import baidu, google, ConnectError

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    url = req
    wget.download(url, "./tmp.wav")
    r = sr.Recognizer()
    myfile = os.path.join((os.getcwd()), 'tmp.wav')

    saudio = sr.AudioFile("tmp.wav")
    with saudio as source:
        audio = r.record(source)
    os.remove('tmp.wav')
    eng = r.recognize_google(audio)
    print("English: %s"%eng)
    try:
        output = baidu(eng, dst='ru',proxies = {'http': '127.0.0.1:1080'})
    except ConnectError:
        print('Invaild proxy')
    print("French: %s"%output)
    return outp