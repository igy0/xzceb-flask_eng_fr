from machinetranslation import translator
from machinetranslation.translator import french_to_english,english_to_french
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    output = english_to_french(textToTranslate)
    return ("Translated test to French: " + output)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    output = french_to_english(textToTranslate)
    return ("Translated text to English: " + output)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    
if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=8080)
