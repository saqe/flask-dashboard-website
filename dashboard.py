from flask import Flask
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def wellcome():
   return {'success':True},200,{'ContentType':'application/json'}

if __name__ == '__main__':
   app.run()