from gpiozero import LEDBoard, LEDBarGraph
from datetime import datetime
from threading import Thread
from time import sleep

coms = LEDBoard(14, 15, 18, 2)
segs = LEDBoard(16, 21, 19, 6, 5, 20, 26, 13)
bargraph = LEDBarGraph(3, 4, 17, 27, 22, 10, 9, 11, 7, 12)
chars_map = {
    ' ': '00000000',
    '0': '11111100',
    '1': '01100000',
    '2': '11011010',
    '3': '11110010',
    '4': '01100110',
    '5': '10110110',
    '6': '10111110',
    '7': '11100000',
    '8': '11111110',
    '9': '11110110',
    'A': '11101110',
    'B': '11111110',
    'C': '10011100',
    'D': '11111100',
    'E': '10011110',
    'F': '10001110',
    'G': '10111100',
    'H': '01101110',
    'I': '01100000',
    'J': '01111000',
    'K': '01101110',
    'L': '00011100',
    'M': '10101010',
    'N': '00101010',
    'O': '11111100',
    'P': '11001110',
    'Q': '11100110',
    'R': '11101110',
    'S': '10110110',
    'T': '10001100',
    'U': '01111100',
    'V': '01001110',
    'W': '01111110',
    'X': '01001010',
    'Y': '01110110',
    'Z': '11011010',
    'a': '11111010',
    'b': '00111110',
    'c': '00011010',
    'd': '01111010',
    'e': '11011110',
    'f': '10001110',
    'g': '11110110',
    'h': '00101110',
    'i': '00100000',
    'j': '01110000',
    'k': '00101110',
    'l': '00001100',
    'm': '10101010',
    'n': '00101010',
    'o': '00111010',
    'p': '11001110',
    'q': '11100110',
    'r': '00001010',
    's': '10110110',
    't': '00011110',
    'u': '00111000',
    'v': '01000110',
    'w': '01010110',
    'x': '01001010',
    'y': '01100110',
    'z': '11011010',
}
chars = [' ', ' ', ' ', ' ']
dots = [False, False, False, False]
running = True


def render():
    dot = segs.leds[7]
    while running:
        for i in range(4):
            char = chars[i]
            bits = chars_map[char]
            for j in range(7):
                led = segs.leds[j]
                bit = bits[j]
                if bit == '1':
                    led.off()
                elif bit == '0':
                    led.on()
            if dots[i]:
                dot.off()
            else:
                dot.on()
            com = coms.leds[i]
            com.on()
            sleep(.0005)
            com.off()


def display_seconds():
    while running:
        now = datetime.now()
        bits = bin(now.second)
        bits = bits[2:]
        bits = bits.zfill(10)
        for i in range(10):
            bit = bits[i]
            led = bargraph.leds[i]
            if bit == '1':
                led.on()
            elif bit == '0':
                led.off()
        sleep(.1)


def show_text(txt):
    global chars
    queue = '    ' + txt + '    '
    while len(queue) != 4:
        buff = queue[0:4]
        chars = list(buff)
        queue = queue[1:]
        sleep(.3)


def update():
    global chars
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    if second == 30:
        day = now.strftime('%A')
        show_text(day)
    else:
        chars = [
            str(hour / 10),
            str(hour % 10),
            str(minute / 10),
            str(minute % 10)
        ]
        dots[1] = (second % 2 == 0)
        sleep(.1)


render_thread = Thread(target=render)
display_seconds_thread = Thread(target=display_seconds)

try:
    render_thread.start()
    display_seconds_thread.start()
    while running:
        update()
except (KeyboardInterrupt, SystemExit):
    pass
finally:
    running = False
    render_thread.join()
    display_seconds_thread.join()
    coms.close()
    segs.close()
    bargraph.close()
