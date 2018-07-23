fig,ax1=plt.subplots()
ax1.plot(xmat1,Fpot(xmat1),'b')
ax1.set_ylabel('F_Potential',color='b')
ax1.tick_params('y',colors='b')

ax2=ax1.twinx()
ax2.plot(xmat1,np.multiply(-1,Pmat),'r')
ax2.set_ylabel(' Log(Probability) observed',color='r')
ax2.tick_params('y',colors='r')


np.savetxt('myfile.txt', np.column_stack([xmat1,Pmat,F(xmat1)]))
#np.loadtxt('myfile.txt')
