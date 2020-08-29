
import serial
import numpy as np
import matplotlib.pyplot as plt

try:
    ser = serial.Serial('COM4', baudrate = 9600, timeout=1)
except:
    print('Please check the port')


rawdata=[]
count=0


while count<20:
    rawdata.append(str(ser.readline()))
    count+=1
print(rawdata)

def clean(L):
    newl=[]
    for i in range(len(L)):
        temp=L[i][2:]
        newl.append(temp[:-5])
    return newl
    
cleandata=clean(rawdata)

def write(L):
    file=open("cms.txt",mode='w')
    for i in range(len(L)):
        file.write(L[i]+'\n')
    file.close()

write(cleandata)

x,y = np.loadtxt('cms.txt',delimiter=',',unpack=True)
plt.plot(x,y)
plt.show()

    
