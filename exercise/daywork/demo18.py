import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import tkinter as Tk    

BLOCKLEN   = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)
# specify low frames_per_buffer to reduce latency

# Filter coefficients (second-order IIR)
a_list = []
b_list = []
ORDER = 2   # filter order
states = np.zeros(ORDER)

CONTINUE = True
KEYPRESS = False
INDEX = 0

# To store parameter separately
x_list = []
y_list = []
states_list = []
key = {
    'a': -12,   # A3
    'w': -11,   # A#3
    's': -10,   # B3
    'd': -9,    # C4
    'r': -8,    # C#4
    'f': -7,    # D4
    't': -6,    # D#4
    'g': -5,    # E4
    'h': -4,    # F4
    'u': -3,    # F#4
    'j': -2,    # G4
    'i': -1,    # G#4
    'k': 0,     # A4
    'o': 1,     # A#4
    'l': 2,     # B4
    ';': 3,     # C5
    '[': 4,     # C#5
    '\'': 5,    # D5
    }

def my_function(event):
    global CONTINUE
    global KEYPRESS
    global a_list
    global b_list
    global INDEX
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    KEYPRESS = True

    if event.char in key:
        print('You pressed ' + event.char + ' with ' + str(round(440 * 2 ** (key[event.char] / 12), 1)) + 'Hz')
        INDEX += 1
        # Parameters
        Ta = 2      # Decay time (seconds)
        f1 = 440 * 2 ** (key[event.char] / 12)    # Frequency (Hz)
        r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
        om1 = 2.0 * pi * float(f1)/RATE

        # Filter coefficients (second-order IIR)
        a = [1, -2*r*cos(om1), r**2]
        b = [r*sin(om1)]
        a_list.append(a)
        b_list.append(b)
        x_list.append(np.zeros(BLOCKLEN))
        x_list[INDEX - 1][0] = 10000.0
        y_list.append(0)
        states_list.append(np.zeros(ORDER))
    else:
        print('You pressed ' + event.char)
    

root = Tk.Tk()
root.bind("<Key>", my_function)

print('Press keys for sound.')
print('Press "q" to quit')

while CONTINUE:
    root.update()

    # if KEYPRESS and CONTINUE:
        
    sum_y = np.zeros(BLOCKLEN)
    for i in range(INDEX):
        [y_list[i], states_list[i]] = signal.lfilter(b_list[i], a_list[i], x_list[i], zi = states_list[i])
        x_list[i][0] = 0.0      
        KEYPRESS = False
        sum_y += y_list[i]

    sum_y = np.clip(sum_y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
    binary_data = struct.pack('h' * BLOCKLEN, *sum_y);    # Convert to binary binary data
    stream.write(binary_data, BLOCKLEN)               # Write binary binary data to audio output

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
