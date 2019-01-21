import matplotlib.pyplot as plt
import numpy as np
comp=["Google","Facebook","TCS","IBM"]
rev=[1000,500,200,300]
profit=[200,100,50,70]

ypos=np.arange(len(comp))
plt.title("US Stocks")
plt.xticks(ypos,comp)#To provide label as company name in place of numbers
plt.bar(ypos-0.2,rev,width=0.4,label="Revenue")
plt.bar(ypos+0.2,profit,width=0.4,label="Profit")
plt.legend()
plt.show()

#HORIZONTAL CHARTS
ypos=np.arange(len(comp))
plt.title("US Stocks")
plt.yticks(ypos,comp)#To provide label as company name in place of numbers
plt.barh(ypos-0.2,rev,label="Revenue")
plt.barh(ypos+0.2,profit,label="Profit")
plt.legend()
plt.show()