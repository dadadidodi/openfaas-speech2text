import speech_recognition as sr
import os
import sys
import requests
import wget
from translation import baidu, google, ConnectError, bing, iciba

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    url = req

    if url[-3:] = 'mp4':
        wget.download(url, './tmp.mp4')
        cmd = "ffmpeg -y -i %s -ac 1 -f wav %s"%('tmp.mp4', 'tmp.wav')
        os.system(cmd)
        os.remove('tmp.mp4')
    else:
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
        output = iciba(eng, 'auto', 'zh', {})
    except ConnectError:
        print('Invaild proxy')
    print("Chinese: %s"%output)
    return outp
