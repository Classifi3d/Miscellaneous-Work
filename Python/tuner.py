import pyaudio
from numpy import zeros, linespace, short, fromstring, hstack, transpose, log2, log, log10
from scipy import fft,signal
from time import sleep
from scipy.signal import hamming, convole
from gpiozero import RGBLED, LED 
import sys
import struct
import math
# Volume Sensitivy, 0.05 Extremley sensitive,
#                   0.1 Probably ideal volume
#                    1 poorly senstive will only go off for realtively loud sounds
#I used sestivity 5 as I has a very good mic
SENSITIVITY = 4
BANDWITDH = 1

frequencyoutput=True
Note_E=5
Note_A=0
Note_D=7
Note_G=2
Note_B=10
Note_E4=5
prevFreq=0
z1=10
z2=0
z0=0
MIN_FREQUENCY = 20  #50
MAX_FREQUENCY = 1000  #600
#Max & Min values we care about
MAX_CENT = 11
MIN_CENT = 0
RELATIVE_FREQUENCY = 440.0
SHORT_NORMALIZE = (1.0/32768.0)

# if you pass in a parameter between 415 and 445 after "sudo python Guitar.py" this is set as the realtive frequency
#This is the frequency for A as A = 0

if len(sys.argv)>1:
    if (sys.argv[1]>=415.0 and sys.argv[1]<=415.0):
        RELATIVE_FREQUENCY = sys.argv[1]
    
# GPIO set up for rgb led and other leds
rgbled = RGBLED(16,20,22)#setting up pins for red,green and blue
ledE4 = LED(26)
ledE = LED(19)
ledB = LED(13)
ledG = LED(6)
ledD = LED(5)
ledA = LED(0)
# these default to

#function to reset all lifht to off postion

def allOff():
    ledE4.off()
    ledE.off()
    ledB.off()
    ledG.off()
    ledD.off()
    ledA.off()

def get_rms( block ):
    # RMS amplitude is defined as the square root of the mean over time of the square of the amplitude.
    # So we need to convert this string of bytes into a string of 16-bit samples...
    
    # We will get one short for each
    # Two chars in the string
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format,block )
    
    # iterate over the block
    sum_squares=0.0
    for sample in shorts:
        # sample is isgned short in +/- 32768
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n
    
    return math.sqrt(sum_squares/count)

#Set up audio sampler 
NUM_SAMPLES = 2048
# Number of samples per second - 48000 is a standard rate 
SAMPLING_RATE = 48000
pa=pyaudio.PyAudio()
_stream = pa.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=SAMPLING_RATE,
                  input=True,
                  frames_per_buffer=NUM_SAMPLES)

print("Detecing Frequencies, Press CTRL+C to quit.")

