import speech_recognition as sr
import os
import sys
import requests
import wave

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    # gateway_hostname = os.getenv("gateway_hostname", "gateway")
    # res = requests.get("http://" + gateway_hostname + ":8080/function/youtube-dl", data=req)
    
    # wave.write
    # r = sr.Recognizer()
    #print(os.listdir("/home/app"))
    #myfile = os.path.join((os.getcwd()), 'tmp.wav')
    #print("should be a file", os.path.isfile(myfile), myfile) 

    with open("tmp.wav", "wb") as tmp_file:
        tmp_file.write(req)
    
    saudio = sr.AudioFile("tmp.wav")
    with saudio as source:
        audio = r.record(source)
    print(type(audio))
    return r.recognize_google(audio)



