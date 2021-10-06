import numpy as np
from numpy.core.defchararray import array
from numpy.core.fromnumeric import size
import matplotlib.pyplot as plt


def SCARAVel(a1, a2, theta1, theta2, n, pep, xi, xf, yi, yf, zi, zf, d3):
    
    q = np.zeros([3,n])
    q[0,0], q[1,0], q[2,0] = theta1, theta2, d3


    jpS = np.array([[-a2*np.sin(theta1+theta2)-a1*np.sin(theta1), -a2*np.sin(theta1+theta2), 0],
                    [a2*np.cos(theta1+theta2)+a1*np.cos(theta1), a2*np.cos(theta1+theta2), 0],
                    [0, 0, -1]])

    invJPS = np.linalg.inv(jpS)

    deltaX = xf-xi
    deltaY = yf-yi
    deltaZ = zf-zi
    d = np.sqrt(((deltaX)**2)+((deltaY)**2)+((deltaZ)**2))
    deltaT = d/(n*np.absolute(pep))
    u = np.true_divide(np.array([[deltaX], [deltaY], [deltaZ]]), d)
    pe = pep*u

    # Ecuación de recursividad
    for i in range(n-1):
        aux = q[:,i].reshape(3,1) + np.dot(np.dot(invJPS,pe),deltaT)
        q[0,i+1], q[1,i+1], q[2,i+1] = aux[0,0], aux[1,0], aux[2,0]

    return q
