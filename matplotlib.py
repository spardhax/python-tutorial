import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=x**2 + 3
print(x,y)

plt.style.available

plt.style.use('seaborn-muted')
plt.title("My line")
plt.plot(x,y,label="Stock Price")
#the label would not appear unless you call it through legend

plt.style.use('seaborn-white')
plt.title("My line")
plt.plot(x,x**2,label="Stock Price")
plt.plot(x,y,label="Another price")
plt.legend()
plt.xlabel("Time stamp")
plt.ylabel("Price")

#scatter plot
plt.style.use('dark_background')
plt.scatter(x,x**2,label="scatter graph")
plt.legend()
