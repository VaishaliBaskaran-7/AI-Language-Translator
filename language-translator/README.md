# AI Language Translation Tool

## Overview

AI Language Translation Tool is a web-based application that translates text between multiple languages using Meta's NLLB-200 Distilled 600M multilingual transformer model. The application provides a simple user interface where users can enter text, select source and target languages, and receive accurate translations in real time.

Unlike traditional translation applications that rely on external translation APIs, this project performs translation locally using a pre-trained neural machine translation model from Hugging Face.

---

## Features

* Translate text between multiple languages
* Select source language
* Select target language
* Real-time translation through Flask backend
* Transformer-based Neural Machine Translation (NMT)
* User-friendly web interface
* No external translation API required after model download

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI / NLP

* Hugging Face Transformers
* PyTorch
* NLLB-200 Distilled 600M Model

---

## Project Structure

language-translator/

├── app.py

├── templates/

│ └── index.html

├── static/

│ ├── style.css

│ └── script.js

├── services/

│ ├── translator.py

│ └── languages.py

├── requirements.txt

└── README.md

---

## How It Works

1. User enters text.
2. User selects source language.
3. User selects target language.
4. Frontend sends the request to Flask backend.
5. Flask processes the request.
6. NLLB-200 model performs translation.
7. Translated text is returned to the frontend.
8. Translation is displayed to the user.

---

## AI Model

This project uses Meta's NLLB-200 Distilled 600M model, a multilingual transformer-based Neural Machine Translation (NMT) model capable of translating between hundreds of languages.

The model is loaded locally using the Hugging Face Transformers library and PyTorch.

---

## Installation

1. Clone the repository.

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment.

Windows:

venv\Scripts\activate

4. Install dependencies:

pip install -r requirements.txt

5. Run the application:

python app.py

6. Open the browser:

http://127.0.0.1:5000

---

## Future Enhancements

* Automatic language detection
* Translation history
* Text-to-speech functionality
* Copy translation button
* Dark mode
* Additional language support
* Translation confidence indicators

---

## Learning Outcomes

This project demonstrates:

* Flask web development
* Frontend and backend integration
* REST API communication
* Transformer-based NLP models
* Hugging Face ecosystem
* Neural Machine Translation (NMT)
* PyTorch model inference

---

## Author

Developed as part of an Artificial Intelligence Internship Project.
