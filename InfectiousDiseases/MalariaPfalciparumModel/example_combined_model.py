from InfectiousDiseases.MalariaPfalciparumModel.Malaria_wh_model_plus_PKPD import WH_PKPD
from pqsp.pqsp_multi_dose_simulations import MultipleDose
from InfectiousDiseases.MalariaPfalciparumModel.within_host_models import pf_dynamics


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
time, conc = mymultimodel.simulation(simulation_time=43, time_unit='days', dose_mg=[1000, 1000, 1000], compartment_pos=[1])


combined_model = WH_PKPD(time, conc, 0.5/24, 15, 500, 2, pop_df)

combined_model.plot_model()

combined_model.parasite_reduction_ratio()
combined_model.parasite_clearance_time()
combined_model.recrudescence(end=43*24)
