import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[12,22,34,45,56,77,99]
z=[44,5,42,43,87,9,89]
w=[89,78,67,66,9,43,21]



plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather")
plt.plot(x,y, label="Max")
plt.plot(x,z, label="Min")
plt.plot(x,w, label="Average")
plt.legend()
plt.grid()
plt.show()