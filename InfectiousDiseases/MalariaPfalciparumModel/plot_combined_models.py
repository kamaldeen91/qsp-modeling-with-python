import numpy as np

import matplotlib.pyplot as plt


def pop_model_output(t_df, C, d_start, pop_dynamics, pop_with_drug, show_irbc: bool=False, show_g: bool=False,
                     #save_fig: bool=False,
                     save_as: str=None):

    p_fal = 1.0 * 1e8; p_min = 1e5; t_step = 0.01

    fig, ax = plt.subplots(figsize=(12, 6))

    ###########################################################################
    ax.hlines(y=pop_dynamics['s'][d_start], xmin=0, xmax=len(t_df), color='r', linestyle='dashed', lw=3, alpha=0.2)
    ax.axvline(x=d_start, ymin=0, ymax=p_fal, color='k', ls='dashed', lw=3, alpha=0.5)
    ax.hlines(y=p_min, xmin=0, xmax=len(t_df), color='b', linestyle='dashed', lw=3, alpha=0.2)

    ############################################################################

    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(2.0)

    for axis in ['top', 'right']:
        ax.spines[axis].set_linewidth(0)

    if show_irbc == True:
        line1, = ax.plot(t_df[d_start - int(3 / t_step):], pop_dynamics['s'][0:len(t_df)][d_start - int(3 / t_step):],
                         'r-', lw=3,
                         label='iRBC Without drug')

    line2, = ax.plot(t_df[d_start:], pop_with_drug[d_start:], 'b-', lw=3,
                     label='iRBC after drug')

    if show_g == True:
        line3, = ax.plot(t_df[d_start - int(3 / t_step):], pop_dynamics['g'][0:len(t_df)][d_start - int(3 / t_step):],
                         'k--', lw=3,
                         label='Gametocytes', alpha=0.3)

    ax.set_yscale('log')
    ax.set_ylabel('Infected rbc', fontsize=24)
    ax.set_xlabel('time (hrs)', fontsize=24)

    ax.tick_params(direction='out', length=6, width=2, colors='k', labelsize=18,
                   color='k')

    ax.legend(fontsize='x-large', frameon=False)

    ########################################################################### np.ones(d_start)

    eps = np.finfo(float).eps
    conc_after_pop = np.concatenate([[eps] * d_start, C])
    conc_after_pop2 = np.ma.masked_where(((conc_after_pop >= eps) & (conc_after_pop <= 0.1)), conc_after_pop)

    ##########################################################################

    ##########################################################################
    ax_conc = ax.twinx()

    for axis in ['bottom', 'right']:
        ax_conc.spines[axis].set_linewidth(2.0)

    for axis in ['top', 'left']:
        ax_conc.spines[axis].set_linewidth(0)

    ax_conc.plot(t_df, conc_after_pop2, 'g-.', lw=4, label='Drug conc', alpha=0.2)

    ax_conc.set_ylabel('Concentration', fontsize=24, color='green', alpha=0.3)

    ax_conc.tick_params(direction='out', length=6, width=2, colors='k', labelsize=18,
                        color='k')

    ax_conc.annotate('', xy=(d_start, 0), xytext=(d_start, -0.01),
                     arrowprops=dict(facecolor='red', edgecolor='red'))

    plt.show()

    if save_as != None:

        fig.savefig(str(save_as)+'.pdf')

