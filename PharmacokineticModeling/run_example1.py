from ModelPlots.model_simulation_plots import single_dose_plot, multi_dose_plot, multi_dose_with_delay_plot
from PharmacokineticModeling.pk_model_and_par import my_model, model_parameters

num_days = 2
num_dose = 3

interval = 3
# delay = np.zeros(num_dose - 1)
delay = [2, 0]

num_comp = 3

drug_doses = [100, 500, 1000]

comp = [1] #range(num_comp)

single_dose_plot(my_model, model_parameters, num_comp, drug_doses,  num_days, 'days', comp)

multi_dose_plot(my_model, model_parameters, num_comp, drug_doses, num_days, 'days', num_dose, interval, comp)
#
multi_dose_with_delay_plot(my_model, model_parameters, num_comp, drug_doses, num_days, 'days', num_dose, interval, delay, comp)