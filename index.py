from flask import Flask,jsonify,render_template,send_from_directory
from flask_compress import Compress
import os
from python.homeScreen import getDashboardData
from python.profileScreen import profileDashboard
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
Compress(app)

# Static files
@app.route('/js/<path:path>')
def send_js(path):      return send_from_directory('js'    , path)
@app.route('/img/<path:path>')
def send_img(path):     return send_from_directory('img'   , path)
@app.route('/css/<path:path>')
def send_css(path):     return send_from_directory('css'   , path)
@app.route('/vendor/<path:path>')
def send_vendor(path):  return send_from_directory('vendor', path)

# Routes
@app.route('/',methods=['GET'])
def index():
   data=getDashboardData(os.getenv('MONGO_TOKEN'))
   return render_template('index.html',data=data)

@app.route('/profile/<int:profile_id>',methods=['GET'])
def profile(profile_id):
   data=profileDashboard(os.getenv('MONGO_TOKEN'),profile_id)
   return render_template('profile.html',data=data)
   
if __name__ == '__main__':
   app.run(debug=True)

