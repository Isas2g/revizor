# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/main')
def main():
    comments = [
        {
            'author': 'Игорь',
            'body': 'отличный ресторан, клёвый я бы сказал'
        },
        {
            'author': 'Ислам',
            'body': 'хороший'
        }
    ]
    return render_template('index.html', title = 'Ревизор', comments = comments)