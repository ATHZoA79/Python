import matplotlib.pyplot as plt
import numpy as np

class Hist:
    x_axis = []
    def __init__(self, inputs) :
        self.inputs = inputs
    
    def create_hist(self):
        step = 0
        print(inputs)
        max = np.max(inputs)
        print('max is :%d'%(max))
        if(max>=1000):
            step = 100
            print('step is: %d'%(step))
        if(max<1000 and max >= 100):
            step = 50
            print('step is: %d'%(step))
        if(max<100 and max >= 0):
            step = 10
            print('step is: %d'%(step))
        
        for i in range(0, int(max*1.1/step)):
            Hist.x_axis.append(i*step)
        print(Hist.x_axis)
        plt.hist(inputs, bins=Hist.x_axis, edgecolor='r')
        plt.show()

inputs = [709,419,405,684,847,901,970,30]
Hist.create_hist(inputs)   