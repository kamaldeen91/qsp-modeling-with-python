import numpy as np

import pandas as pd
from scipy.integrate import odeint

from InfectiousDiseases.MalariaPfalciparumModel.within_host_models import pf_model_with_imm


def pop_pkpd(kappa, c50, tc, C, mus, pop_dynamics):

    conc_res = pd.DataFrame([tc, C], index=['Time', 'Conc']).T

    conc_res['mus'] = mus + ((kappa - 1) * mus * conc_res['Conc']/(c50 + conc_res['Conc']))

    pix = 2* 1e8 / 24; beta = 1e-9 / 24; mux = 1 / (120 * 24); sigma = 12; mum = 48 / 24
    gamma = 0.03 / 24; mug = 0.0625 / 24; theta = 1e-5; c0 = 0.6; c1 = 0.85; deltam = 4 / 24
    deltas = 4 / 24; mub = 5 / 24; lambdab = 0.01 / 24; mua = 2e-2 / 24; num = 1 / 24
    xim = 1 / 24; xiy = 1 / 24; rhos = 1e3; rho1 = 1e3; rho2 = 1e3

    new_par = []
    for i in conc_res['mus'].index:
        n_par = (pix, beta, mux, sigma, conc_res['mus'][i], mum, gamma, mug, theta, c0, c1, deltam, deltas,
                 mub, lambdab, mua, num, xim, xiy, rhos, rho1, rho2)

        new_par.append(n_par)

    p_fal = 1e6

    drug_time = pd.DataFrame(pop_dynamics[pop_dynamics['s'] >= p_fal]['t'])

    d_start = drug_time.index[0]

    new_y = odeint(pf_model_with_imm, [pop_dynamics['x'][d_start], pop_dynamics['m'][d_start], pop_dynamics['s'][d_start],
                                   pop_dynamics['g'][d_start], pop_dynamics['b'][d_start], pop_dynamics['a'][d_start]],
                   drug_time['t'][0:2], new_par[0])

    yy = new_y; drug_comp = []

    for j in range(1, len(conc_res['mus'])):

        if (conc_res['Conc'][j] > 0) and (conc_res['Conc'][j] < 1):
            y_n = odeint(pf_model_with_imm, [yy[:, 0][1], yy[:, 1][1], yy[:, 2][1], yy[:, 3][1], yy[:, 4][1], yy[:, 5][1]],
                         drug_time['t'][0:2], new_par[0])

        else:
            y_n = odeint(pf_model_with_imm, [yy[:, 0][1], yy[:, 1][1], yy[:, 2][1], yy[:, 3][1], yy[:, 4][1], yy[:, 5][1]],
                         drug_time['t'][0:2], new_par[j])

        yy = y_n
        drug_comp.append(yy[:, 2][1])

    pop_with_drug = np.concatenate([pop_dynamics['s'][0:d_start + 1], drug_comp])

    t_df = np.arange(0, len(tc) + d_start)

    return t_df, pop_with_drug, d_start