while True:
    while _stream.get_read_available() < NUM_SAMPLES: sleep(0.01) # checking if mic has enough data
    
    stream_data = _stream.read(_stream.get_read_available(),exception_on_overflow=False)
    audio_data = fromstring(stream_data, dtype=short)[-NUM_SAMPLES:]
    
    amplitude = get_rms(stream_data)
    
    if amplitude>0.01:
        print("amplitude",amplitude) #used for testing
        
        #Each data point is a signed 16 bit number, so we can normalize by diving 32*1024
        normalized_data = audio_data/32768.0
        w = hamming(2048)
        intensity = abs(w*fft(normalized_data))[:int(NUM_SAMPLES/2)]
        
        if frequencyoutput:
            which = intensity[1:].argmax()+1
            maxVal = intensity[which-1]
            adjfreq=1
            if which!=len(intensity)-1:
                y0,y1,y2=log(intensity[which-1:which+2:])
                x1=(y2-y0)*.5/(2*y1-y2-y0)
                # find the frequency and the output:w it
                thefreq=(which+x1)*SAMPLING_RATE/NUM_SAMPLES
                if thefreq < MIN_FREQUENCY or thefreq>MAX_FREQUENCY:
                    adjfreq=-9999
                else:
                    thefreq=which*SAMPLING_RATE/NUM_SAMPLES
                    if thefreq>MIN_FREQUENCY:
                        adjfreq=thefreq
            if (adjfreq != -9999):
                print("RAW_FREQ: ",adjfreq) # Also used for testing
                test_freq=adjfreq
                adjfreq=1200*log2(RELATIVE_FREQUENCY/adjfreq)/100
                adjfreq=adjfreq%12
                #Case statement
                # E
                if abs(adjfreq-Note_E4)<1 and test_freq>200:
                    #Different distence between low E and E
                    allOff()
                    ledE4.on()
                    # In tune E
                    if abs(adjfreq-Note_E4)<0.1:
                        print("You played an E!")
                        rgbled.color = (0,1,0)
                    # Sharp E
                    if abs(adjfreq-Note_E4)<0:
                        print("You played a Sharp E!")
                        rgbled.color = (1,0,0)
                    # Flat E
                    if abs(adjfreq-Note_E4)>0:
                        print("You played a Flat E!")
                        rgbled.color = (0,0,1)
                # low E
                elif abs(adjfreq-Note_E<1):
                    allOff()
                    ledE.on()
                    # In tune E
                    if abs(adjfreq-Note_E)<0.1:
                        print("You played a low E!")
                        rgbled.color = (0,1,0)
                    # Sharp E
                    if abs(adjfreq-Note_E)<0:
                        print("You played a Sharp E!")
                        rgbled.color = (1,0,0)
                    # Flat E
                    if abs(adjfreq-Note_E)>0:
                        print("You played a Flat E!")
                        rgbled.color = (0,0,1)
                # B
                elif abs(adjfreq-Note_B<1):
                    allOff()
                    ledB.on()
                    # In tune B
                    if abs(adjfreq-Note_B)<0.1:
                        print("You played a B!")
                        rgbled.color = (0,1,0)
                    # Sharp B
                    if abs(adjfreq-Note_B)<0:
                        print("You played a Sharp B!")
                        rgbled.color = (1,0,0)
                    # Flat B
                    if abs(adjfreq-Note_B)>0:
                        print("You played a Flat B!")
                        rgbled.color = (0,0,1)
                # G
                elif abs(adjfreq-Note_B<1):
                    allOff()
                    ledG.on()
                    # In tune G
                    if abs(adjfreq-Note_G)<0.1:
                        print("You played a G!")
                        rgbled.color = (0,1,0)
                    # Sharp G
                    if abs(adjfreq-Note_G)<0:
                        print("You played a Sharp G!")
                        rgbled.color = (1,0,0)
                    # Flat G
                    if abs(adjfreq-Note_G)>0:
                        print("You played a Flat G!")
                        rgbled.color = (0,0,1)         
                # D
                elif abs(adjfreq-Note_D<1):
                    allOff()
                    ledD.on()
                    # In tune D
                    if abs(adjfreq-Note_D)<0.1:
                        print("You played a D!")
                        rgbled.color = (0,1,0)
                    # Sharp D
                    if abs(adjfreq-Note_D)<0:
                        print("You played a Sharp D!")
                        rgbled.color = (1,0,0)
                    # Flat D
                    if abs(adjfreq-Note_D)>0:
                        print("You played a Flat D!")
                        rgbled.color = (0,0,1)            
                                # D
                elif abs(adjfreq-Note_A<1):
                    allOff()
                    ledA.on()
                    # In tune A
                    if abs(adjfreq-Note_A)<0.1:
                        print("You played an A!")
                        rgbled.color = (0,1,0)
                    # Sharp A
                    if abs(adjfreq-Note_A)<0:
                        print("You played a Sharp A!")
                        rgbled.color = (1,0,0)
                    # Flat A
                    if abs(adjfreq-Note_A)>0:
                        print("You played a Flat A!")
                        rgbled.color = (0,0,1)    
                elif abs(adjfreq - 12)<1:
                    allOff()
                    ledA.on()
                    # In tune A
                    if abs(adjfreq-Note_A)<0.1:
                        print("You played an A!")
                        rgbled.color = (0,1,0)
                    # Sharp A
                    if abs(adjfreq-Note_A)<0:
                        print("You played a Sharp A!")
                        rgbled.color = (1,0,0)
                    # Flat A
                    if abs(adjfreq-Note_A)>0:
                        print("You played a Flat A!")
                        rgbled.color = (0,0,1)    
            # All off
            else:
                rgbled.off()
    sleep(0.01)