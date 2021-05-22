import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

t = np.loadtxt("Serie2.txt", delimiter=" ", dtype=int, usecols=(0,1))
temps = t[:,0]
dist=t[:,1]
dist = dist*1.03e-4 #conversion pixels -> mètres
dist = dist-dist[0] 
#print(temps)
#print(dist)


def modele(t,D): # L en fonction de T et D
    return np.sqrt(D*t) # D = L^2/T

params, params_covariance = optimize.curve_fit(modele, temps, dist, p0=[1e-5]) #params : coefficient de diffusion
print("Coefficient de diffusion : D = " + str(params[0]) + " m^2/s")


plt.scatter(temps,dist)

tps = np.linspace(0,temps[len(temps)-1], 200)
plt.plot(tps,modele(tps,params[0]), c="red")

plt.xlabel("Temps en s")
plt.ylabel("Distance caractéristique L-L0 en m")
plt.show()
