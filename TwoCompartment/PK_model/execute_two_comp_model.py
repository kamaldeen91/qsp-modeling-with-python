from TwoCompartment.PK_model.oral_dose_simulations import two_comp_multi_dose_simulation, two_comp_multi_dose_sim_delay

from simulation_plot import plot_multi_dose_output, plot_multi_dose_delay_output

num_days = 10
num_dose = 3

interval = 24
# delay = np.zeros(num_dose - 1)

delay = [5, 0]

dose_1 = 100
dose_2 = [100, 0, 100]

t1, C1 = two_comp_multi_dose_simulation(num_days, num_dose, interval, [dose_1]*num_dose)

t2, C2 = two_comp_multi_dose_sim_delay(num_days, num_dose, interval, [dose_1]*num_dose, delay)

plot_multi_dose_output(t1, C1, num_dose, interval, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')

plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
