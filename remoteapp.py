from flask import Flask
from flask import render_template
import gpio
import urllib2
import yaml

app = Flask(__name__)
sf = open('settings.yaml','r')
settings = yaml.load(sf)

pin = settings['pin']
status_url = settings['url']

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
	return gpio.pin_status(pin)

@app.route('/check')
def check():
	stat_url = status_url
	
	response = urllib2.urlopen(stat_url)
	html = response.read()
	
	if html == "1":
	        classToday = True
	else:
	        classToday = False
	
	if classToday:
	        gpio.turn_on(pin)

	return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
