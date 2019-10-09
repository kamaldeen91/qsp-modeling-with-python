from model_simulation_plots import single_dose_plot, multi_dose_plot, multi_dose_with_delay_plot

num_days = 15
num_dose = 3

interval = 24
# delay = np.zeros(num_dose - 1)
delay = [5, 0]

dose_1 = 100
dose_2 = [100, 0, 100]
num_comp = 7

drug_doses = [200, 400]

comp = range(num_comp)
single_dose_plot(drug_doses, num_comp, num_days, comp)

multi_dose_plot(drug_doses, num_comp, num_days, num_dose, interval, comp)

multi_dose_with_delay_plot(drug_doses, num_comp, num_days, num_dose, interval, delay, comp)