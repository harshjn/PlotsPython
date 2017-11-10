"""
In this code, we see, how to generate subplots, as well as,
how to setup a size in inchesxInches for a figure,
and save figure, and effective ways to save results from a simulation.

Simulation for the langevin equation for the particle on a ring

"""



#%% How to insert Legends
#%%
#import matplotlib.patches as mpatches
#import matplotlib.lines as mlines

Data,= plt.plot(eps,elogP,'r+',markersize=10)


z=np.polyfit(eps,elogP,1)
pf=np.poly1d(z)

xp = np.linspace(0, 6, 1000)

Polyfit,= plt.plot(xp, pf(xp), 'c--',dashes=(5, 1))


#Red_patches = mpatches.Patch(color='red', marker='*',
#                          markersize=15, label='Data Points')
#
#
#cyan_dashes = mlines.Line2D( [],[],color='cyan',
#                          markersize=5, label='Poly Fit')
                          
#plt.legend(handles=[cyan_dashes,Red_patches])
plt.legend([Data,Polyfit], ["DataPoints","Fitted data"])

plt.title('Estimation of the Large Deviation Function')

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

