# Metodo de Muller

# %% Reset
from IPython import get_ipython
get_ipython().magic('reset -sf')

# %% Funciones
import Funciones_Muller as f

# %% Entradas
print("\nMetodo de Muller\n")
Po = float(input("Ingrese el valor de la primera aproximacion(Po)\n"))
P1 = float(input("Ingrese el valor de la segunda aproximacion(P1)\n"))
P2 = float(input("Ingrese el valor de la tercera aproximacion(P2)\n"))
TOL = float(input("Ingrese el valor de la tolerancia(TOL)\n"))

if TOL != 0.0:
    tipErr = int(input("Escoja el tipo de error, 1:E_abs, 2:E_rel,3:E_%\n"))
else:
    print("\nTipo de error: porcencual")
    
No = int(input("Ingrese el numero maximo de interaciones(No)\n"))
guardar = input("¿Quiere guardar el resultado? y/n\n")

# %% Declaracion de variables
i = 3
E = 100.0
alfa = 1.0
epsilon = 6.123233995736766e-17
z = 0.0

AproxIni0 = Po
AproxIni1 = P1
AproxIni2 = P2

h1 = P1 - Po
h2 = P2 - P1
delta1 = (f.f(P1)-f.f(Po))/(h1)
delta2 = (f.f(P2)-f.f(P1))/(h2)
d = (delta2-delta1)/(h2+h1)

# %% Cosideraciones iniciales
if TOL == 0.0:
    TOL = epsilon
    tipErr = 3

if tipErr < 1.0 or tipErr > 3.0:
    tipErr = 2

#Tipo de error(Mensaje)    
if tipErr == 1:
    Err = "_abs"
elif tipErr == 2:
    Err = "_rel"
elif tipErr == 3:
    Err = "_%"

# %% Metodo de Muller
while E> epsilon and i<=No:
    
    b = delta2+h2*d
    D = ((b**2)-(4*f.f(P2)*d))**(1/2)
    
    if abs(b-D) < abs(b+D):
        E=b+D
    else:
        E=b-D
    
    h = -2*f.f(P2)/E
    p = P2+h
    
    if p != 0.0:
        E = f.Errores(tipErr,p,z)
        
    delta = abs(p-Po)
    alfa = abs(E/alfa)
    
    #Impresion y almacenamiento de resultados
    if abs(h) < TOL:
        print("-------------------------------------------------------------")
        print("Proceso exitoso")
        print("Po =",AproxIni0)
        print("P1 =",AproxIni1)
        print("P2 =",AproxIni2)
        print("p =",p)
        print("f(p) =",f.f(p))
        print("Error"+Err+" =",E)
        print("Alfa =",alfa)
        print("Delta =",delta)
        print("TOL =",TOL)
        print("No =",i)
        print("-------------------------------------------------------------")
        
        #Archivo de texto con los datos
        if guardar == "y":        
            resultado_Muller = open("resultado_Muller.txt","a")
            resultado_Muller.write("Po = "+str(AproxIni0)+"\n")
            resultado_Muller.write("P1 = "+str(AproxIni1)+"\n")
            resultado_Muller.write("P2 = "+str(AproxIni2)+"\n")
            resultado_Muller.write("p = "+str(p)+"\n")
            resultado_Muller.write("Error"+Err+" = "+str(E)+"\n")
            resultado_Muller.write("Alfa = "+str(alfa)+"\n")
            resultado_Muller.write("Delta = "+str(delta)+"\n")
            resultado_Muller.write("TOL = "+str(TOL)+"\n")
            resultado_Muller.write("No = "+str(i)+"\n")
            resultado_Muller.write("-------------------------------------------------------------\n")
            resultado_Muller.close()
        break
    
    i += 1
    z = p
    Po = P1
    P1 = P2
    P2 = p
    h1 = P1 - Po
    h2 = P2 - P1
    delta1 = (f.f(P1)-f.f(Po))/(h1)
    delta2 = (f.f(P2)-f.f(P1))/(h2)
    d = (delta2-delta1)/(h2+h1)
    alfa = E
    
if i > No:
    print("\nEl metodo ha fallado luego de la interación No =", i-1)            