from InfectiousDiseases.MalariaPfalciparumModel.within_host_models import pf_dynamics
from InfectiousDiseases.MalariaPfalciparumModel.integrated_models import pop_pkpd
from InfectiousDiseases.MalariaPfalciparumModel.plot_combined_models import pop_model_output

from pqsp.pqsp_multi_dose_simulations import MultipleDose

pop_df = pf_dynamics(2000)


def model(y, t, ka, F, K, K12, K21):
    G = y[0]; A1 = y[1]; A2 = y[2]

    dGdt = -ka * G
    dA1dt = F * ka * G + K21 * A2 - K12 * A1 - K * A1
    dA2dt = K12 * A1 - K21 * A2

    return [dGdt, dA1dt, dA2dt]


ka = 0.867; Cl = 15.5; F = 1; Vc = 368; Vd = 1060
Q = 16; K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc

par = (ka, F, K, K12, K21)

mymultimodel = MultipleDose(model, par, number_of_compartments=3, number_of_dose=3, interval=8)

tc, C = mymultimodel.simulation(simulation_time=55, time_unit='days', dose_mg=[1000, 1000, 1000], compartment_pos=[1])


mus = 0.5/24

t_df, dynamics_with_drug, drug_start = pop_pkpd(15, 500, 2, tc, C, mus, pop_df)

pop_model_output(t_df, C, drug_start, pop_df, dynamics_with_drug, show_irbc=True, show_g=False)