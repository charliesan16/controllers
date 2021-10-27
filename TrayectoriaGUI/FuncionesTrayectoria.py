import numpy as np

def treyectoriaCuadratSCARA(thetai, thetaf, tf, dt): #Thetai y thetaf tienen que ser si o si ingresados como degrees
    a0 = thetai
    a1 = 0
    a2 = (3/tf**2)*(thetaf-thetai)
    a3 = -(2/tf**3)*(thetaf-thetai)
    ti = 0
    i = 0
    q = []
    qp =[]
    qpp = []
    for t in np.arange(ti, tf, dt):
        q.append(a3*t**3 + a2*t**2 + a1*t + a0)
        qp.append(3*a3*t**2 + 2*a2*t + a1)
        qpp.append(6*a3*t + 2*a2)
    return q, qp, qpp

def treyectoriaCuadratAntro(thetai, thetaf, tf, dt):
    a0 = thetai
    a1 = 0
    a2 = (3/tf**2)*(thetaf-thetai)
    a3 = -(2/tf**3)*(thetaf-thetai)
    ti = 0
    i = 0
    q = []
    qp =[]
    qpp = []
    for t in np.arange(ti, tf, dt):
        q.append(a3*t**3 + a2*t**2 + a1*t + a0) #Posicion ángular
        qp.append(3*a3*t**2 + 2*a2*t + a1) #velocidad ángular
        qpp.append(6*a3*t + 2*a2) #aceleración angular
    return q, qp, qpp

def trapes1Antropo(v, thetai, thetaf, tf, dt):
    qp = v
    qi = np.radians(thetai)
    qf = np.radians(thetaf)
    mayor = (2*np.abs(qf-qi))/tf
    menor = (np.abs(qf-qi))/tf
    #print(mayor, menor)
    ti = 0
    qt = []
    qtp = []
    qtpp = []
    if np.abs(qp) > menor and np.abs(qp) <= mayor:
        sgn = np.sign(qf-qi)
        tc = (qi-qf+qp*sgn*tf)/(qp*sgn)
        #print(tc)
        i=0
        if qp != 0:
            qpp = (qp/tc)

            for t in np.arange(ti, tf, dt):
                i+=1
                if t >=0 and t <= tc:
                    qt.append(qi+sgn*(1/2)*qpp*t**2) #Posición
                    qtp.append(sgn*qpp*t) #Velocito
                    qtpp.append(sgn*qpp)
                elif t > tc and t <= tf-tc:
                    qt.append((qi+sgn*(qpp*tc)*(t-(tc/2)))) #Posición
                    qtp.append(sgn*qp)
                    qtpp.append(0)
                elif t >tf-tc and t <= tf:
                    qt.append((qf-(1/2)*sgn*qpp*(tf-t)**2))
                    qtp.append(sgn*(-(qpp*(t-(tf-tc)))+qp))
                    qtpp.append(sgn*-qpp)

    return qt, qtp, qtpp

def trapes2Antropo(a, thetai, thetaf, tf, dt):
    qpp = a
    qi = np.radians(thetai)
    qf = np.radians(thetaf)
    mayor = (4*np.abs(qf-qi))/(tf**2)
    ti = 0
    qt = []
    qtp = []
    qtpp = []
    if  np.abs(qpp) >= mayor:
        sgn = np.sign(qf-qi)
        tc = (tf/2)-(1/2)*np.sqrt((tf**2*qpp*sgn-4*(qf-qi))/(qpp*sgn))
        i=0
        qp=qpp*tc
        if qpp != 0:
            for t in np.arange(ti, tf, dt):
                i+=1
                if t >=0 and t <= tc:
                    qt.append(qi+sgn*(1/2)*qpp*t**2) #Posición
                    qtp.append(sgn*qpp*t) #Velocito
                    qtpp.append(sgn*qpp)
                elif t > tc and t <= tf-tc:
                    qt.append(qi+sgn*qpp*tc*(t-tc/2)) #Posición
                    qtp.append(sgn*qp)
                    qtpp.append(0)
                elif t >tf-tc and t <= tf:
                    qt.append(qf-sgn*(1/2)*qpp*(tf-t)**2)
                    qtp.append(sgn*(-(qpp*(t-(tf-tc)))+qp))
                    qtpp.append(sgn*-qpp)

    return np.degrees(qt), np.degrees(qtp), np.degrees(qtpp)

def trapes1SCARA(v, thetai, thetaf, tf, dt):
    qp = v
    qi = thetai
    qf = thetaf
    mayor = (2*np.abs(qf-qi))/tf
    menor = (np.abs(qf-qi))/tf
    ti = 0
    qt = []
    qtp = []
    qtpp = []
    if np.abs(qp) > menor and np.abs(qp) <= mayor:
        sgn = np.sign(qf-qi)
        tc = (qi-qf+qp*tf*sgn)/(qp*sgn)
        i=0
        if qp != 0:
            qpp = (qp/tc)
            for t in np.arange(ti, tf, dt):
                i+=1
                if t >=0 and t <= tc:
                    qt.append(qi+sgn*(1/2)*qpp*t**2) #Posición
                    qtp.append(sgn*qpp*t) #Velocito
                    qtpp.append(sgn*qpp)
                elif t > tc and t <= tf-tc:
                    qt.append((qi+sgn*(qpp*tc)*(t-(tc/2)))) #Posición
                    qtp.append(sgn*qp)
                    qtpp.append(0)
                elif t >tf-tc and t <= tf:
                    qt.append((qf-(1/2)*sgn*qpp*(tf-t)**2))
                    qtp.append(sgn*(-(qpp*(t-(tf-tc)))+qp))
                    qtpp.append(sgn*-qpp)

    return qt, qtp, qtpp

def trapes2SCARA(a, thetai, thetaf, tf, dt):
    qpp = a
    qi = np.radians(thetai)
    qf = np.radians(thetaf)
    mayor = (4*np.abs(qf-qi))/(tf**2)
    ti = 0
    qt = []
    qtp = []
    qtpp = []
    if  np.abs(qpp) >= mayor:
        sgn = np.sign(qf-qi)
        tc = (tf/2)-(1/2)*np.sqrt((tf**2*qpp*sgn-4*(qf-qi))/(qpp*sgn))
        i=0
        qp=qpp*tc
        if qpp != 0:
            for t in np.arange(ti, tf, dt):
                i+=1
                if t >=0 and t <= tc:
                    qt.append(qi+sgn*(1/2)*qpp*t**2) #Posición
                    qtp.append(sgn*qpp*t) #Velocito
                    qtpp.append(sgn*qpp)
                elif t > tc and t <= tf-tc:
                    qt.append(qi+sgn*qpp*tc*(t-tc/2)) #Posición
                    qtp.append(sgn*qp)
                    qtpp.append(0)
                elif t >tf-tc and t <= tf:
                    qt.append(qf-sgn*(1/2)*qpp*(tf-t)**2)
                    qtp.append(sgn*(-(qpp*(t-(tf-tc)))+qp))
                    qtpp.append(sgn*-qpp)

    return qt, qtp, qtpp