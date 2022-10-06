'''
Created on 04-Sep-2019

@author: bkadambi
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""

from prometheus_client import Counter
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

c_hellos = Counter('count_hellos', 'number of hellos')
c_byes = Counter('count_byes', 'number of byes')

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'Hello, world!'

@app.route("/metrics") # URL for metrics
def metrics():
    res = "c_hellos " + str(c_hellos._value.get()) + '\n'
    res = res + "c_byes " + str(c_byes._value.get())
    return res

@app.route("/hello") 
def hello():
    c_hellos.inc()
    return "hello"

@app.route("/bye")
def goodbye():
    c_byes.inc()
    return "Goodbye"

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
