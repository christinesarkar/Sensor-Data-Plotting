
import serial
import numpy as np
import matplotlib.pyplot as plt

try:
    ser = serial.Serial('COM3', baudrate = 9600, timeout=1)
except:
    print('Please check the port')


rawdata=[]
count=0


while count<10:
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
    file=open("boshir.txt",mode='w')
    for i in range(len(L)):
        file.write(L[i]+'\n')
    file.close()

write(cleandata)

x,y = np.loadtxt('boshir.txt',delimiter=',',unpack=True)
plt.plot(x,y)
plt.show()
