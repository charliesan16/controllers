import numpy as np
from numpy.core.defchararray import array
from numpy.core.fromnumeric import size
import matplotlib.pyplot as plt
from numpy import sin, cos, array, arange, rad2deg
from math import sqrt
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'App')))
from App import Functions

def SCARAVel(a1, a2, n, v, xi, xf, yi, yf, zi, zf, codo):
    
    d, pe = Pe_punto(xi,yi,zi,xf,yf,zf,v)
    dt = deltaT(d,n,v)
    
    P = [xi, yi, zi]
    L = [0.1475, 0.195, 0.3185]
    theta1Inv, theta1InvDown, theta2Inv, theta2InvDown, theta3Inv, theta3InvDown = Functions.inverseKinematics('SCARA', P, L)
    if codo=='arriba':
      theta1 = theta1Inv
      theta2 = theta2Inv
      d3 = theta3Inv
    else:
      theta1 = theta1InvDown
      theta2 = theta2InvDown
      d3 = theta3InvDown
    
    q = np.zeros([3,n])
    q[0,0], q[1,0], q[2,0] = np.radians(theta1), np.radians(theta2), d3

    print(theta1, theta2, d3)
    print(np.radians(theta1), np.radians(theta2), d3)

    invJpS = JacobianoInversoSCARA(a1,a2,theta1, theta2)

    # Ecuación de recursividad
    for i in range(n-1):
        aux = q[:,i].reshape(3,1) + np.dot(np.dot(invJpS,pe),dt)
        q[0,i+1], q[1,i+1], q[2,i+1] = aux[0,0], aux[1,0], aux[2,0]
        invJpS = JacobianoInversoSCARA(a1,a2, q[0,i+1], q[1,i+1])

    return q

def JacobianoInversoSCARA(a1, a2, theta1, theta2):
  jpS = np.array([[-a2*np.sin(theta1+theta2)-a1*np.sin(theta1), -a2*np.sin(theta1+theta2), 0],
                    [a2*np.cos(theta1+theta2)+a1*np.cos(theta1), a2*np.cos(theta1+theta2), 0],
                    [0, 0, -1]])
  return np.linalg.inv(jpS)


#Antropomorfico

