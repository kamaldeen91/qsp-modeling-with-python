from OneCompartment.pk_1C_model_simulations import one_comp_single_dose_simulation, one_comp_multi_dose_simulation, one_comp_multi_dose_sim_delay

from plot_simulations_with_AUC import plot_single_dose_output, plot_multi_dose_output, plot_multi_dose_delay_output

num_days = 10
num_dose = 3

interval = 24
# delay = np.zeros(num_dose - 1)

delay = [5, 0]

dose_1 = 100
dose_2 = [100, 0, 100]

t0, C0 = one_comp_single_dose_simulation(num_days, [dose_1]*num_dose)
plot_single_dose_output(t0, C0, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')

t1, C1 = one_comp_multi_dose_simulation(num_days, num_dose, interval, [dose_1]*num_dose)
plot_multi_dose_output(t1, C1, num_dose, interval, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')

t2, C2 = one_comp_multi_dose_sim_delay(num_days, num_dose, interval, [dose_1]*num_dose, delay)
plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')

t2, C2 = one_comp_multi_dose_simulation(num_days, num_dose, interval, dose_2)
plot_multi_dose_output(t2, C2, num_dose, interval, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
