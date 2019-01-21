import matplotlib.pyplot as plt
#%matplotlib inline

x=[1,2,3,4,5,6,7,8,9]
y=[10,20,40,50,30,20,22,40,88]

plt.plot(x,y,color="green")
plt.show()

plt.xlabel("Temperature")
plt.ylabel("windspeed")
plt.title("Temp_vs_Windspeed")
plt.plot(x,y,color="green",linewidth=5,linestyle="dashdot")
plt.show()

#Format Strings
plt.plot(x,y,'g+--')
plt.show()