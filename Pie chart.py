import matplotlib.pyplot as plt
x=[10,20,30,40]
y=["tea","Floor","Rice","Vegetables"]
plt.axis("equal")
plt.pie(x,labels=y,autopct='%0.1f%%',shadow=True,explode=[0,0.3,0,0.1])
plt.show()