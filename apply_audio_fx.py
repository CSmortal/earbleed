from pyo import *
import urllib.request
import json
from constants import *

TEMP_FILE_PROCESSED = "./temp-fx.ogg"

# FX functions
def deep(sf, s, filedur):
  s.recordOptions(dur=filedur+3, filename=TEMP_FILE_PROCESSED, fileformat=7, quality=1.0)
  sf = Harmonizer(sf, transpo=-7.0, feedback=0).out()
  sf = STRev(sf, inpos=0.5, revtime=2.5, cutoff=1000, bal=0.85, roomSize=4, firstRefGain=-3).out()
  return sf

def chipmunk(sf):
  # sf.setSpeed([2,2])
  pva = PVAnal(sf, size=1024)
  pvt = PVTranspose(pva, transpo=2)
  sf = PVSynth(pvt).out()
  return sf

def echo(sf, s, filedur):
  s.recordOptions(dur=filedur+3, filename=TEMP_FILE_PROCESSED, fileformat=7, quality=1.0)
  sf = Delay(sf, delay=0.35, feedback=.5, mul=.43, maxdelay=2.5).out()
  return sf

def drunk(sf, s, filedur):
  s.recordOptions(dur=filedur*3.1, filename=TEMP_FILE_PROCESSED, fileformat=7, quality=1.0)
  sf.setSpeed([0.33,0.33])
  sf = Harmonizer(sf, transpo=13, feedback=0).out()
  sf = Delay(sf, delay=[0.13, 0.21], feedback=.25, mul=.4, maxdelay=2).out()
  return sf

def deepfried(sf):
  sf = Disto(sf, drive=1, slope=0.25, mul=0.15).out()
  return sf

def reverse(sf):
  sf.setSpeed([-1,-1])
  return sf

def bot(sf):
  sf = FreqShift(sf, shift=500, mul=1, add=0).out()
  return sf

# Main function
def effect_audio(file_id, API_KEY, effect):
  response = urllib.request.urlopen(f"https://api.telegram.org/bot{API_KEY}/getFile?file_id={file_id}")
  data = json.load(response)

  SERVER_FILE = f"https://api.telegram.org/file/bot{API_KEY}/{data['result']['file_path']}"
  TEMP_FILE = "./temp.oga"
  urllib.request.urlretrieve(SERVER_FILE, TEMP_FILE)

  s = Server(audio="offline").boot()
  filedur = sndinfo(TEMP_FILE)[1]
  s.recordOptions(dur=filedur, filename=TEMP_FILE_PROCESSED, fileformat=7, quality=1.0)
  
  # Read the og file
  sf = SfPlayer(TEMP_FILE, speed=[1,1])

  # EFFECTS GO HERE vvv
  if effect == DEEP:
    sf = deep(sf, s, filedur)
  elif effect == CHIPMUNK:
    sf = chipmunk(sf)
  elif effect == ECHO:
    sf = echo(sf, s, filedur)
  elif effect == DRUNK:
    sf = drunk(sf, s, filedur)
  elif effect == DEEPFRIED:
    sf = deepfried(sf)
  elif effect == REVERSE:
    sf = reverse(sf)
  # EFFECTS GO HERE ^^^

  sf.out()
  s.start()
