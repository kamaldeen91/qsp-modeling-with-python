from model_simulation_plots import single_dose_plot, multi_dose_plot, multi_dose_with_delay_plot

num_days = 1
num_dose = 3

interval = 3
# delay = np.zeros(num_dose - 1)
delay = [2, 0]

num_comp = 3

drug_doses = [100, 500, 1000]

comp = range(num_comp)

single_dose_plot(drug_doses, num_comp, num_days, 'day', comp)

multi_dose_plot(drug_doses, num_comp, num_days, 'day', num_dose, interval, comp)

multi_dose_with_delay_plot(drug_doses, num_comp, num_days, 'day', num_dose, interval, delay, comp)