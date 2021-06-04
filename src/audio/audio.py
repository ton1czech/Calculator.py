from pygame import mixer
import time

# mixer.init()

### SOUNDS ###
def s_coin():
    mixer.music.load('./coin.wav')
    mixer.music.play()
    time.sleep(1)

def s_fail():
    mixer.music.load('./fail.wav')
    mixer.music.play()
    time.sleep(1.5)

def s_laugh():
    mixer.music.load('./laugh.wav')
    mixer.music.play()
    time.sleep(7)