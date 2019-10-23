from PharmacokineticModeling.pk_model_sim_with_vary_F import multi_dose_delay_simulation_vary_bioav, multi_dose_simulation_vary_bioav
from ModelPlots.plot_simulations_with_AUC import plot_single_dose_output
import matplotlib.pyplot as plt

from PharmacokineticModeling.pk_model_and_par import two_c_model, model_par_no_F
# ka = 0.17; Cl = 15.5; Vc = 368;
#
# Vd = 1060; Q = 16;
#
# K12 = Q / Vc;
# K21 = Q / Vd;
# K = Cl / Vc;
#
# par_no_F = [ka, K, K12, K21]


t1, C1 = multi_dose_delay_simulation_vary_bioav(two_c_model, model_par_no_F, 3, 8, 'days', 4, 24, [10], [0, 0, 0],
                                                [1, 0.51, 0.41, 0.6], [1])

t2, C2 = multi_dose_delay_simulation_vary_bioav(two_c_model, model_par_no_F, 3, 8, 'days', 4, 24, [10], [2, 4, 4],
                                                [1, 0.51, 0.41, 0.6], [1])

plot_single_dose_output(t1, C1, (12,6), 'concentration', 'ng/ml', show_auc = True, auc_start = 0, auc_end = 'inf', show_max = True)

# par = PK_mul_F(8, 4, 13, 1000, [0, 11, 0], [1,0.8,1,1])

plt.figure(figsize = (8, 6))

plt.plot(t1, C1, 'b-', lw=3, label='Varying F')
plt.plot(t2, C2, 'r-.', lw=3, label='Varying F with delay')


plt.ylabel('Concentration (ng/L)', fontsize=12)
plt.xlabel('time (hr)', fontsize=12)

plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
               color='k')

plt.legend(fontsize='x-large')

plt.show()

######

t3, C3 = multi_dose_simulation_vary_bioav(two_c_model, model_par_no_F, 3, 8, 'days', 4, 24, [10], [1, 0.51, 0.41, 0.6], [1])

plot_single_dose_output(t3, C3, (12,6), 'concentration', 'ng/ml', show_auc = True, auc_start = 0, auc_end = 'inf', show_max = True)

plt.figure(figsize = (8, 6))

plt.plot(t3, C3, 'b-', lw=3, label='Varying F')

plt.ylabel('Concentration (ng/L)', fontsize=12)
plt.xlabel('time (hr)', fontsize=12)

plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
               color='k')

plt.legend(fontsize='x-large')

plt.show()
# res = pd.DataFrame([C4], index=['Conc']).T
#
# c_max = max(res['Conc'])
# t_max = int(res[res['Conc'] == c_max].index[0]*0.01)

# t_max, c_max