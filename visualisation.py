import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#multivariate normal distribution

mean=np.array([0.0,0.0])
cov=np.array([[1,0],[0,1]])
dist=np.random.multivariate_normal(mean,cov,500)
#print(dist)
plt.scatter(dist[:,0],dist[:,1],color='green')
plt.show()

mean=np.array([0.0,0.0])
cov=np.array([[1,0.8],[0.8,1]])
dist=np.random.multivariate_normal(mean,cov,500)
#print(dist)
plt.scatter(dist[:,0],dist[:,1],color='magenta')
plt.show()

mean1=np.array([0.0,0.0])
cov1=np.array([[1,0.8],[0.8,1]])#1 is sigma y
mean2=np.array([5,6])
cov2=np.array([[1.3,0.2],[0.2,1.1]])#1.1 is sigma y

dist1=np.random.multivariate_normal(mean1,cov1,500)
dist2=np.random.multivariate_normal(mean2,cov2,500)
print(dist1.shape)

plt.scatter(dist1[:,0],dist1[:,1])
plt.scatter(dist2[:,0],dist2[:,1])
