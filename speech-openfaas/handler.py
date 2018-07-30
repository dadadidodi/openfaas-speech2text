import speech_recognition as sr
import os
import sys
import requests
import wget
import json
from translation import baidu, google, ConnectError, bing, iciba

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    #print(req)
    json_load = json.loads(req)
    url = json_load['url']
    lang = json_load['lang']
   # print(url)
   # print(lang)
   # return
    
    if url[-3:] == 'mp4':
        wget.download(url, './tmp.mp4')
        cmd = "ffmpeg  -loglevel panic -y -i %s -ac 1 -f wav %s"%('tmp.mp4', 'tmp.wav')
        os.system(cmd)
        os.remove('tmp.mp4')
        print("ffmpeg done")
    else:
        wget.download(url, "./tmp.wav")
    r = sr.Recognizer()
    myfile = os.path.join((os.getcwd()), 'tmp.wav')
    print(os.path.isfile(myfile))
    saudio = sr.AudioFile(myfile)
    with saudio as source:
        audio = r.record(source)
    os.remove('tmp.wav')
    eng = r.recognize_google(audio, language=lang)
    print("[%s]: %s"%(lang ,eng))
    try:
        output = iciba(eng, 'auto', 'zh', {})
    except ConnectError:
        print('Invaild proxy')

    print("Chinese: %s"%output)
    #return output
