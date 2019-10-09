import numpy as np
import pandas as pd

from sklearn.metrics import auc

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_multi_dose_delay_output(time, C, num_dose, interval, delay, figsize: tuple=(12,6),
                ylabel: str = 'concentration', yunit: str = 'ng/ml', tS: int = 0,
                tC: any = 'inf', show_auc: bool = False, show_max: bool = False, **kwargs):

    res = pd.DataFrame([time, C], index=['Time', 'Conc']).T

    c_max = max(res['Conc'])
    t_max = round(res[res['Conc'] == c_max]['Time'], 3)

    plt_stp = 0.1

    tmax = t_max.index[0] * plt_stp

    fig = plt.figure(figsize=figsize)

    ax = fig.add_subplot(111)

    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(2.0)

    for axis in ['top', 'right']:
        ax.spines[axis].set_linewidth(0)

    ax.plot(time, C, 'k-', lw=2)

    ax.set_ylabel(r'{} ({})'.format(ylabel, yunit), fontsize=16)
    ax.set_xlabel('time (hr)', fontsize=16)
    ax.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                   color='k')

    if show_max == True:

        ax.axvline(x=tmax, ymin=0, ymax=1.5, color='k', ls='dashed', lw=3, alpha=0.4)
        ax.hlines(y=c_max, xmin=0, xmax=tmax + 20, color='k', linestyle='dashed', lw=3, alpha=0.3)

        ax.text(tmax + 20, c_max, r'{} = {} {}'.format('C$_{max}$', round(c_max, 2), yunit), fontsize=12, color='r',
                alpha=0.7)
        ax.text(tmax - 2, c_max + 0.08 * c_max, r'{} = {} hr'.format('t$_{max}$', round(tmax, 2)), fontsize=12, color='r',
                alpha=0.7)

    tick_spacing = interval

    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    if show_auc == True:

        if tC == 'inf':
            plt.fill_between(time[int(tS / plt_stp):], C[int(tS / plt_stp):], step="pre", color='k', alpha=0.1)

            ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{t_0-\infty}$', round(
                auc(time[int(tS / plt_stp):], C[int(tS / plt_stp):]), 2), yunit),
                    horizontalalignment='center',
                    verticalalignment='center', transform=ax.transAxes,
                    fontsize=12, color='r', alpha=0.5)

        else:

            plt.fill_between(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1],
                             step="pre", color='k', alpha=0.1)

            if tS != 0:

                ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{t_0-t}$', round(
                    auc(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1]), 2), yunit),
                        horizontalalignment='center',
                        verticalalignment='center', transform=ax.transAxes,
                        fontsize=12, color='r', alpha=0.5)


            else:
                ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{0-t}$', round(
                    auc(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1]), 2), yunit),
                        horizontalalignment='center',
                        verticalalignment='center', transform=ax.transAxes,
                        fontsize=12, color='r', alpha=0.5)

    hr_step = np.arange(0, interval * num_dose, interval)

    for i in range(len(hr_step)):
        ndelay = np.concatenate([[0], delay])

        ax.annotate('', xy=(hr_step[i] + ndelay[i], 0), xytext=(hr_step[i] + ndelay[i], -0.01 * num_dose),
                    arrowprops=dict(facecolor='red', edgecolor='red'))

    plt.show()


