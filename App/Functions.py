import numpy as np

def matrixT(theta, alpha, a, d):
    matriz = np.array([[np.cos(theta), -np.sin(theta)*np.cos(alpha),  np.sin(theta)*np.sin(alpha),  a*np.cos(theta)],
                      [np.sin(theta),  np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha),  a*np.sin(theta)],
                      [0,              np.sin(alpha),                np.cos(alpha),                d               ],
                      [0,              0,                            0,                            1               ]])
    return matriz

def totalMatrix(m1, m2, m3):
    return (m1.dot(m2)).dot(m3)