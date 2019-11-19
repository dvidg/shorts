import requests
import json
import time
import datetime

# Woolacombe 1352 | Porthcawl 1449
def getJSON(ID,bounds):

  url  = "http://magicseaweed.com/api/082f1c64c83ce0ed8ba3f08b805fb6fa/forecast/?spot_id="
  full = url+str(ID)+"&start="+str(bounds[0])+"&end="+str(bounds[1])+"&units=eu"
  return requests.get(full).json()



def main(id):
  boundTime = getTime()
  b = getJSON(id,boundTime)
  return getData(b, boundTime)


if __name__ == '__main__':
  # execution as script
  main(id)