def Jacobiano_inverso(theta1,theta2,theta3):
  JP = array([[-1.5000e-30*(1.4263e+63*sin(theta1)*sin(theta3) - 1.0000e+30*cos(theta1)*cos(theta2)**2*cos(theta3) + 1.0000e+30*cos(theta1)*cos(theta2)*sin(theta2)*sin(theta3) + 1.0000e+30*cos(theta2)*cos(theta3)*sin(theta1)*sin(theta2))/(2*sin(theta3)*cos(theta2)**3 + sin(theta2)*cos(theta2)**2*cos(theta3) + 7.5199e+32*sin(theta3)*cos(theta2)*cos(theta3) + 2.9133e+32*sin(theta3)*cos(theta2) + 7.5199e+32*sin(theta2)*cos(theta3)**2 - 7.5199e+32*sin(theta2)),
               1.5000e-30*(1.4263e+63*cos(theta1)*sin(theta3) + 1.0000e+30*cos(theta2)**2*cos(theta3)*sin(theta1) + 1.0000e+30*cos(theta1)*cos(theta2)*cos(theta3)*sin(theta2) - 1.0000e+30*cos(theta2)*sin(theta1)*sin(theta2)*sin(theta3))/(2*sin(theta3)*cos(theta2)**3 + sin(theta2)*cos(theta2)**2*cos(theta3) + 7.5199e+32*sin(theta3)*cos(theta2)*cos(theta3) + 2.9133e+32*sin(theta3)*cos(theta2) + 7.5199e+32*sin(theta2)*cos(theta3)**2 - 7.5199e+32*sin(theta2)),
               (1.0723e+33*sin(theta3))/(1.4566e+32*sin(theta2 - theta3) - 3.7600e+32*sin(theta2 + 2*theta3) - 0.375*sin(3*theta2 + theta3) + 0.125*sin(3*theta2 - theta3) - 1.4566e+32*sin(theta2 + theta3) + 3.7600e+32*sin(theta2))],
               [(15.711544364448364326294319813323*(93944769614604776811620175985924.0*cos(theta1 - theta3) + 636229244166585186653671755374130.0*cos(2*theta2 - theta1 + 2*theta3) + 93944769614604776811620175985924.0*cos(theta1 + 2*theta2 + theta3) + 246480230385377215193284720034970.0*cos(theta1 + theta3) + 878725000000031286617740988731380.0*cos(theta1) + 246480230385377215193284720034970.0*cos(2*theta2 - theta1 + theta3) - 0.3125*cos(theta1 - 2*theta2 + 2*theta3) - 0.3125*cos(theta1 + 2*theta2 - 2*theta3) + 242495755833446099964069233357260.0*cos(theta1 + 2*theta2 + 2*theta3)))/(1.8799802893040330594257752372286e+33*sin(theta2 + 2*theta3) - 728319201099625950023901254260160.0*sin(theta2 - theta3) + 1.25*sin(3*theta2 + theta3) + 728319201099625950023901254260160.0*sin(theta2 + theta3) - 1.8799802893040330594257752372286e+33*sin(theta2)),
               (15.711544364448364326294319813323*(93944769614604776811620175985924.0*sin(theta1 - theta3) - 636229244166585186653671755374130.0*sin(2*theta2 - theta1 + 2*theta3) + 93944769614604776811620175985924.0*sin(theta1 + 2*theta2 + theta3) + 246480230385377215193284720034970.0*sin(theta1 + theta3) + 878725000000031286617740988731380.0*sin(theta1) - 246480230385377215193284720034970.0*sin(2*theta2 - theta1 + theta3) - 0.3125*sin(theta1 - 2*theta2 + 2*theta3) - 0.3125*sin(theta1 + 2*theta2 - 2*theta3) + 242495755833446099964069233357260.0*sin(theta1 + 2*theta2 + 2*theta3)))/(1.8799802893040330594257752372286e+33*sin(theta2 + 2*theta3) - 728319201099625950023901254260160.0*sin(theta2 - theta3) + 1.25*sin(3*theta2 + theta3) + 728319201099625950023901254260160.0*sin(theta2 + theta3) - 1.8799802893040330594257752372286e+33*sin(theta2)),
               (7.6506e+33*sin(2.0*theta2 + theta3) + 1.9748e+34*sin(2*theta2 + 2*theta3) + 1.1494e+34*sin(theta3))/(sin(3.0*theta2 - 1.0*theta3) + 1.1653e+33*sin(theta2 - theta3) - 3.0080e+33*sin(theta2 + 2*theta3) - 3.0*sin(3.0*theta2 + theta3) - 1.1653e+33*sin(theta2 + theta3) + 3.0080e+33*sin(theta2))],
               [-1.5000e-31*(2.0004e+63*cos(theta1 - 2*theta2) + 7.6243e+62*cos(theta1 + 2*theta2) + 7.1315e+63*cos(theta1 - theta3) + 1.3328e+64*cos(2*theta2 - theta1 + 2*theta3) + 5.0000e+30*cos(theta1 - 2*theta2 + theta3) + 3.9360e+63*cos(theta1 + 2*theta2 + theta3) + 7.1315e+63*cos(theta1 + theta3) + 2.1171e+64*cos(theta1) - 5.0000e+30*cos(theta1 + 2*theta2 - theta3) + 1.0327e+64*cos(2*theta2 - theta1 + theta3) + 5.0800e+63*cos(theta1 + 2*theta2 + 2*theta3))/(3.7600e+32*sin(theta2 + 2*theta3) - 1.4566e+32*sin(theta2 - theta3) + sin(3*theta2 + theta3)/4 + 1.4566e+32*sin(theta2 + theta3) - 3.7600e+32*sin(theta2)),
               -1.5000e-31*(2.0004e+63*sin(theta1 - 2*theta2) + 7.6243e+62*sin(theta1 + 2*theta2) + 7.1315e+63*sin(theta1 - theta3) - 1.3328e+64*sin(2*theta2 - theta1 + 2*theta3) + 5.0000e+30*sin(theta1 - 2*theta2 + theta3) + 3.9360e+63*sin(theta1 + 2*theta2 + theta3) + 7.1315e+63*sin(theta1 + theta3) + 2.1171e+64*sin(theta1) - 5.0000e+30*sin(theta1 + 2*theta2 - theta3) - 1.0327e+64*sin(2*theta2 - theta1 + theta3) + 5.0800e+63*sin(theta1 + 2*theta2 + 2*theta3))/(3.7600e+32*sin(theta2 + 2*theta3) - 1.4566e+32*sin(theta2 - theta3) + sin(3*theta2 + theta3)/4 + 1.4566e+32*sin(theta2 + theta3) - 3.7600e+32*sin(theta2)),
               -(5.0000e-32*(3.8253e+64*sin(2*theta2 + theta3) + 7.4098e+63*sin(2*theta2) + 4.9371e+64*sin(2*theta2 + 2*theta3)))/(1.4566e+32*sin(theta2 - theta3) - 3.7600e+32*sin(theta2 + 2*theta3) - 0.375*sin(3*theta2 + theta3) + 0.125*sin(3*theta2 - theta3) - 1.4566e+32*sin(theta2 + theta3) + 3.7600e+32*sin(theta2))]])


  return JP

