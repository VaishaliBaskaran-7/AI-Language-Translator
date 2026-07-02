from flask import Flask, render_template, request, jsonify
from services.translator import translate_text
from services.languages import LANGUAGE_CODES

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data["text"]
    source_lang = data["source_lang"]
    target_lang = data["target_lang"]
    source_code = LANGUAGE_CODES[source_lang]
    target_code = LANGUAGE_CODES[target_lang]

    translated_text = translate_text(
        text,
        source_code,
        target_code
    )
    return jsonify({
        "translated_text": translated_text
    })

if __name__ == "__main__":
    app.run(debug=True)