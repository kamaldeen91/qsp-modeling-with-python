def one_comp_model(y, t, ka, F, K):
    G = y[0]; A = y[1]

    dGdt = -ka * G
    dAdt = F * ka * G - K * A

    return [dGdt, dAdt]
