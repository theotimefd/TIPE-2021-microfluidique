import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# -------------------------------- PARAMETRES --------------------------------
#grille
L=100e-6
J = 150 #nombre de cases dans une colonne (y)
dy = float(L)/float(J-1)

N = 6000 #nombre de cases dans une ligne (t)
T = 10
dt = float(T)/float(N-1)

#D = 1e-10 #coefficient de diffusion 
D = 1e-10

r = D*dt/(dy**2)
if r>=0.5:
    print("simulation risquée dt trop grand ou dy trop petit")
    print("dt = " + str(dt))
    print("yt = " + str(dy))
    print("D = " + str(D))
    print("r = " + str(r))


# ------------------------------- FONCTIONS OUTIL ---------------------------

def calc_norme(A): # pas besoin
    norme = 0
    for i in range(len(A)):  
        norme += (A[i]**2)
    return np.sqrt(norme)

def moyenne(A):
    return sum(A)/len(A)

def ecart_type(A):
    moy = moyenne(A)
    ect = 0
    for i in range(len(A)):
        ect += (A[i] - moy)**2
    return np.sqrt(ect/len(A))


# ------------------------------- INTEGRATION --------------------------------

def schema_explicite(C0):
    
    ItMax = N
    C_tous_n = np.zeros((J,ItMax))  # colonne : pour un même tn ligne : pour un même yj
    C_tous_n[:,0] = C0[:] #initialisation de la premiere colonne de concentrations des points yj
    n = 1 #premiere iteration, instant dt
    Cint = 1 #conditions aux imites
    Cext = 0
    
    #profil de concentration à l'instant n = 1 
    C_tous_n[0,1] =  r*Cint + (1-2*r)*C_tous_n[0,0] + r*C_tous_n[1,0] #ligne 0 = point x1
    for j in range(1,J-1):
        C_tous_n[j,1]=r*C_tous_n[j-1,0] + (1-2*r)*C_tous_n[j,0] + r*C_tous_n[j+1,0]
    C_tous_n[J-1,1] = r*C_tous_n[J-2,0] + (1-2*r)*C_tous_n[J-1,0] + r*Cext
    
    #norme2 = calc_norme(C_tous_n[:,1]-C_tous_n[:,0])
    nbIter = 1
    
    while (nbIter<ItMax-1): #condition d'arret à vérifier
        
        C_tous_n[0,nbIter+1] =  r*C_tous_n[0,nbIter] + (1-2*r)*C_tous_n[0,nbIter] + r*C_tous_n[1,nbIter] #ligne 0 = point x1
        for j in range(1,J-1):
            C_tous_n[j,nbIter+1]=r*C_tous_n[j-1,nbIter] + (1-2*r)*C_tous_n[j,nbIter] + r*C_tous_n[j+1,nbIter]
        C_tous_n[J-1,nbIter+1] = r*C_tous_n[J-2,nbIter] + (1-2*r)*C_tous_n[J-1,nbIter] + r*C_tous_n[J-1,nbIter]
    
        #norme2 = calc_norme(C_tous_n[:,nbIter+1]-C_tous_n[:,nbIter])
        nbIter += 1
    return nbIter,C_tous_n


