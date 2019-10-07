def pf_model_parameters():
    pix = 2 * 1e8 / 24; beta = 1e-9 / 24; mux = 1 / (120 * 24); sigma = 12; mus = 0.5 / 24
    mum = 48 / 24; gamma = 0.03 / 24; mug = 0.0625 / 24; theta = 1e-5; c0 = 0.6; c1 = 0.85

    deltam = 4 / 24; deltas = 4 / 24; mub = 5 / 24; lambdab = 0.01 / 24; mua = 2e-2 / 24
    num = 1 / 24; xim = 1 / 24; xiy = 1 / 24; rhos = 1e3; rho1 = 1e3; rho2 = 1e3

    par = (pix, beta, mux, sigma, mus, mum, gamma, mug, theta, c0, c1, deltam, deltas,
           mub, lambdab, mua, num, xim, xiy, rhos, rho1, rho2)

    return par


def pf_model_with_imm_parameters():
    pix = 2 * 1e8 / 24; beta = 1e-9 / 24; mux = 1 / (120 * 24); sigma = 12; mus = 0.5 / 24
    mum = 48 / 24; gamma = 0.03 / 24; mug = 0.0625 / 24; theta = 1e-5; c0 = 0.6; c1 = 0.85

    deltam = 4 / 24; deltas = 4 / 24; mub = 5 / 24; lambdab = 0.01 / 24; mua = 2e-2 / 24
    num = 1 / 24; xim = 1 / 24; xiy = 1 / 24; rhos = 1e3; rho1 = 1e3; rho2 = 1e3

    par = (pix, beta, mux, sigma, mus, mum, gamma, mug, theta, c0, c1, deltam, deltas,
           mub, lambdab, mua, num, xim, xiy, rhos, rho1, rho2)

    return par
