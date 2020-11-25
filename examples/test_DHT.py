#!/usr/bin/python3
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32
# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

import Adafruit_DHT
GPIO_PIN = 4
while True:
	h0, t0 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, GPIO_PIN)
	if h0 is not None and t0 is not None:
		print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(t0, h0))
	else:
		print('Failed to get reading. Try again!')
		sys.exit(1)

