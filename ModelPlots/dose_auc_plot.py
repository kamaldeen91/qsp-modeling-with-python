from PharmacokineticModeling.pk_model_simulations import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay

from pylab import *
import matplotlib.pyplot as plt

from sklearn.metrics import auc


#######################################################################################################################


def single_dose_auc_plot(model, model_parameters, number_of_compartments, drug_doses, simulation_time: any,
                  time_unit: str, comp_num, auc_start: int = 0, auc_end: any = 'inf', show_auc_value: bool = True,
                  yunit: str = 'ng/l', figsize: tuple=(8,5)):

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)

    x = []; y = []
    plt_stp = 0.1

    for i in drug_doses:
        x.append(i)
        time, conc = single_dose_simulation(model, model_parameters, number_of_compartments, simulation_time,
                                            time_unit, [i], comp_num)

        if auc_end == 'inf':
            dose_auc = round(auc(time[int(auc_start / plt_stp):], conc[int(auc_start / plt_stp):]), 2)
            y.append(dose_auc)

        else:
            dose_auc = round(auc(time[int(auc_start / plt_stp):int(float(auc_end) / plt_stp) + 1],
                    conc[int(auc_start / plt_stp):int(float(auc_end) / plt_stp) + 1]), 2)
            y.append(dose_auc)

        plot(x, y, 'ro', lw=2)

        #plt.tight_layout()
        plt.ylabel('AUC ({})'.format(yunit), fontsize=12)
        plt.xlabel('Dose ({})'.format(yunit), fontsize=12)
        plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12, color='k')

        if auc_end == 'inf':
            plt.title(r'Dose - AUC for single dose (t = {}hr - $\infty$)'.format(auc_start))

        else:
            plt.title(r'Dose - AUC for single dose (t = {} - {}hr)'.format(auc_start, auc_end))

        if show_auc_value == True:

            for j in range(len(x)):
                ax.text(x[j], y[j], y[j], fontsize=12, color='g', alpha=0.7)

    plt.show()


#######################################################################################################################

def multi_dose_auc_plot(model, model_parameters, number_of_compartments, drug_doses, simulation_time: any,
                  time_unit: str, number_of_dose, interval, comp_num, auc_start: int = 0, auc_end: any = 'inf', show_auc_value: bool = True,
                  yunit: str = 'ng/l', figsize: tuple=(8,5)):

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)

    x = []; y = []
    plt_stp = 0.1

    for i in drug_doses:
        x.append(i)
        time, conc = multi_dose_simulation(model, model_parameters, number_of_compartments, simulation_time,
                                               time_unit, number_of_dose, interval, [i], comp_num)

        if auc_end == 'inf':
            dose_auc = round(auc(time[int(auc_start / plt_stp):], conc[int(auc_start / plt_stp):]), 2)
            y.append(dose_auc)

        else:
            dose_auc = round(auc(time[int(auc_start / plt_stp):int(float(auc_end) / plt_stp) + 1],
                    conc[int(auc_start / plt_stp):int(float(auc_end) / plt_stp) + 1]), 2)
            y.append(dose_auc)

        plot(x, y, 'ro', lw=2)

        plt.ylabel('AUC ({})'.format(yunit), fontsize=12)
        plt.xlabel('Dose ({})'.format(yunit), fontsize=12)
        plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12, color='k')

        if auc_end == 'inf':
            plt.title(r'Dose - AUC for multiple dose (t = {}hr - $\infty$)'.format(auc_start))

        else:
            plt.title(r'Dose - AUC for multiple dose (t = {} - {}hr)'.format(auc_start, auc_end))

        if show_auc_value == True:

            for j in range(len(x)):
                ax.text(x[j], y[j], y[j], fontsize=12, color='g', alpha=0.7)

    plt.show()


#######################################################################################################################

def multi_dose_delay_auc_plot(model, model_parameters, number_of_compartments, drug_doses, simulation_time: any,
                  time_unit: str, number_of_dose, interval, delay, comp_num, auc_start: int = 0, auc_end: any = 'inf', show_auc_value: bool = True,
                  yunit: str = 'ng/l', figsize: tuple=(8,5)):

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)

    x = []; y = []
    plt_stp = 0.1

    for i in drug_doses:
        x.append(i)
        time, conc = multi_dose_sim_delay(model, model_parameters, number_of_compartments, simulation_time,
                                          time_unit, number_of_dose, interval, [i], delay, comp_num)

        if auc_end == 'inf':
            dose_auc = round(auc(time[int(auc_start / plt_stp):], conc[int(auc_start / plt_stp):]), 2)
            y.append(dose_auc)

        else:
            dose_auc = round(auc(time[int(auc_start / plt_stp):int(float(auc_end) / plt_stp) + 1],
                    conc[int(auc_start / plt_stp):int(float(auc_end) / plt_stp) + 1]), 2)
            y.append(dose_auc)

        plot(x, y, 'ro', lw=2)

        plt.ylabel('AUC ({})'.format(yunit), fontsize=12)
        plt.xlabel('Dose ({})'.format(yunit), fontsize=12)
        plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12, color='k')

        if auc_end == 'inf':
            plt.title(r'Dose - AUC for multiple dose with delay (t = {}hr - $\infty$)'.format(auc_start))

        else:
            plt.title(r'Dose - AUC for multiple dose with delay (t = {} - {}hr)'.format(auc_start, auc_end))

        if show_auc_value == True:

            for j in range(len(x)):
                ax.text(x[j], y[j], y[j], fontsize=12, color='g', alpha=0.7)

    plt.show()
