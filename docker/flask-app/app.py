from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, I am Zeeshan Kanuga.'
    return 'Agar appko istarah ka content dekhna or sikhna hai to aap is repo ko Fork or Star karlo'

@app.route('/health')
def health():
    return 'Server is up and running'
