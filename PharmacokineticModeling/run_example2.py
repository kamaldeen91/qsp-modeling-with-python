from PharmacokineticModeling.pk_model_simulations import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay

from plot_simulations_with_AUC import plot_multi_dose_output, plot_multi_dose_delay_output, plot_single_dose_output

num_days = 15
num_dose = 3

interval = 24
# delay = np.zeros(num_dose - 1)
delay = [5, 0]

dose_1 = 100
dose_2 = [100, 0, 100]
num_comp = 7


###

t, C = single_dose_simulation(num_comp, num_days, dose_1)
plot_single_dose_output(t, C, (7, 5), 'ng/mL', 'central compartment', show_auc = True, tS=10, tC='inf', show_max = False)


###

t1, C1 = multi_dose_simulation(num_comp, num_days, num_dose, interval, [dose_1]*num_dose)
plot_multi_dose_output(t1, C1, num_dose, interval, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')


###

t2, C2 = multi_dose_sim_delay(num_comp, num_days, num_dose, interval, [dose_1]*num_dose, delay)
plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
