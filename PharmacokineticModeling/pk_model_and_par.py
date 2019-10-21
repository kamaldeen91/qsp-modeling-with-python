def my_model(y, t, K12, K21, K13, K31, K):
    A1 = y[0]; A2 = y[1]; A3 = y[2]

    # dGdt = -ka*G
    dA1dt = (K21*A2 - K12*A1) + (K31*A3 - K13*A1) - K * A1
    dA2dt = K12*A1 - K21*A2
    dA3dt = K13*A1 - K31*A3

    return [dA1dt, dA2dt, dA3dt]


def two_c_model(y, t, ka, K, K12, K21, F):
    G = y[0];
    A1 = y[1];
    A2 = y[2]

    dGdt = -ka * G
    dA1dt = F * ka * G + K21 * A2 - K12 * A1 - K * A1
    dA2dt = K12 * A1 - K21 * A2

    return [dGdt, dA1dt, dA2dt]


def model_parameters():

    # ka = 1.8; F = 0.89;

    # Cl = 15.5; Vc = 368; Vd = 1060; Q = 16;

    # K12 = Q / Vc; K21 = Q / Vd

    K12 = 0.7; K21 = 0.3
    K13 = 0.01; K31 = 0.002

    K = 0.28  # Cl / Vc

    par = (K12, K21, K13, K31, K)

    return par


def model_par_no_F():

    ka = 0.17; Cl = 15.5; Vc = 368; Vd = 1060; Q = 16
    K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc

    par = (ka, K, K12, K21)

    return par
