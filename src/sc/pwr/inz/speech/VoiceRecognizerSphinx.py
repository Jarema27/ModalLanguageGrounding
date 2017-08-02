#   $ pip install --upgrade pip setuptools wheel

#   $ pip install --upgrade pocketsphinx

from pocketsphinx import LiveSpeech
for phrase in LiveSpeech():
    print(phrase)
