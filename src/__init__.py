import os
from flask import Flask, jsonify, render_template, request, redirect, url_for
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("key")

from src import routes