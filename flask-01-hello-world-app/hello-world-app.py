from flask import Flask 
app = Flask(__name__)
@app.route('/')
def head():
     return "Hello World Seyma"


@app.route('/second')
def second():
     return "this is second Page"


@app.route('/third')
def third():
     return "this is third Page"


@app.route('/fourth/<string:id>')
def fourth(id):
   return f'Id of this page {id}'


if __name__ == '__main__':

     #app.run(debug=True, port=3000)
     app.run(host= '0.0.0.0', port=8080)