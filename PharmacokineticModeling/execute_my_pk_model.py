from PharmacokineticModeling.my_pk_model_sim import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay

from simulation_plot import plot_multi_dose_output, plot_multi_dose_delay_output, plot_single_dose_output

from simulation_plot_diff_dose import plot_diff_single_dose, plot_diff_multi_dose, plot_diff_multi_dose_delay

num_days = 15
num_dose = 3

interval = 24
# delay = np.zeros(num_dose - 1)
delay = [5, 0]

dose_1 = 100
dose_2 = [100, 0, 100]
num_comp = 5


###

t0, C0 = single_dose_simulation(num_comp, num_days, dose_1)
plot_single_dose_output(t0, C0, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
drug_doses = [100, 200]
plot_diff_single_dose(drug_doses, num_comp, num_days)


###

t1, C1 = multi_dose_simulation(num_comp, num_days, num_dose, interval, [dose_1]*num_dose)
plot_multi_dose_output(t1, C1, num_dose, interval, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
drug_doses = [100, 200]
plot_diff_multi_dose(drug_doses, num_comp, num_days, num_dose, interval)


###

t2, C2 = multi_dose_sim_delay(num_comp, num_days, num_dose, interval, [dose_1]*num_dose, delay)
plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
drug_doses = [100, 200]
plot_diff_multi_dose_delay(drug_doses, num_comp, num_days, num_dose, interval, delay)
