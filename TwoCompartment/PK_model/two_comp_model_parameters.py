def pk_two_comp_model_parameters():

    # ka = 0.0867; Cl = 15.5; F = 1; Vc = 368; Vd = 1060; Q = 16;
    #
    # K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc

    F = 0.89; ka = 1.8; K12 = 0.7; K21 = 0.3; K = 0.28;

    par = (ka, F, K, K12, K21)

    return par
