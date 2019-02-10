# Animated display of ADC data (ADS1115)
# Created by Noah Carpenter

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import Adafruit_ADS1x15
import time



# Create an ADS1115 ADC interface
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

# gain value should be one of the following:
# 2/3 for +/- 6.144 Volts
# 1   for +/- 4.096 volts
# 2   for +/- 2.048 volts
# 4   for +/- 1.024 volts
# 8   for +/- 0.512 volts
# 16  for +/- 0.256 volts

GAIN = 2/3

# CHANNEL is the ADC channel (0 through 3)

CHANNEL = 0

# Set up the basic figure elements
'''
fig = plt.figure() # the figure to plot

ax = plt.axes(xlim=(0,10),ylim=(-15,15)) # the figure axes

(line,) = ax.plot([],[],lw=2) # start with a null line

x = np.linspace(0,10,301) # x-axis goes from 0 to 10, increments of 1/30 second
y = 0*x # y is same size as x, initially equal to zero
ly = list(y) # ly is the y-array, but in list form

# i is a counter variable used to generate data
'''
i = 0

# plot initialization function
def init():
	line.set_data([],[])
	return (line,)

# get_data() gets the next y-value to plot

def get_data(i):
	return adc.read_adc(CHANNEL, gain=GAIN)/(8192*GAIN)

# animate() is the animation plot
def animate(i):
	ly.pop(0) # pop off first element of y
	ly.append(get_data(i)) # add on the next data point
	y = np.asarray(ly) # convert list into array
	line.set_data(x,y) # load array data into the line
	return (line,)

# Set up the animation for matplotlib
'''
anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=33)
'''

# show the animation

#plt.show()

def tenSeconds():
        total = 0
        values = []
        newValues = []
        multipliedValues =[]
        derValues = []
        smoothedValues = []
        beatList = []
        totalBeats = 0
        bpm = 0
        
        for i in range(300): #Gets a new value each 1/30 second, adds to list
                value = get_data(1)
                total = total + value
                values.append(value)
                time.sleep(1/30)
                
        avg = total/(i+1)
        print("Average:",avg)

        for i in range(len(values)): #Subtract average from each value
                newValues.append(values[i]-avg)

        
        for i in range(len(newValues)): #Multiply each value by scalar 
                multiplier = 100
                multipliedValues.append(newValues[i] * multiplier)
                #print(newValues[i],multipliedValues[i])
        #print(multipliedValues)
        plt.plot(multipliedValues)
        plt.ylabel('newPlot')

        '''
for i in range(len(value)): #I'm attempting to do the sliding computation Derin just showed on the board
        
        
        
        '''
        

        for i in range(len(multipliedValues)-1): #Establish a derivative list
                derValues.append(multipliedValues[i+1] - multipliedValues[i])

        for i in range(len(derValues)-1):
                if derValues[i] > 0 and derValues[i+1] < 0:
                        totalBeats = totalBeats+1
                        beatList.append(i)
                        
        for i in range(len(beatList)):
                plt.plot(beatList[i],multipliedValues[beatList[i]],'ro')
        
        print("totalBeats:",totalBeats)
        bpm = 6*totalBeats
        print("BPM: ",bpm)
        print(beatList)
        plt.show()
                

        
