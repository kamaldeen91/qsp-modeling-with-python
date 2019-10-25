from ModelPlots.model_simulation_plots import single_dose_plot, multi_dose_plot, multi_dose_with_delay_plot

from ModelPlots.dose_auc_plot import single_dose_auc_plot, multi_dose_auc_plot, multi_dose_delay_auc_plot

from PharmacokineticModeling.pk_model_and_par import my_model, model_parameters

num_days = 2
num_dose = 3

interval = 3
# delay = np.zeros(num_dose - 1)
delay = [2, 0]

num_comp = 3

drug_doses = [100, 500, 600]

comp = [1] #range(num_comp)

###############

K12 = 0.7; K21 = 0.3
K13 = 0.01; K31 = 0.002

K = 0.28

par = [K12, K21, K13, K31, K]

###############

single_dose_auc_plot(my_model, model_parameters, num_comp, drug_doses, num_days, 'days', comp, 10, 15)

# (my_model, par, num_comp, drug_doses, num_days, 'days', num_dose, interval, comp)
multi_dose_auc_plot(my_model, par, num_comp, drug_doses, num_days, 'days', num_dose, interval, comp, 10)

multi_dose_delay_auc_plot(my_model, par, num_comp, drug_doses, num_days, 'days', num_dose, interval, delay, comp, 10)

single_dose_plot(my_model, model_parameters, num_comp, drug_doses,  num_days, 'days', comp)

multi_dose_plot(my_model, par, num_comp, drug_doses, num_days, 'days', num_dose, interval, comp)
#
multi_dose_with_delay_plot(my_model, par, num_comp, drug_doses, num_days, 'days', num_dose, interval, delay, comp)