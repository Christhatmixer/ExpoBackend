from flask import Flask, render_template, request, jsonify

import psycopg2
import psycopg2.extras
import psycopg2.extensions
import sys
import json
import requests




app = Flask(__name__)
app.config['DATABASE_URL'] = os.environ['DATABASE_URL']