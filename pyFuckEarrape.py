import numpy as np
import sounddevice as sd
import string, os, random, configparser
from os.path import exists
import time as t
userconfig = "/tmp/." + str(os.getlogin())+ "-pyFuckEarrape.cfg"
f = open(userconfig, "a")
f.close()
config = configparser.RawConfigParser()
config.read(userconfig)
duration = 1
def audio_callback(indata, frames, time, status):
   config.read(userconfig)
   volume_norm = np.linalg.norm(indata) * 10
   t.sleep(0.75)
   if volume_norm > int(config['AutochangeVolume']['max-allowed-as-safe'] :
       if int(config['AutochangeVolume']['notearraped']) == 1:
             num = int(config['DEFAULT']['lowvol'])
             run = "pactl set-sink-volume 0 " + str(num) + "%"
             os.system(run)
             config.set('AutochangeVolume', 'notearraped', '0')
             with open(userconfig, 'w') as configfile:
                 config.write(configfile)
                 configfile.close
   else:
       if int(config['AutochangeVolume']['notearraped']) == 0:
             num = int(config['DEFAULT']['lowvol'])
             num2 = int(config['DEFAULT']['maxvol'])
             while num <= num2:
                 run = "pactl set-sink-volume 0 " + str(num) + "%"
                 os.system(run)
                 num = num + 1
                 t.sleep(0.1)
                 config.set('AutochangeVolume', 'notearraped', '1')
             with open(userconfig, 'w') as configfile:
                 config.write(configfile)
                 configfile.close

stream = sd.InputStream(callback=audio_callback)
print("pyFuckEarrape started.")
while True:
    stream = sd.InputStream(callback=audio_callback)
    with stream:
        sd.sleep(duration * 1000)