C00 = np.zeros(J) #condition initale de concentration
for i in range(len(C00)//2):
    C00[i] = 1


C01 = np.zeros(J)

nb_lamination = 4
largeur_lam = J//nb_lamination

c = 0
for i in range(0,J-largeur_lam,largeur_lam):
    if c==0 : c += 1
    else: c -= 1

    for j in range(largeur_lam):
        C01[i+j] = c


iterations, C_tous_n0 = schema_explicite(C00)    # on récupère les données pour les deux essais
iterations, C_tous_n1 = schema_explicite(C01)

print("iterations : " + str(iterations))

#   ----------------------- TEMPS DE MELANGE ------------------------

#  bien mélangé si écart-type inférieur à 0.2
ecartTypeMelange = 0.2
tau0 = 0 # temps de mélange pour premier essai
tau1 = 0 # pour deuxième essai (avec lamination)
for i in range(len(C_tous_n0[0,:])):
    if ecart_type(C_tous_n0[:,i])<ecartTypeMelange:
        tau0 = i*dt
        break
for i in range(len(C_tous_n1[0,:])):
    if ecart_type(C_tous_n1[:,i])<ecartTypeMelange:
        tau1 = i*dt
        break
print("temps de mélange pour ecartTypeMelange = " + str(ecartTypeMelange) + " :")
print("tau0 = " + str(round(tau0,2)) + " s")
print("tau1 = " + str(round(tau1,2)) + " s")


# ------------------------- AFFICHAGE -----------------------------

fig, axes = plt.subplots(2, 1,figsize=(20,10))


ax0 = sns.heatmap(ax=axes[0], data=C_tous_n0 , linewidth = 0 , cmap = "YlGnBu", cbar_kws={'label': 'Concentration'})
ax1 = sns.heatmap(ax=axes[1], data=C_tous_n1 , linewidth = 0 , cmap = "YlGnBu", cbar_kws={'label': 'Concentration'} )

ax0.set_title("Canal de " + str(L*1e6) + " μm pour D = " + str(D) + " m²/s")
ax1.set_xlabel("Temps écoulé, s")
ax0.set_xlabel("Temps écoulé, s")
ax1.set_ylabel("position y, μm")
ax0.set_ylabel("position y, μm")


def traduiret(x,pos):
    return str(round(int(x)*dt,1)) #pour passer d'un axe qui montre juste le nombre de points à un axe qui montre le temps écoulé

def traduirey(x,pos):
    return str(round(int(x)*dy*1e6,1))

formattert = FuncFormatter(traduiret)
formattery = FuncFormatter(traduirey)

ax0.yaxis.set_major_formatter(formattery)
ax0.xaxis.set_major_formatter(formattert)
ax0.xaxis.set_major_locator(plt.MaxNLocator(10))
ax0.xaxis.set_minor_locator(plt.MaxNLocator(100))

ax0.yaxis.set_major_locator(plt.MaxNLocator(10))
ax0.yaxis.set_minor_locator(plt.MaxNLocator(10))
ax0.vlines([tau0/dt], *ax0.get_xlim())

ax1.yaxis.set_major_formatter(formattery)
ax1.xaxis.set_major_formatter(formattert)
ax1.xaxis.set_major_locator(plt.MaxNLocator(10))
ax1.xaxis.set_minor_locator(plt.MaxNLocator(100))

ax1.yaxis.set_major_locator(plt.MaxNLocator(10))
ax1.yaxis.set_minor_locator(plt.MaxNLocator(10))
ax1.vlines([tau1/dt], *ax0.get_xlim())

plt.show()




def initial(n):       # crée un profil initial de concentration
    C0 = np.zeros(J)
    nb_lamination = n # avec n subdivisions de tailles égales
    largeur_lam = J//nb_lamination
    c = 0
    for i in range(0,J-largeur_lam,largeur_lam):
        if c==0 : c += 1
        else: c -= 1
        for j in range(largeur_lam):
            C0[i+j] = c
    return C0


tempsMelange = []

for j in [2,4,6,10]: # affiche un graphique de l'évolution de l'écart-type
    ecarts = []      # pour différents nombres de subdivisions
    iterations,C_tous_n = schema_explicite(initial(j))
    for i in range(len(C_tous_n[0,:])):
        ecarts.append(ecart_type(C_tous_n[:,i]))
    plt.plot([round(i*dt,2) for i in range(len(ecarts))],ecarts, label=str(j) + " subdivisions")
    
    for i in range(len(ecarts)):
        if ecarts[i]<ecartTypeMelange:
            tempsMelange.append(round(i*dt,2))
            break
        
print(tempsMelange)
    
plt.title("Influence du nombre de subdivisions dans l'efficacité de la lamination")
plt.xlabel("Temps écoulé en s")
plt.ylabel("Ecart-type")
plt.legend()
plt.show()