def plot_multi_dose_output(time, C, num_dose, interval, figsize: tuple=(12,6),
                ylabel: str = 'concentration', yunit: str = 'ng/ml', tS: int = 0,
                tC: any = 'inf', show_auc: bool = False, show_max: bool = False, **kwargs):

    res = pd.DataFrame([time, C], index=['Time', 'Conc']).T

    c_max = max(res['Conc'])
    t_max = round(res[res['Conc'] == c_max]['Time'], 3)

    plt_stp = 0.1

    tmax = t_max.index[0] * plt_stp

    fig = plt.figure(figsize=figsize)

    ax = fig.add_subplot(111)

    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(2.0)

    for axis in ['top', 'right']:
        ax.spines[axis].set_linewidth(0)

    ax.plot(time, C, 'k-', lw=2)

    ax.set_ylabel(r'{} ({})'.format(ylabel, yunit), fontsize=16)
    ax.set_xlabel('time (hr)', fontsize=16)
    ax.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                   color='k')

    if show_max == True:

        ax.axvline(x=tmax, ymin=0, ymax=1.5, color='k', ls='dashed', lw=3, alpha=0.4)
        ax.hlines(y=c_max, xmin=0, xmax=tmax + 20, color='k', linestyle='dashed', lw=3, alpha=0.3)

        ax.text(tmax + 20, c_max, r'{} = {} {}'.format('C$_{max}$', round(c_max, 2), yunit), fontsize=12, color='r',
                alpha=0.7)
        ax.text(tmax - 2, c_max + 0.08 * c_max, r'{} = {} hr'.format('t$_{max}$', round(tmax, 2)), fontsize=12, color='r',
                alpha=0.7)

    tick_spacing = interval

    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    if show_auc == True:

        if tC == 'inf':
            plt.fill_between(time[int(tS / plt_stp):], C[int(tS / plt_stp):], step="pre", color='k', alpha=0.1)

            ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{t_0-\infty}$', round(
                auc(time[int(tS / plt_stp):], C[int(tS / plt_stp):]), 2), yunit),
                    horizontalalignment='center',
                    verticalalignment='center', transform=ax.transAxes,
                    fontsize=12, color='r', alpha=0.5)

        else:

            plt.fill_between(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1],
                             step="pre", color='k', alpha=0.1)

            if tS != 0:

                ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{t_0-t}$', round(
                    auc(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1]), 2), yunit),
                        horizontalalignment='center',
                        verticalalignment='center', transform=ax.transAxes,
                        fontsize=12, color='r', alpha=0.5)

            else:
                ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{0-t}$', round(
                    auc(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1]), 2), yunit),
                        horizontalalignment='center',
                        verticalalignment='center', transform=ax.transAxes,
                        fontsize=12, color='r', alpha=0.5)

    hr_step = np.arange(0, interval * num_dose, interval)

    for i in hr_step:

        ax.annotate('', xy=(i, 0), xytext=(i, -0.01 * num_dose),
                    arrowprops=dict(facecolor='red', edgecolor='red'))

    plt.show()


def plot_single_dose_output(time, C, figsize: tuple=(12,6), yunit: str = 'ng/ml', title: any = 'Central',
                            show_auc: bool = False, tS: int = 0, tC: any = 'inf', show_max: bool = False):

    res = pd.DataFrame([time, C], index=['Time', 'Conc']).T

    c_max = max(res['Conc'])
    t_max = round(res[res['Conc'] == c_max]['Time'], 3)

    plt_stp = 0.1

    tmax = t_max.index[0] * plt_stp

    fig = plt.figure(figsize=figsize)

    ax = fig.add_subplot(1, 1, 1)

    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(2.0)

    for axis in ['top', 'right']:
        ax.spines[axis].set_linewidth(0)

    ax.plot(time, C, 'k-', lw=2)

    ax.set_title(title)

    ax.set_ylabel(r'Concentration ({})'.format(yunit), fontsize=16)
    ax.set_xlabel('time (hr)', fontsize=16)
    ax.tick_params(direction='out', length=6, width=2, colors='k', labelsize=12,
                   color='k')

    if show_max == True:

        ax.axvline(x=tmax, ymin=0, ymax=1.5, color='k', ls='dashed', lw=3, alpha=0.4)
        ax.hlines(y=c_max, xmin=0, xmax=tmax + 20, color='k', linestyle='dashed', lw=3, alpha=0.3)

        ax.text(tmax + 20, c_max, r'{} = {} {}'.format('C$_{max}$', round(c_max, 2), yunit), fontsize=12, color='r',
                alpha=0.7)
        ax.text(tmax - 2, c_max + 0.08 * c_max, r'{} = {} hr'.format('t$_{max}$', round(tmax, 2)), fontsize=12, color='r',
                alpha=0.7)

    if show_auc == True:

        if tC == 'inf':
            plt.fill_between(time[int(tS / plt_stp):], C[int(tS / plt_stp):], step="pre", color='k', alpha=0.1)

            ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{t_0-\infty}$', round(
                auc(time[int(tS / plt_stp):], C[int(tS / plt_stp):]), 2), yunit),
                    horizontalalignment='center',
                    verticalalignment='center', transform=ax.transAxes,
                    fontsize=12, color='r', alpha=0.5)

        else:

            plt.fill_between(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1],
                             step="pre", color='k', alpha=0.1)

            if tS != 0:

                ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{t_0-t}$', round(
                    auc(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1]), 2), yunit),
                        horizontalalignment='center',
                        verticalalignment='center', transform=ax.transAxes,
                        fontsize=12, color='r', alpha=0.5)

            else:
                ax.text(0.2, 0.15, r'{} = {} {}'.format('AUC$_{0-t}$', round(
                    auc(time[int(tS / plt_stp):int(float(tC) / plt_stp) + 1], C[int(tS / plt_stp):int(float(tC) / plt_stp) + 1]), 2), yunit),
                        horizontalalignment='center',
                        verticalalignment='center', transform=ax.transAxes,
                        fontsize=12, color='r', alpha=0.5)

    plt.show()

