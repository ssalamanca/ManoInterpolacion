import sys
import numpy as np
import scipy as sp
#from scipy.interpolate import CubicSpline
import scipy.interpolate
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.image as mimg
import tkinter as tk
from tkinter import filedialog
kindw=input("tipo de interpolacion(zero,quadratic,linear,slinear):")
limit=int(input("Cuantos puntos desea:"))
if(limit!=-1):
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()
	root.destroy()

"""
esto parte el arreglo de puntos
"""
temp1 = []
temp2 = []
continu=0


if limit != -1:
	try:
		img=mimg.imread(file_path)
		imgplot=plt.imshow(img)
		ax = plt.gca()
		fig = plt.gcf()
		implot = ax.imshow(img)
	except:
		print("El achivo no es una imagen")
		exit()
	

#plt.figure()
coords = []


def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print(ix,iy)
    global coords
    coords.append((ix, iy))
    if len(coords) == limit:
        fig.canvas.mpl_disconnect(cid)
        plt.close(fig)
        x1,y1=zip(*coords)
        global continu   
        continu=1
    return coords
if limit  != -1:  
	cid = fig.canvas.mpl_connect('button_press_event', onclick)
else:
	continu=1
plt.show()
while continu==0:
	qw=0
x1=np.array([268.4,263.2,260.6,234.8,198.7,172.9,162.6,183.2,211.7,219.4,232.2,255.5,268.4,304.5,312.3,327.7,338.1,340.6,343.2,348.4,351.1,345.8,351.0,369.0,397.4,410.3,415.5,418.1,431.0,428.4,436.1,456.8,477.4,500.6,508.4,518.7,539.4,549.7,578.1,588.4,580.6,567.7,570.3,552.3,544.5,596.1,632.3,663.2,701.9,727.7,740.6,758.7,756.1,740.6,709.7,676.1,637.4,619.4,606.5,611.6,634.8,665.8,699.4,748.4,789.7,828.4,872.3,882.6,859.4,805.2,761.3,701.9,645.2,603.9,563.6,526.5])
y1=np.array([474.3,559.5,662.7,755.6,840.7,913.0,972.4,993.0,1000.7,990.4,962.0,900.1,882.0,812.4,796.9,789.1,794.3,835.6,938.8,972.4,1005.9,1034.3,1106.6,1134.9,1127.2,1109.1,1029.1,972.4,944.0,879.5,833.0,869.1,951.5,1018.8,1098.8,1124.6,1142.7,1147.8,1132.4,1111.7,1026.6,982.7,949.1,884.4,809.8,871.7,933.6,980.1,1052.4,1065.3,1067.8,1042.0,1013.6,969.8,915.6,838.2,765.9,711.7,649.8,631.7,626.5,626.6,642.0,678.2,698.8,704.0,685.9,665.3,634.3,605.9,572.4,544.0,487.2,451.1,414.9,389.1])
if(limit!=-1):
	x1,y1=zip(*coords)
x=np.array(x1)
y=np.array(y1)
if limit !=-1:
	for KI in range(0,len(y)):y[KI]=y[KI]*-1 

plt.subplot(1,2,1)
plt.title('Mano con puntos ')
plt.plot(x,y,'b.-')
plt.subplot(1,2,2)
plt.title('Mano interpolada')

def arrays(temp):
  for i in range(len(temp)):
    temp1.append(temp[i][0])
    temp2.append(temp[i][1])
    print(temp[i][0],temp[i][1])

def plotear(aux):
		arrays(aux)
		#plt.plot(temp1,temp2,'b.-')
		
		x1=np.array(temp1)	
		x2=np.array(temp2)	
		#X = np.linspace(x1.min(), x1.max(),40)
		#y1=np.interp(X,x1,x2)
		#yP=InterpolatedUnivariateSpline(x1,x2)(X)
		try:
			new_x = np.linspace(x1.min(), x1.max(),20)
			new_y = sp.interpolate.interp1d(x1, x2, kind=kindw)(new_x)
			#plt.plot(X, yP,'r.-')
			plt.plot(new_x,new_y,'r.-')
			temp1.clear()	
			temp2.clear() 
			
		except:
			print ("Oops!  no se pudo interpolar esos puntos ;v")
			return
  



def separar(x,y):
  sentido=0
  aux=[]
  otra=[]
  print(len(x))
  for i in range(1,len(x)):
    temp=x[i-1],y[i-1]
    if(i==len(x)-1):
      temp=x[i],y[i]
    if temp[0]<=x[i]:
      if(sentido==0):
        aux.append(temp)
        plotear(aux)
        print("---")
        aux.clear()
      sentido=1
      aux.append(temp)
    if temp[0]>=x[i]:
      if(sentido==1):
        aux.append(temp)
        plotear(aux)
        print("---")
        aux.clear()
      sentido=0
      aux.append(temp)


separar(x,y)
plt.show()

