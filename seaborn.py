import numpy as np
import matplotlib.pyplot as plt

x=np.arange(10)
y1=x**2
print(x)
print(y1)

y2=2*x+3
print(y2)

plt.style.use('seaborn-notebook')
plt.plot(x,y1,color='red',marker="o")
plt.show()
plt.plot(x,y2,color='green',label="guava",linestyle="dashed")
plt.xlabel("colors")
plt.ylabel("movie")
plt.title("hey")
plt.plot(x,y1,color='blue',label="blueberry")
plt.legend()
plt.show()
#use plot show to draw multiple graphs , finish one of the graphs

prices=np.array([2,5,7,13])**2

plt.style.use('seaborn-notebook')
plt.plot(prices,color='magenta',marker="*",label="names")
plt.xlabel("prices")
plt.ylabel("stocks")
plt.legend()

plt.style.use('seaborn-notebook')
plt.scatter(x,y1,color='red',label='apple',marker='o')
plt.bar(x,y2,color='green')
plt.xlabel("Price")
plt.ylabel("Time")
plt.title("Prices of Fruits")
plt.legend()
plt.show()

plt.figure(figsize=(3,3))
plt.plot(x,y2,color='magenta',marker="o",label="y")
plt.legend()
plt.show()
