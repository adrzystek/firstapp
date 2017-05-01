# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 22:53:50 2017

@author: Andr
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)