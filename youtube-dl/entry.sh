#!/bin/sh

url=""
if [ ! -z "$1" ] ; then
  url=$1
else
  url=$(cat /dev/stdin)
fi

trimmedURL=$(echo "$url" | tr -d '\n')

youtube-dl $trimmedURL --extract-audio --audio-format "wav" --no-warnings --quiet -o "tmp.wav"
curl -X POST "http://127.0.0.1:8080/function/speech-openfaas"  --data-binary  @tmp.wav
