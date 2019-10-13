from PharmacokineticModeling.pk_model_simulations import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay

from plot_simulations_with_AUC import plot_multi_dose_output, plot_multi_dose_delay_output, plot_single_dose_output

num_comp = 3

###

num_days = 48
num_dose = 3

interval = 12

delay = [4, 0]

dose_mg = [100]

t0, C0 = single_dose_simulation(num_comp, num_days, 'hr', dose_mg, 0)
plot_single_dose_output(t0, C0, (12,6), 'concentration', 'ng/ml', show_auc = True, tS = 0, tC = 'inf', show_max = False)

###

t1, C1 = multi_dose_simulation(num_comp, num_days, 'hr', num_dose, interval, dose_mg, 0)
plot_multi_dose_output(t1, C1, num_dose, interval, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')


t2, C2 = multi_dose_sim_delay(num_comp, num_days, 'hr', num_dose, interval, dose_mg, delay, 0)
plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10, 6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')