import speech_recognition as sr
import os
import wget

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    url = req
    wget.download(url, "./tmp.wav")
    print(req, os.getcwd())
    print(os.listdir())
    r = sr.Recognizer()
    print(os.path.join(os.getcwd(), 'tmp.wav'))
    myfile = os.path.join((os.getcwd()), 'tmp.wav')
    print("should be a file", os.path.isfile(myfile)) 
    saudio = sr.AudioFile(myfile)
    with saudio as source:
        audio = r.record(source)
    print(type(audio))
    return r.recognize_bing(audio)