def Pe_punto(xi,yi,zi,xf,yf,zf,v):
  deltax = xf-xi
  deltay = yf-yi
  deltaz = zf-zi
  d = sqrt((deltax**2) + (deltay**2) + (deltaz**2))
  u = array([[deltax],[deltay],[deltaz]]) / d
  Pe_p = u * v
  return d, Pe_p

def inversaAntro(px, py, pz):
    L1 = 0.1555
    L2 = 0.13617
    L3 = 0.35149

    theta1= np.arctan2(py,px)

    costheta3 = (px**2+py**2 + (pz-L1)**2 - L2**2 - L3**2)/(2*L2*L3)
    theta3rad = np.arccos(costheta3)
    theta3deg = theta3rad
    alpha =  np.arctan2(pz-L1,(px**2+py**2)**(1/2))
    beta = np.arctan2((L3*np.sin(theta3rad)),(L2+L3*np.cos(theta3rad)))

    theta2up = alpha - beta
    theta2down = alpha + beta
    theta3up = theta3deg
    theta3down = -theta3deg

    return theta1, theta2down, theta3down

def deltaT(d,n,v):
  delta_t = (d)/(n*v)
  return delta_t

def cinematicaDiferencial(n,v,xi,yi,zi,xf,yf,zf, codo):
  d, Pe_p = Pe_punto(xi,yi,zi,xf,yf,zf,v)
  dt = deltaT(d,n,v)
  P = [xi, yi, zi]
  L = [0.155, 0.13617, 0.35149]
  theta1Inv, theta1InvDown, theta2Inv, theta2InvDown, theta3Inv, theta3InvDown = Functions.inverseKinematics('Antropomorfico', P, L)

  if codo=='arriba':
    theta1 = theta1Inv
    theta2 = theta2Inv
    theta3 = theta3Inv
  else:
    theta1 = theta1InvDown
    theta2 = theta2InvDown
    theta3 = theta3InvDown

  qi = array([[np.radians(theta1)],[np.radians(theta2)],[np.radians(theta3)]])

  lista_q1 = [qi[0].item()]
  lista_q2 = [qi[1].item()]
  lista_q3 = [qi[2].item()]

  for i in range(n):
    JP = Jacobiano_inverso(qi[0].item(),qi[1].item(),qi[2].item())
    t1 = JP @ Pe_p
    t2 = t1*dt
    qi_1 = qi + t2
    qi = qi_1
    lista_q1.append(qi_1[0].item())
    lista_q2.append(qi_1[1].item())
    lista_q3.append(qi_1[2].item())
  return rad2deg(lista_q1),rad2deg(lista_q2),rad2deg(lista_q3)

