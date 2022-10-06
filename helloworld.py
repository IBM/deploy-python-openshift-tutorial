from prometheus_client import Counter
from flask import Flask  # From module flask import class Flask
from flask import Response 
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

c_hellos = Counter('count_hellos', 'number of hellos')
c_byes = Counter('count_byes', 'number of byes')

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    return Response('Hello, world 2!', mimetype="text/plain")

@app.route("/metrics") # URL for metrics
def metrics():
    res = "#HELP c_hellos count of calls to /hello\n#TYPE c_hellos counter\n"
    res = res + "c_hellos " + str(c_hellos._value.get()) + '\n'
    res = res + "#HELP c_byes count of calls to /bye\n#TYPE c_byes counter\n"
    res = res + "c_byes " + str(c_byes._value.get())

    return Response(res, mimetype="text/plain")

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
