import numpy as np

def matrixT(theta, alpha, a, d):
    matriz = np.array([[np.cos(theta), -np.sin(theta)*np.cos(alpha),  np.sin(theta)*np.sin(alpha),  a*np.cos(theta)],
                      [np.sin(theta),  np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha),  a*np.sin(theta)],
                      [0,              np.sin(alpha),                np.cos(alpha),                d               ],
                      [0,              0,                            0,                            1               ]])
    return matriz

def totalMatrix(m1, m2, m3):
    return (m1.dot(m2)).dot(m3)

def inverseKinematics(name, P, L):
    if name == 'Antropomorfico':
        theta1 = np.degrees(np.arctan2(P[1],P[0]))
        costheta3 = ( P[0]**2+P[1]**2 + (P[2]-L[0])**2 - L[1]**2 - L[2]**2 )/(2*L[1]*L[2])
        theta3rad = np.arccos(costheta3)
        theta3deg = np.degrees(theta3rad)
        alpha = np.degrees(np.arctan2(P[2]-L[0],(P[0]**2+P[1]**2)**(1/2)))
        beta = np.degrees(np.arctan2((L[2]*np.sin(theta3rad)),(L[1]+L[2]*np.cos(theta3rad))))

        theta2up = -alpha + beta
        theta2down = -(alpha + beta)
        theta3up = -theta3deg
        theta3down = theta3deg

        return theta1, theta1, theta2up, theta2down, theta3up, theta3down
    else:
        theta3= L[2]-P[2]
        d = (P[0]**2+P[1]**2)**(1/2)
        costheta2 = (d**2-L[0]**2-L[1]**2)/(2*L[0]*L[1])
        theta2 = np.degrees(np.arccos(costheta2))

        alpha = np.arctan2(P[1],P[0])
        beta = np.abs(np.arccos((L[1]**2 - d**2 - L[0]**2)/(-2*L[0]*d)))
        theta1up = np.degrees(alpha + beta)
        theta1down =  np.degrees(alpha - beta)

        return theta1up, theta1down, -theta2, theta2, theta3, theta3 
    