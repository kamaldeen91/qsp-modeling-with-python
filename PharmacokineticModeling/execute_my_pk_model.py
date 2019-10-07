from PharmacokineticModeling.my_pk_model_sim import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay

from simulation_plot import plot_multi_dose_output, plot_multi_dose_delay_output, plot_single_dose_output


num_days = 15
num_dose = 5

interval = 24
# delay = np.zeros(num_dose - 1)

delay = [5, 0]

dose_1 = 100
dose_2 = [100, 0, 100]

t0, C0 = single_dose_simulation(5, num_days, [dose_1]*num_dose)

t1, C1 = multi_dose_simulation(5, num_days, num_dose, interval, [dose_1]*num_dose)

# t2, C2 = multi_dose_sim_delay(3, num_days, num_dose, interval, [dose_1]*num_dose, delay)

plot_single_dose_output(t0, C0, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')

plot_multi_dose_output(t1, C1, num_dose, interval, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')

# plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')