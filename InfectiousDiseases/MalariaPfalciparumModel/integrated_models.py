import numpy as np

import pandas as pd
from scipy.integrate import odeint

from InfectiousDiseases.MalariaPfalciparumModel.within_host_models import pf_model


def pharmacodynamics(kappa, c50, n, tc, C, mus):

    conc_res = pd.DataFrame([tc, C], index=['Time', 'Conc']).T
    conc_res['mus'] = mus + ((kappa - 1) * mus * conc_res['Conc'] ** n / (c50 ** n + conc_res['Conc'] ** n))

    return conc_res


def pop_pkpd(kappa, c50, n, tc, C, mus, pop_dynamics):

    conc_res = pharmacodynamics(kappa, c50, n, tc, C, mus)

    pix = 2 * 1e8 / 24; beta = (1e-9) / 24; mux = 1 / (120 * 24); sigma = 16
    mum = 48 / 24; gamma = 0.03 / 24; mug = 1 / (40 * 24)

    new_par = []
    for i in conc_res['mus'].index:
        n_par = (pix, beta, mux, sigma, conc_res['mus'][i], mum, gamma, mug)
        new_par.append(n_par)

    p_fal = 1.0 * 1e8
    drug_time = pd.DataFrame(pop_dynamics[pop_dynamics['s'] >= p_fal]['t'])
    drug_start = drug_time.index[0]

    new_y = odeint(pf_model, [pop_dynamics['x'][drug_start], pop_dynamics['m'][drug_start], pop_dynamics['s'][drug_start],
                                  pop_dynamics['g'][drug_start]], drug_time['t'][0:2], new_par[0])
    yy = new_y; drug_comp = []

    for j in range(1, len(conc_res['mus'])):

        if (conc_res['Conc'][j] > 0) and (conc_res['Conc'][j] < 1):
            y_n = odeint(pf_model, [yy[:, 0][1], yy[:, 1][1], yy[:, 2][1], yy[:, 3][1]], drug_time['t'][0:2],
                         new_par[0])

        else:
            y_n = odeint(pf_model, [yy[:, 0][1], yy[:, 1][1], yy[:, 2][1], yy[:, 3][1]], drug_time['t'][0:2],
                         new_par[j])

        yy = y_n
        drug_comp.append(yy[:, 2][1])

    pop_with_drug = np.concatenate([pop_dynamics['s'][0:drug_start + 1], drug_comp])

    t_df = np.arange(0, len(tc) + drug_start)

    return t_df, pop_with_drug, drug_start

