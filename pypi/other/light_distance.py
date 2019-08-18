from gpiozero import LED, LightSensor, DistanceSensor

leds = [LED(i) for i in [14, 15, 18, 23, 24, 25, 8, 7]]
ldr = LightSensor(4)
ultrasonic = DistanceSensor(echo=17, trigger=27)

try:
    while True:
        for led in leds:
            led.off()
        light = ldr.value
        if light > 0:
            leds[0].on()
        if light > 0.25:
            leds[1].on()
        if light > 0.5:
            leds[2].on()
        if light > 0.75:
            leds[3].on()
        distance = ultrasonic.distance
        if distance > 0:
            leds[4].on()
        if distance > 0.25:
            leds[5].on()
        if distance > 0.5:
            leds[6].on()
        if distance > 0.75:
            leds[7].on()
        print('L:', light, '\tD:', distance)
except KeyboardInterrupt:
    pass
finally:
    for led in leds:
        led.off()
