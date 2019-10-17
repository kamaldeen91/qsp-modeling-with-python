from PharmacokineticModeling.pk_model_simulations import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay
from pylab import *
import matplotlib.pyplot as plt


#######################################################################################################################

def single_dose_plot(model, model_parameters, number_of_compartments, drug_doses, simulation_time: any, time_unit: str, comp_num, yunit: str = 'ng/l', figsize: tuple=(8,5)):

    fig = plt.figure(figsize=figsize)

    for i in drug_doses:

        if len(comp_num) == 1:

            time, conc = single_dose_simulation(model, model_parameters, number_of_compartments, simulation_time,
                                                time_unit, [i], comp_num)
            plot(time, conc, lw = 2, label=r'Dose = {}'.format(i))

            plt.tight_layout()
            plt.ylabel('Conc {}'.format(yunit), fontsize=12)
            plt.xlabel('time (hr)', fontsize=12)

            plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                            color='k')
            plt.legend(fontsize=12)

        else:

            for (j, k) in enumerate(comp_num):

                axes = fig.add_subplot(len(comp_num) / 2 + len(comp_num) % 2, 2, j+1, title=r'compartment {}'.format(k))

                time, conc = single_dose_simulation(model, model_parameters, number_of_compartments, simulation_time, time_unit, [i], [k])

                axes.plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))
                plt.tight_layout()

                plt.ylabel('Conc (ng/L)', fontsize=12)
                plt.xlabel('time (hr)', fontsize=12)

                plt.legend(fontsize=12)

                plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                                color='k')

    plt.show()


#######################################################################################################################

def multi_dose_plot(model, model_parameters, number_of_compartments, drug_doses, simulation_time: any, time_unit: str,
                    number_of_dose, interval, comp_num, yunit: str = 'ng/l', figsize: tuple=(10,6), show_hstep: bool=False):

    fig = plt.figure(figsize=figsize)

    for i in drug_doses:

        if len(comp_num) == 1:

            time, conc = multi_dose_simulation(model, model_parameters, number_of_compartments, simulation_time, time_unit, number_of_dose, interval, [i], comp_num)

            plot(time, conc, lw=2, label=r'Dose = {}'.format(i))
            plt.tight_layout()
            plt.ylabel('Conc {}'.format(yunit), fontsize=12)
            plt.xlabel('time (hr)', fontsize=12)

            plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                            color='k')
            plt.legend(fontsize=12)

            if show_hstep == True:

                hr_step = np.arange(0, interval * number_of_dose, interval)

                for m in hr_step:
                    plt.annotate('', xy=(m, 0), xytext=(m, -0.01 * number_of_dose),
                                 arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

        else:

            for (j, k) in enumerate(comp_num):

                axes = fig.add_subplot(len(comp_num) / 2 + len(comp_num) % 2, 2, j+1, title=r'compartment {}'.format(k))

                plt.tight_layout()

                time, conc = multi_dose_simulation(model, model_parameters, number_of_compartments, simulation_time, time_unit, number_of_dose, interval, [i], [k])

                axes.plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))

                plt.ylabel('Conc {}'.format(yunit), fontsize=12)
                plt.xlabel('time (hr)', fontsize=12)

                plt.legend(fontsize=12)

                plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                                color='k')

                if show_hstep == True:

                    hr_step = np.arange(0, interval * number_of_dose, interval)

                    for m in hr_step:
                        plt.annotate('', xy=(m, 0), xytext=(m, -0.01 * number_of_dose),
                                     arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

    plt.show()


#######################################################################################################################

def multi_dose_with_delay_plot(model, model_parameters, number_of_compartments, drug_doses, simulation_time: any, time_unit: str, number_of_dose, interval, delay, comp_num,
                               yunit: str = 'ng/l', figsize: tuple=(10,6), show_hstep: bool=False):

    fig = plt.figure(figsize=figsize)

    for i in drug_doses:

        if len(comp_num) == 1:

            time, conc = multi_dose_sim_delay(model, model_parameters, number_of_compartments, simulation_time,
                                              time_unit, number_of_dose, interval, [i], delay, comp_num)

            plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))
            plt.tight_layout()
            plt.ylabel('Conc {}'.format(yunit), fontsize=12)
            plt.xlabel('time (hr)', fontsize=12)

            plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12, color='k')
            plt.legend(fontsize=12)

            if show_hstep == True:

                hr_step = np.arange(0, interval * number_of_dose, interval)

                for m in range(len(hr_step)):
                    ndelay = np.concatenate([[0], delay])

                    plt.annotate('', xy=(hr_step[m] + ndelay[m], 0), xytext=(hr_step[m] + ndelay[m], -0.01 * number_of_dose),
                                arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

        else:

            for (j, k) in enumerate(comp_num):

                axes = fig.add_subplot(len(comp_num) / 2 + len(comp_num) % 2, 2, j+1, title=r'compartment {}'.format(k))

                plt.tight_layout()
                time, conc = multi_dose_sim_delay(model, model_parameters, number_of_compartments, simulation_time,
                                                  time_unit, number_of_dose, interval, [i], delay, [k])

                axes.plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))

                plt.ylabel('Conc {}'.format(yunit), fontsize=12)
                plt.xlabel('time (hr)', fontsize=12)

                plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                                color='k')
                plt.legend(fontsize=12)

                if show_hstep == True:
                    hr_step = np.arange(0, interval * number_of_dose, interval)

                    for m in range(len(hr_step)):
                        ndelay = np.concatenate([[0], delay])

                        plt.annotate('', xy=(hr_step[m] + ndelay[m], 0), xytext=(hr_step[m] + ndelay[m], -0.01 * number_of_dose),
                                     arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

    plt.show()
