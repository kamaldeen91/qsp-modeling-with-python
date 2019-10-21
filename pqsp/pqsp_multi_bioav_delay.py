import numpy as np

from plot_simulations_with_AUC import plot_multi_dose_delay_output
from model_simulation_plots import multi_dose_vary_bioav_plot, mutli_dose_delay_vary_bioav_plot

from PharmacokineticModeling.pk_model_sim_with_vary_F import multi_dose_delay_simulation_vary_bioav

########################################################################################################################


class MultipleDoseVaryBioavDelay():
    def __init__(self, model, parameters_no_bioav, number_of_compartments, number_of_dose, interval, delay=None, bioav=None):

        self.model = model
        self.parameters_no_bioav = parameters_no_bioav
        self.number_of_compartments = number_of_compartments
        self.number_of_dose = number_of_dose
        self.interval = interval

        if delay is None:
            delay = np.zeros(number_of_dose - 1)

        self.delay = delay

        if bioav is None:
            bioav = [1]*self.number_of_dose

        self.bioav = bioav

    ######################

    def simulation(self, simulation_time: any, time_unit: str, dose_mg, compartment_pos=None):

        if compartment_pos is None:
            compartment_pos = [1]

        time, conc =  multi_dose_delay_simulation_vary_bioav(self.model, self.parameters_no_bioav, self.number_of_compartments,
                                                             simulation_time, time_unit, self.number_of_dose, self.interval,
                                                             dose_mg, self.delay, self.bioav, compartment_pos)
        return time, conc

    ######################

    def plot_simulation(self, time, conc, figsize: tuple = (12, 6), ylabel: str = 'concentration', yunit: str = 'ng/ml',
                        auc_start: int = 0, auc_end: any = 'inf', show_auc: bool = False, show_max: bool = False):

        plot_multi_dose_delay_output(time, conc, self.number_of_dose, self.interval, self.delay, figsize,
                                     ylabel, yunit, show_max,show_auc, auc_start, auc_end)

    ######################

    def md_delay_vary_bioav_plot(self, simulation_time, time_unit: str, drug_doses, compartment_pos,
                        yunit: str = 'ng/l', figsize: tuple = (10, 6), show_hstep: bool = False):

        mutli_dose_delay_vary_bioav_plot(self.model, self.parameters_no_bioav, self.number_of_compartments, drug_doses,
                                         simulation_time, time_unit, self.number_of_dose, self.interval, self.delay,
                                         self.bioav, compartment_pos, yunit, figsize, show_hstep)

    ######################
