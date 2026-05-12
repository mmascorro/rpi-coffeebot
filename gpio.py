from gpiozero import LED

def turn_on(pin):
	od = LED(pin, active_high=False)
	od.on()

def turn_off(pin):
	od = LED(pin, active_high=False)
	od.off()

def pin_status(pin):
	od = LED(pin, active_high=False)
	return od.value