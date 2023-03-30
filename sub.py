import schedule
import time 
import datetime
import main

def work():
   main.receive()
   print(datetime.datetime.today())
  
while True:
  try:
     work()
     schedule.run_pending()
     time.sleep(600)

  except:
     pass
     time.sleep(600)
