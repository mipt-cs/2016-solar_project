import numpy as np
import matplotlib.pyplot as plt

def Pifagor(x1, x2):
    return np.sqrt(x1**2 + x2**2)

def making_plots(object_properties, data_input_row):
    """
    function make plots for each planet:
    1)velocity(time)
    2)radius(time)
    3)velocity(radius)
    """
    time = [0]*len(data_input_row)
    data_input = [0]*len(data_input_row)
    for i in range(len(data_input_row)):
        time[i], data_input[i] = data_input_row[i]
    
    for i in range(len(object_properties)):
        if object_properties[i][0] == 'star':
            rep = i
    data_star = [data_input[j][rep] for j in range(len(data_input))]        
    number = len(object_properties)
    for i in range(number):#(i+1, 3, i*3+1,2,3) mb number-1
        data = [data_input[j][i] for j in range(len(data_input))]
        x, y = [], []
        x.append([Pifagor(data[j][0]-data_star[j][0], data[j][1]-data_star[j][1])  for j in range(len(data))])
        y.append([Pifagor(data[j][2], data[j][3]) for j in range(len(data))])
        sp = plt.subplot(number, 3, i*3+1)
        plt.plot(x[0], y[0])
        plt.grid(True)
        plt.title(object_properties[i][0]+' '+object_properties[i][2]+' '+'V(R)')
        x, y = [], []
        x = time
        y.append([Pifagor(data[j][2], data[j][3]) for j in range(len(data))])
        sp = plt.subplot(number, 3, i*3+2)
        plt.plot(x, y[0])
        plt.grid(True)
        plt.title(object_properties[i][0]+' '+object_properties[i][2]+' '+'V(t)')
        x, y = [], []
        x = time
        y.append([Pifagor(data[j][0]-data_star[j][0], data[j][1]-data_star[j][1]) for j in range(len(data))])
        sp = plt.subplot(number, 3, i*3+3)
        plt.plot(x, y[0])
        plt.grid(True)
        plt.title(object_properties[i][0]+' '+object_properties[i][2]+' '+'R(t)')
    plt.show()
        
        
        


if __name__ == "__main__":
    print("This module is not for direct call!")
