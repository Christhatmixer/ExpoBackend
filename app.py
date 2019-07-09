from flask import Flask, render_template, request, jsonify

import psycopg2
import psycopg2.extras
import psycopg2.extensions
import os
import sys
import json
import requests




app = Flask(__name__)
app.config['DATABASE_URL'] = os.environ['DATABASE_URL']


@app.route('/getPresenters', methods=['GET', 'POST'])
def getPresenters():
    #data = request.json
    connection = psycopg2.connect(app.config["DATABASE_URL"])
    dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        with dict_cur as cursor:
            sql = "SELECT * FROM presenters;"
            cursor.execute(sql)

            result = cursor.fetchall()
            print(result)

            connection.commit()
    finally:
        connection.close()
    return jsonify(result)


@app.route('/getPresenterProducts', methods=['GET', 'POST'])
def getPresenterProducts():
    connection = psycopg2.connect(app.config["DATABASE_URL"])

    data = request.json
    dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        with dict_cur as cursor:
            sql = "SELECT * FROM products WHERE name = %s"

            cursor.execute(sql, (data["name"],))
            result = cursor.fetchone()

            print(result)

            connection.commit()
    finally:
        connection.close()

    return jsonify(result)