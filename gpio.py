from gpiozero import DigitalOutputDevice

def turn_on(pin):
	od = DigitalOutputDevice(pin)
	od.off()

def turn_off(pin):
	od = DigitalOutputDevice(pin)
	od.on()

def pin_status(pin):
	od = DigitalOutputDevice(pin)
	return od.value