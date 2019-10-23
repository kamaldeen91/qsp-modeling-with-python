import pandas as pd

from ModelPlots.plot_simulations_with_AUC import plot_single_dose_output
from ModelPlots.model_simulation_plots import single_dose_plot

from PharmacokineticModeling.pk_model_simulations import single_dose_simulation

########################################################################################################################


class SingleDose():

    def __init__(self, model, model_parameters, number_of_compartments):
        self.model = model
        self.model_parameters = model_parameters
        self.number_of_compartments = number_of_compartments

    ###################

    def simulation(self, simulation_time: any, time_unit: str, dose_mg, compartment_pos=None):

        if compartment_pos is None:
            compartment_pos = [1]

        time, conc = single_dose_simulation(self.model, self.model_parameters, self.number_of_compartments,
                                            simulation_time, time_unit, dose_mg, compartment_pos)

        return time, conc

    ######################

    def plot_simulation(self, t, conc, figsize: tuple = (12, 6), ylabel: any = 'Concentration', yunit: any = 'ng/mL',
                        show_max: bool=False, show_auc: bool = False, auc_start: any = 0, auc_end: any = 'inf' ):

        plot_single_dose_output(t, conc, figsize, ylabel, yunit, show_max, show_auc, auc_start, auc_end)

    ######################

    def single_dose_plot(self, simulation_time, time_unit, drug_doses, compartment_pos, yunit: str = 'ng/l', figsize: tuple = (8, 5)):

        single_dose_plot(self.model, self.model_parameters, self.number_of_compartments, drug_doses, simulation_time, time_unit,
                         compartment_pos, yunit, figsize)

    ######################

    def model_properties(self, time, C, t_step: any = 0.1):

        res = pd.DataFrame([time, C], index=['Time', 'Conc']).T
        c_max = max(res['Conc'])
        t_max = round(res[res['Conc'] == c_max]['Time'], 3)
        tmax = t_max.index[0] * t_step

        return print(c_max, tmax)

    ######################
