import matplotlib.pyplot as mt
#..................
"""
mt.plot([1,2,5],[3,4,3],color='red',marker='o')
#marker is only use in line or dot  but not use in bar or pie
mt.title('firstgraph')
mt.xlabel('x-axis')
mt.ylabel('y-axis')

mt.xticks((1,2,5),('a','b','c'))  #replace the x axis point name with a b c 

#mt.hist(a)
mt.grid(True) #show the horizontal and vertical line...
mt.tick_params(axis='x',colors='white')
mt.tick_params(axis='y',colors='red')

mt.show()

"""
#....................................
"""
year=[2001,2002,2003]
orange=[24,45,67]
mango=[21,34,26]
mt.plot(year,orange)
mt.plot(year,mango)
#~~~~~~~~~~~~~~~~~~~~~~
"""

"""
#.............
mt.scatter([1,2,5],[3,4,3],color='red',marker='o')
#dot without line 
mt.legend(title='legend1')
mt.grid(True)
mt.show()


"""

"""
categories=['a','b','c','d']#x
values=[25,40,15,38]#y
mt.bar(categories,values,color='g',alpha=0.9)#color transperancy/brightness (0 - 9)
#show the output as the colomn
mt.ylabel('values')
mt.xlabel('categories')
mt.title('BAR')
mt.grid(True)
mt.show()

"""
#.....................

"""
categories=['a','b','c','d','e']
value=[10,10,10,10,10]
mt.pie(value, labels=categories, autopct='%1.1f%%',startangle=90)
#in circle shape define all the values...........
#autopct='%1.1f%%' adds percentage labels to the slices.
#lt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
mt.axis('equal')#means exact circle
mt.title('Pie Chart')
mt.legend(title='Legend)#for this u must be added a labels
mt.show()



"""
#................
#histogram
"""
#now lets draw the 3d graph
from mpl_toolkits.mplot3d import axes3d
fig=mt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
X,Y,Z=[1,2,3],[4,5,6],[6,7,8]
chart.plot_wireframe(X,Y,Z)
mt.show()

"""

"""
#practice

#mt.plot([4,5,6],[5,2,9],color='pink',marker='o')
#mt.bar([4,5,6],[5,2,9],color='pink',alpha=0.9)
size=[10,20,40]
lab=["a","b",'c']
mt.pie(size,labels=lab,startangle=90)
mt.axis('equal')
mt.legend(title="ravi")
mt.xlabel('x element')
mt.ylabel('y element')
mt.title('title1')
mt.grid(True)
mt.show()


#mt.scatter([4,5,6],[5,2,9],color='pink',marker='o')
#mt.show()


"""

"""
import matplotlib.pyplot as plt
import numpy as np
#for the random value generation 
data = np.random.randn(1000)


plt.hist(data, bins=5, color='purple', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(True)
plt.show()

"""
