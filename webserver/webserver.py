from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to your Raspberry PI Web Server !</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a basic web server running on Raspberry PI 3B+</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)