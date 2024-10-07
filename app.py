from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
from dotenv import load_dotenv
import os

client = OpenAI()

api_key = os.getenv("OPENAI_API_KEY")

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"
    #return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)