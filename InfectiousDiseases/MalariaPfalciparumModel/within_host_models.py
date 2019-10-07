import numpy as np

import pandas as pd

from scipy.integrate import odeint

from InfectiousDiseases.MalariaPfalciparumModel.model_parameters import pf_model_parameters, pf_model_with_imm_parameters


def pf_model(y, t, pix, beta, mux, sigma, mus, mum, gamma, mug):

    x = y[0]; m = y[1]; s = y[2]; g = y[3]

    dxdt = pix - beta * m * x - mux * x
    dmdt = sigma * mus * s - mum * m - beta * m * x
    dsdt = beta * m * x - mus * s - gamma * s
    dgdt = gamma * s - mug * g

    return [dxdt, dmdt, dsdt, dgdt]


def pf_dynamics(time):
    y0 = [1e10, 1e6, 0, 0]

    t_step = 0.1; t = np.arange(0, time, t_step)

    par = pf_model_parameters()

    y = odeint(pf_model_with_imm, y0, t, par)

    x = y[:, 0]; m = y[:, 1]; s = y[:, 2]; g = y[:, 3]

    dynamics_df = pd.DataFrame([t, x, m, s, g]).T
    dynamics_df.columns = ['t', 'x', 'm', 's', 'g']

    return dynamics_df


def pf_model_with_imm(y, t, pix, beta, mux, sigma, mus, mum, gamma, mug,
                  theta, c0, c1, deltam, deltas, mub, lambdab, mua, num,
                  xim, xiy, rhos, rho1, rho2):
    x = y[0]; m = y[1]; s = y[2]; g = y[3]
    b = y[4]; a = y[5]

    dxdt = pix - beta * m * x / (1 + c0 * a) - mux * x - theta * x * m * b
    dmdt = sigma * mus * s / (1 + c1 * b) - mum * m - beta * m * x / (1 + c0 * a) - deltam * b * m
    dsdt = beta * m * x / (1 + c0 * a) - mus * s - gamma * s - deltas * b * s
    dgdt = gamma * s - mug * g

    dbdt = lambdab + xim * (m / (rho1 + m)) * b + xiy * (s / (rhos + s)) * b - mub * b
    dadt = num * b * m / (rho2 + m) - mua * a

    return [dxdt, dmdt, dsdt, dgdt, dbdt, dadt]


def pf_dynamics_with_imm(time):
    y0 = [1e10, 1e6, 0, 0, 0, 0]

    t_step = 0.1; t = np.arange(0, time, t_step)

    par = pf_model_with_imm_parameters()

    y = odeint(pf_model_with_imm, y0, t, par)

    x = y[:, 0]; m = y[:, 1]; s = y[:, 2]; g = y[:, 3]
    b = y[:, 4]; a = y[:, 5]

    dynamics_df = pd.DataFrame([t, x, m, s, g, b, a]).T
    dynamics_df.columns = ['t', 'x', 'm', 's', 'g', 'b', 'a']

    return dynamics_df

