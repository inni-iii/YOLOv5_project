from lidar_lite import Lidar_Lite
import os

def speak(option,msg):
    os.system("espeak {} '{}'".format(option,msg))
    
option = '-s200 -p99 -a100' 
msg = 'warning'#'be careful'  # warning
#print('espeak', option, msg)


lidar = Lidar_Lite()
connected = lidar.connect(1)
if connected == 0:
    while(1):
        if lidar.getDistance() <= 100 :
            print('warning')
            speak(option,msg)
            
        else:
            print (lidar.getDistance())
        

    if connected < -1:
      print ("Not Connected")

