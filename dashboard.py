from flask import Flask,jsonify,render_template,send_from_directory

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('vendor', path)

@app.route('/',methods=['GET'])
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)

