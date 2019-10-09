from PharmacokineticModeling.my_pk_model_sim import single_dose_simulation, multi_dose_simulation, multi_dose_sim_delay

import matplotlib.pyplot as plt

import numpy as np
from matplotlib.pyplot import cm
from pylab import *


def plot_diff_single_dose(drug_doses, num_comp, num_days):

    n = len(drug_doses)
    color=iter(cm.brg(np.linspace(0,1,n)))

    for i in drug_doses:
        c = next(color)
        time, conc = single_dose_simulation(num_comp, num_days, i)
        plt.plot(time, conc, 'b-', lw=2, c=c, label=r'Dose = {}'.format(i))

    plt.ylabel('Concentration (ng/L)', fontsize=12)
    plt.xlabel('time (hr)', fontsize=12)

    plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                    color='k')
    plt.legend(fontsize=12)
    plt.show()


def plot_diff_dose(drug_doses, num_comp, num_days, comp_num):

    fig = plt.figure(figsize=(10, 6))

    for i in drug_doses:
        if len(comp_num) == 1:

            t0, C0 = single_dose_simulation(num_comp, num_days, i, comp_num)
            plot(t0, C0)

        else:

            for (j, k) in enumerate(comp_num):

                axes = fig.add_subplot(len(comp_num) / 2 + len(comp_num) % 2, 2, j+1, title=r'compartment {}'.format(k))

                plt.tight_layout()
                t0, C0 = single_dose_simulation(num_comp, num_days, i, k)

                axes.plot(t0, C0, lw=2)

    plt.show()


def plot_diff_multi_dose(drug_doses, num_comp, num_days, num_dose, interval):

    n = len(drug_doses)
    color=iter(cm.brg(np.linspace(0,1, n)))

    for i in drug_doses:
        c = next(color)
        time, conc = multi_dose_simulation(num_comp, num_days, num_dose, interval, [i]*num_dose)
        plt.plot(time, conc, 'b-', lw=2, c=c, label=r'Dose = {}'.format(i))

    plt.ylabel('Concentration (ng/L)', fontsize=12)
    plt.xlabel('time (hr)', fontsize=12)

    plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                    color='k')
    plt.legend(fontsize=12)
    plt.show()


def plot_diff_multi_dose_delay(drug_doses, num_comp, num_days, num_dose, interval, delay):

    n = len(drug_doses)
    color=iter(cm.brg(np.linspace(0,1, n)))

    for i in drug_doses:
        c = next(color)
        time, conc = multi_dose_sim_delay(num_comp, num_days, num_dose, interval, [i]*num_dose, delay)
        plt.plot(time, conc, 'b-', lw=2, c=c, label=r'Dose = {}'.format(i))

    plt.ylabel('Concentration (ng/L)', fontsize=12)
    plt.xlabel('time (hr)', fontsize=12)

    plt.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                    color='k')
    plt.legend(fontsize=12)
    plt.show()
