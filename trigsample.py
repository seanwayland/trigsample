
from pyo import *

# Creates and boots the server.
# The user should send the "start" command from the GUI.
s = Server(sr=96000, buffersize=256 ).boot()
s.start()
a = Input(chnl=0)

# Drops the gain by
s.amp = 0.5
# envelope pollower
fol2= Follower2(a, risetime=0.001, falltime=.01)
# pitch detection
pit = Yin(a, tolerance=0.2,minfreq=10, maxfreq=1000, cutoff = 1000, winsize=1000)

snd = "/Users/seanwayland/Desktop/pianoc.wav"

c = SfPlayer(snd, speed=1, loop=True , mul=fol2)
#trig = TrigEnv(SfPlayer(snd, speed=1, loop=True, mul=fol2), mul=.3)
amp = TrigEnv(c, table=HannTable(), mul=.7)
env = fol2


pva = PVAnal(c, size=2048)
pvt = PVTranspose(pva, transpo= pit)
pvs = PVSynth(pvt)
fx2 = STRev(pvs, inpos=0.25, revtime=2, cutoff=5000, mul=env, bal=0.01, roomSize=1).out()

# amp = TrigEnv(c, table=HannTable(), mul=.7)

# Creates a sine wave player.
# The out() method starts the processing
# and sends the signal to the output.
# b = Sine(freq=pit, mul=fol2).out(0)
# c = Sine(freq=pit, mul=fol2).out(1)
# octave lower
# d = Sine(freq=pit/2, mul=fol2).out(0)
# e = Sine(freq=pit/2, mul=fol2).out(1)

# Opens the server graphical interface.
s.gui(locals())
