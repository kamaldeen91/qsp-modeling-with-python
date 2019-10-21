from pqsp.pqsp_multi_bioav import MultipleDoseVaryBioav
from pqsp.pqsp_multi_bioav_delay import MultipleDoseVaryBioavDelay


def two_c_model(y, t, ka, K, K12, K21, F):
    G = y[0]; A1 = y[1]; A2 = y[2]

    dGdt = -ka * G
    dA1dt = F * ka * G + K21 * A2 - K12 * A1 - K * A1
    dA2dt = K12 * A1 - K21 * A2

    return [dGdt, dA1dt, dA2dt]


ka = 0.17; Cl = 15.5; Vc = 368; Vd = 1060; Q = 16
K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc

par = [ka, K, K12, K21]

#############################

mymultimodel = MultipleDoseVaryBioav(two_c_model, par, number_of_compartments=3, number_of_dose=4, interval=24, bioav=[1, 0.51, 0.41, 0.6])
tn, cn = mymultimodel.simulation(simulation_time=8, time_unit='days', dose_mg=[10])
mymultimodel.plot_simulation(tn, cn, show_auc=True, show_max=True)
mymultimodel.multi_dose_vary_bioav_plot(simulation_time=8, time_unit='days', drug_doses=[10,20,30],
                                   compartment_pos=[0,1,2], figsize=(12,8))


#############################

mymultimodel_delay = MultipleDoseVaryBioavDelay(two_c_model, par, number_of_compartments=3, number_of_dose=4, interval=24,
                                                delay=[6,3,0], bioav=[1, 0.7, 0.9, 0.4])
tnn, cnn = mymultimodel_delay.simulation(simulation_time=8, time_unit='days', dose_mg=[10])
mymultimodel_delay.plot_simulation(tnn, cnn, show_auc=True, show_max=True)
mymultimodel_delay.md_delay_vary_bioav_plot(simulation_time=8, time_unit='days', drug_doses=[10, 20, 30],
                                           compartment_pos=[0,1,2], figsize=(12,8))
