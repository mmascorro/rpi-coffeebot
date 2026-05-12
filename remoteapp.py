from flask import Flask
from flask import render_template
from yaml import load, Loader
from gpiozero import LED
import urllib.request

sf = open('settings.yaml','r')
settings = load(sf, Loader=Loader)

pin = settings['pin']
status_url = settings['url']

app = Flask(__name__)
device = LED(pin, active_high=False)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/on')
def on():
	device.on()
	return 'on'

@app.route('/off')
def off():
	device.off()
	return 'off'

@app.route('/status')
def status():
	return str(device.value)

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
		device.on()
	return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
