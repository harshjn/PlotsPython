"""
In this code, we see, how to generate subplots, as well as,
how to setup a size in inchesxInches for a figure,
and save figure, and effective ways to save results from a simulation.

Simulation for the langevin equation for the particle on a ring

For effective simulation, we see that we need to make sure that the order of magnitude of
dw and Fdt are comparable.
"""



import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
#import timeit


pi=np.pi;
dtheta=0.0001;
phi=np.arange(0,2*pi,dtheta);




#global A,thTrap,func
#A=0.0001/2
#func=A*(th-thTrap)**2 + 0.01


#U=-A*(-(phi-thTrap))*np.exp(-(phi-thTrap)**2/sigma);
#U=-A*np.exp(-(phi-thTrap)**2/sigma);

#plt.plot(np.diff(U)/dtheta)
#%%
N=int(1e7)
dt=0.01
thTrap=pi
#sigma=0.1;
dtheta=0.0001;
f=0.01
Eps=0.01

th=sp.symbols('th');
func=0.005*(1-np.e**(-(th-thTrap)**2/0.5**2))

func2=sp.diff(func,th)
U=sp.lambdify(th,func)     #Used for evaluation
dU=sp.lambdify(th,func2)


fig, ax = plt.subplots(nrows=2, ncols=2,figsize=(15.0, 9.0))

print('orders of magnitudes are as shown:')
stoch=[]
for i in range(10000):
    stoch+=[np.random.normal(0,np.sqrt(Eps*dt))] 
    
plt.subplot(2, 2, 1)

plt.hist(stoch)
plt.title('order of stochastic force='+str(np.average(np.abs(stoch))))

plt.subplot(2, 2, 2)



forc=-dU(phi)+f
plt.plot(phi,forc*dt)
plt.title('Order of F*dt, F=-Du+f, with f = '+str(f)+'and dt='+str(dt))

plt.subplot(2, 2, 3)

Uval=U(phi)
pot=U(phi)-f*phi
plt.plot(phi,pot)
plt.title('potential corresponding to f')


plt.show()
#%%
theta=np.zeros([N,1])
theta[0]=pi;
for i in range(1,N):
    dw=np.random.normal(0,np.sqrt(Eps*dt))
    F=-dU(theta[i-1])+f
    theta[i]=theta[i-1]+F*dt+dw
    theta[i]=np.mod(theta[i],2*pi)
    
    if np.mod(i,N/10)==0:
        print(i)
#%%
##plt.hist(theta,bins=100)
#Nbins=100
#a=np.histogram(theta,bins=np.arange(0,2*pi,2*pi/Nbins))
#
##%%
#line1,=plt.plot(a[1][1:Nbins],a[0],label='eps=1')
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)

#%%
#thetas=theta[0:int(240000000)]
dtval=dt
Nval=N
fu = lambda m, n: [i*n//m + n//(2*m) for i in range(m)]
SampSpac=int(1)
if SampSpac==1:
    thetas=theta;
else:  
    thetas=theta[(fu(int(Nval/SampSpac),int(Nval)))]



#%% Compare the data results
save=False
Theoreticaldata=np.loadtxt('C:/Users/Admin/OneDrive/BB30Lab/Project_OT/11.7.17SimulationResults/Eps=fExp.dat')
ThX=Theoreticaldata[1:101,0]
ThVals=Theoreticaldata[1:101,1]

Val_bins=Theoreticaldata[:,0]
a=np.histogram(thetas,bins=Val_bins)
SimVals=a[0]
plt.plot(ThX,SimVals)
plt.title('dt='+str(dtval)+'T='+str(np.round(Nval*dt))+'Eps='+str(Eps)+'SampleSpacing='+str(SampSpac))
plt.xlabel('angle')
plt.ylabel('Simsdata')
add='C:/Users/Admin/OneDrive/BB30Lab/Project_OT/11.7.17SimulationResults/Exp8Nov'
if save==True:
    plt.savefig(add+'SimExp'+str(Eps)+'a'+str(np.round(Nval*dt))+'SampSpace='+str(SampSpac)+'.tif')
    plt.close()
#%%
plt.plot(ThX,SimVals/ThVals)
plt.title('dt='+str(dtval)+'T='+str(np.round(Nval*dt))+'Eps='+str(Eps)+'SampleSpacing='+str(SampSpac))
plt.xlabel('angle')
plt.ylabel('Ratio of theory and sim')
if save==True:
    plt.savefig(add+'SimEps'+str(Eps)+'b'+str(np.round(Nval*dt))+'SampSpace='+str(SampSpac)+'.tif')
    plt.close()

 #%%
plt.close()
plt.plot(ThX,SimVals)
plt.plot(ThX,ThVals*np.mean(SimVals/ThVals))
plt.title('dt='+str(dtval)+'T='+str(np.round(Nval*dt))+'Eps='+str(Eps)+'SampleSpacing='+str(SampSpac))
plt.xlabel('angle')
plt.ylabel('Simsdata')
if save==True:
    plt.savefig(add+'SimEps'+str(Eps)+'c'+str(np.round(Nval*dt))+'SampSpace='+str(SampSpac)+'.tif')
    plt.close()

