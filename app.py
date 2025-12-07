from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World - Owolabi Adeyinka Oluwatosin, A Final year chemical Engineering Student of OAU and Cloud Sec Dev(view)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
