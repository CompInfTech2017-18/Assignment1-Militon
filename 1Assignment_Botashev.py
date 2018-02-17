import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
P=np.pi
class solid_object:
    def __init__(self, Velocity0, angle, gravity, mass, plottr):
        self.V0=Velocity0
        self.m=mass
        self.a=angle
        self.g=gravity
        self.plotr=plottr
    
    def getx(self,time):
        return self.V0*np.cos(self.a)*time
    
    def gety(self,time):
        return self.V0*np.sin(self.a)*time-self.g*time**2/2
    
    
    def coordinate(self,time, interval):
        t=np.linspace(0,time,interval)
        x=self.getx(t)
        y=self.gety(t)
        self.plotr.plot(x,y)
        
        
        
class Plotter: 
	
	def __init__(self): #initialize a canvas to plot on
		self.fig = plt.figure()

	def plot(self, x, y): #Plotter interface, to plot we use this method
		return plt.scatter(x, y, marker='.')

	def show(self):
		plt.show()
        
body = solid_object(10, P/4, 9.8, 1.0, Plotter())
body.coordinate(10,10)

class dumbbell(solid_object):
    def __init__(self,Velocity0, angle, gravity, mass, plottr, radius, freq):
        self.R=radius
        self.fi=freq
        solid_object.__init__(self, Velocity0, angle, gravity, mass, plottr)
    
    def position(self, time, interval):
         t=np.linspace(0,time,interval)
         x1=self.getx(t)+self.R*np.cos(self.fi*t)
         y1=self.gety(t)+self.R*np.sin(self.fi*t)
         self.plotr.plot(x1,y1)
         x2=self.getx(t)+self.R*np.cos(self.fi*t-P)
         y2=self.gety(t)+self.R*np.sin(self.fi*t-P)
         print((x1-x2)**2+(y1-y2)**2)
         self.plotr.plot(x2,y2)
         
dumb=dumbbell(100, P/4, 9.8, 1.0, Plotter(),5, -P/7)
dumb.position(10,100)

class dipol(dumbbell):
    def __init__(self,Velocity0, angle, gravity, mass, plottr, radius, freq, q, E):
        self.w=freq
        self.q=q
        self.E=E
        self.mass=mass
        self.radius=radius
        solid_object.__init__(self, Velocity0, angle, gravity, mass, plottr)
        dumbbell.__init__(self,Velocity0, angle, gravity, mass, plottr, radius, freq)
        
    def position_dipol(self,time, interval):
        t=np.linspace(0,time,interval)
        def func(y,t):
         fi,w =y
         return [w, (self.mass*self.radius)/(self.q*self.E)*np.sin(fi)]
        omega=odeint(func,[0,self.w],t)[:,0]
        t=np.linspace(0,time,interval)
        x1=self.getx(t)+self.R*np.cos(omega)
        y1=self.gety(t)+self.R*np.sin(omega)
        self.plotr.plot(x1,y1)
        x2=self.getx(t)+self.R*np.cos(omega-P)
        y2=self.gety(t)+self.R*np.sin(omega-P)
        print((x1-x2)**2+(y1-y2)**2)
        self.plotr.plot(x2,y2)
        
dip=dipol(100, P/4, 9.8, 1.0, Plotter(),5, -P/7,1,1)
dip.position_dipol(10,100)