from PharmacokineticModeling.pk_model_simulations import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay
from pylab import *
import matplotlib.pyplot as plt

#######################################################################################################################


def single_dose_plot(drug_doses, num_comp, num_days, comp_num, yunit: str = 'ng/l', figsize: tuple=(8,5)):

    fig = plt.figure(figsize=figsize)

    for i in drug_doses:
        if len(comp_num) == 1:

            time, conc = single_dose_simulation(num_comp, num_days, i, comp_num)
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

                time, conc = single_dose_simulation(num_comp, num_days, i, k)

                axes.plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))
                plt.tight_layout()

                plt.ylabel('Conc (ng/L)', fontsize=12)
                plt.xlabel('time (hr)', fontsize=12)

                plt.legend(fontsize=12)

                plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                                color='k')

    plt.show()


#######################################################################################################################

def multi_dose_plot(drug_doses, num_comp, num_days, num_dose, interval, comp_num,
                    yunit: str = 'ng/l', figsize: tuple=(10,6), show_hstep: bool=False):

    fig = plt.figure(figsize=figsize)

    for i in drug_doses:

        if len(comp_num) == 1:

            time, conc = multi_dose_simulation(num_comp, num_days, num_dose, interval, [i] * num_dose, comp_num)

            plot(time, conc, lw=2, label=r'Dose = {}'.format(i))
            plt.tight_layout()
            plt.ylabel('Conc {}'.format(yunit), fontsize=12)
            plt.xlabel('time (hr)', fontsize=12)

            plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                            color='k')
            plt.legend(fontsize=12)

            if show_hstep == True:

                hr_step = np.arange(0, interval * num_dose, interval)

                for m in hr_step:
                    plt.annotate('', xy=(m, 0), xytext=(m, -0.01 * num_dose),
                                 arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

        else:

            for (j, k) in enumerate(comp_num):

                axes = fig.add_subplot(len(comp_num) / 2 + len(comp_num) % 2, 2, j+1, title=r'compartment {}'.format(k))

                plt.tight_layout()
                time, conc = multi_dose_simulation(num_comp, num_days, num_dose, interval, [i] * num_dose, k)

                axes.plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))

                plt.ylabel('Conc {}'.format(yunit), fontsize=12)
                plt.xlabel('time (hr)', fontsize=12)

                plt.legend(fontsize=12)

                plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                                color='k')

                if show_hstep == True:

                    hr_step = np.arange(0, interval * num_dose, interval)

                    for m in hr_step:
                        plt.annotate('', xy=(m, 0), xytext=(m, -0.01 * num_dose),
                                     arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

    plt.show()


#######################################################################################################################

def multi_dose_with_delay_plot(drug_doses, num_comp, num_days, num_dose, interval, delay, comp_num,
                               yunit: str = 'ng/l', figsize: tuple=(10,6), show_hstep: bool=False):

    fig = plt.figure(figsize=figsize)

    for i in drug_doses:
        if len(comp_num) == 1:

            time, conc = multi_dose_sim_delay(num_comp, num_days, num_dose, interval, [i] * num_dose, delay, comp_num)
            plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))
            plt.tight_layout()
            plt.ylabel('Conc {}'.format(yunit), fontsize=12)
            plt.xlabel('time (hr)', fontsize=12)

            plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                            color='k')
            plt.legend(fontsize=12)

            if show_hstep == True:

                hr_step = np.arange(0, interval * num_dose, interval)

                for m in range(len(hr_step)):
                    ndelay = np.concatenate([[0], delay])

                    plt.annotate('', xy=(hr_step[m] + ndelay[m], 0), xytext=(hr_step[m] + ndelay[m], -0.01 * num_dose),
                                arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

        else:

            for (j, k) in enumerate(comp_num):

                axes = fig.add_subplot(len(comp_num) / 2 + len(comp_num) % 2, 2, j+1, title=r'compartment {}'.format(k))

                plt.tight_layout()
                time, conc = multi_dose_sim_delay(num_comp, num_days, num_dose, interval, [i] * num_dose, delay, k)

                axes.plot(time, conc, lw=2, label=r'Dose = {} {}'.format(i, yunit))

                plt.ylabel('Conc {}'.format(yunit), fontsize=12)
                plt.xlabel('time (hr)', fontsize=12)

                plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                                color='k')
                plt.legend(fontsize=12)

                if show_hstep == True:
                    hr_step = np.arange(0, interval * num_dose, interval)

                    for m in range(len(hr_step)):
                        ndelay = np.concatenate([[0], delay])

                        plt.annotate('', xy=(hr_step[m] + ndelay[m], 0), xytext=(hr_step[m] + ndelay[m], -0.01 * num_dose),
                                     arrowprops=dict(facecolor='red', edgecolor='red', alpha=0.2))

    plt.show()
