from flask import Flask
from flask import render_template
from yaml import load, Loader
import gpio
import urllib.request

sf = open('settings.yaml','r')
settings = load(sf, Loader=Loader)

pin = settings['pin']
status_url = settings['url']

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/on')
def on():
	gpio.turn_on(pin)
	return 'on'

@app.route('/off')
def off():
	gpio.turn_off(pin)
	return 'off'

@app.route('/status')
def status():
	return str(gpio.pin_status(pin))

@app.route('/check')
def check():
	stat_url = status_url
	
	response = urllib.request.urlopen(stat_url)
	html = response.read().decode('utf-8')
	
	if html == '1':
		classToday = True
	else:
		classToday = False
	if classToday:
		gpio.turn_on(pin)
	return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
