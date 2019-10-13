from TwoCompartment.PK_model.pk_2C_model_simulations import two_comp_multi_dose_simulation, \
    two_comp_multi_dose_with_delay_simulation, two_comp_single_dose_simulation

import matplotlib.pyplot as plt

from plot_simulations_with_AUC import plot_multi_dose_output, plot_multi_dose_delay_output, plot_single_dose_output

num_days = 48
num_dose = 3

interval = 12
# delay = np.zeros(num_dose - 1)

delay = [5, 0]

dose_1 = [100]
# dose_2 = [100, 0, 100]

t0, C0 = two_comp_single_dose_simulation(num_days, 'hr', dose_1)
plot_single_dose_output(t0, C0, (12,6), 'concentration', 'ng/ml', show_auc = False, tS = 0, tC = 'inf', show_max = False)
#

t1, C1 = two_comp_multi_dose_simulation(num_days, 'hr', num_dose, interval, dose_1)  # [dose_1]*num_dose)
plot_multi_dose_output(t1, C1, num_dose, interval, (10,6), 'concentration', 'ng/mL', show_auc = False, show_max = True, tS=10, tC='inf')

# plt.plot(t1, C1)

t2, C2 = two_comp_multi_dose_with_delay_simulation(num_days, 'hr', num_dose, interval, dose_1, delay) #, [dose_1]*num_dose, delay)
plot_multi_dose_delay_output(t2, C2, num_dose, interval, delay, (10,6), 'concentration', 'ng/mL', show_auc = True, show_max = True, tS=10, tC='inf')
