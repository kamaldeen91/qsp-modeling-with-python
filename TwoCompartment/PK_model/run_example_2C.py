from TwoCompartment.PK_model.pk_2C_model_simulations import SingleDose


def two_comp_model(y, t, K, K12, K21):

    # G = y[0];
    A1 = y[0]; A2 = y[1]

    # dGdt = -ka * G
    dA1dt = K21 * A2 - K12 * A1 - K * A1
    dA2dt = K12 * A1 - K21 * A2

    return [dA1dt, dA2dt]


def model_parameters():

    # ka = 0.0867; Cl = 15.5; F = 1; Vc = 368; Vd = 1060; Q = 16;
    #
    # K12 = Q / Vc; K21 = Q / Vd; K = Cl / Vc

    # F = 0.89; ka = 1.8;
    K12 = 0.47; K21 = 0.3; K = 0.28

    par = (K, K12, K21)

    return par


# print(len(two_comp_model()))

num_days = 10
num_dose = 3

interval = 12
# delay = np.zeros(num_dose - 1)

delay = [5, 0]

dose_1 = [100]
# dose_2 = [100, 0, 100]

mymodel = SingleDose(two_comp_model, model_parameters, num_days, 'hr', dose_1, [0])
t0, C0 = mymodel.simulation()

# mymodel.plot_simulation(t0, C0, show_max=True)


num_days = 10

num_comp = 2

drug_doses = [100, 500, 1000]

comp = range(num_comp)

# single_dose_plot(drug_doses, num_comp, num_days, 'days', comp)
# single_dose_plot(two_comp_model, model_parameters, drug_doses, num_comp, num_days, 'hr', comp)

mymodel.single_dose_plot(drug_doses, comp)

mymodel.model_properties(t0, C0)

# model_properties(self, time, conc)

# t0, C0 = two_comp_single_dose_simulation(num_days, 'hr', dose_1)
# plot_single_dose_output(t0, C0, (12,6), 'concentration', 'ng/ml', show_max = False, show_auc = False, auc_start = 0, auc_end = 'inf')
# #
#
# t1, C1 = two_comp_multi_dose_simulation(num_days, 'hr', num_dose, interval, dose_1)  # [dose_1]*num_dose)
# plot_multi_dose_output(t1, C1, num_dose, interval, (10,6), 'concentration', 'ng/mL', show_auc = False, show_max = True, tS=10, tC='inf')
#
# # plt.plot(t1, C1)
#
# t2, C2 = two_comp_multi_dose_with_delay_simulation(num_days, 'hr', num_dose, interval, dose_1, delay) #, [dose_1]*num_dose, delay)
# plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
