def pk_two_comp_model_parameters():

    ka = 0.0867; Cl = 15.5; F = 1; Vc = 368; Vd = 1060; Q = 16;

    K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc

    par = (ka, F, K, K12, K21)

    return par
