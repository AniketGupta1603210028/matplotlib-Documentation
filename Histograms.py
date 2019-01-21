import matplotlib.pyplot as plt
bloodm=[29,30,50,60,70,80,77,88,99,66,100,101,22]
bloodw=[28,27,45,65,75,63,89,53,76,42,51,90,51]

plt.hist([bloodm,bloodw],bins=[30,60,100,170],rwidth=0.95,color=["green","red"],label=["men","women"])
plt.show()