def my_model(y, t, ka, F, K, K12, K21, K13, K31, K14, K41, K15, K51, K16, K61):
    G = y[0]; A1 = y[1]; A2 = y[2]; A3 = y[3]; A4 = y[4]; A5 = y[5]; A6 = y[6]

    dGdt = -ka * G
    dA1dt = F * ka * G + (K21 * A2 - K12 * A1) + (K31 * A3 - K13 * A1) + (K41 * A4 - K14 * A1) + \
            (K51 * A5 - K15 * A1) + (K61 * A6 - K16 * A1) - K * A1
    dA2dt = K12 * A1 - K21 * A2
    dA3dt = K13 * A1 - K31 * A3
    dA4dt = K14 * A1 - K41 * A4
    dA5dt = K15 * A1 - K51 * A5
    dA6dt = K16 * A1 - K61 * A6

    return [dGdt, dA1dt, dA2dt, dA3dt, dA4dt, dA5dt, dA6dt]


def model_parameters():

    ka = 0.0867; Cl = 15.5; F = 1; Vc = 368; Vd = 1060; Q = 16;

    K12 = Q / Vc; K21 = Q / Vd

    K13 = 0.01*K12; K31 = 0.05 * K21

    K14 = 0.001 * K12; K41 = 0.005 * K21

    K15 = 0.0001 * K12; K51 = 0.0005 * K21

    K16 = 0.00001 * K12; K61 = 0.00005 * K21

    K = Cl / Vc

    par = (ka, F, K, K12, K21, K13, K31, K14, K41, K15, K51, K16, K61)

    return par
