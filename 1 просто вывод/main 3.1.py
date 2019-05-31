import numpy
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('ex1data1.csv')

data1 = pd.DataFrame(file, columns = ['6.1101'])
data2 = pd.DataFrame(file, columns = ['17.592'])

X = data1['6.1101'].tolist()
Y = data2['17.592'].tolist()


plt.scatter(X,Y)

x1 = [4,23]
y1 = [0,-5]
y1[0] = 2*x1[0]-10
y1[1] = 2*x1[1]-10

plt.plot(x1,y1)


plt.show()




