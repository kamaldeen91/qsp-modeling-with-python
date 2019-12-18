import pandas as pd
import numpy as np
from InfectiousDiseases.MalariaPfalciparumModel.within_host_models import pf_model

from InfectiousDiseases.MalariaPfalciparumModel.integrated_models import pop_pkpd

from InfectiousDiseases.MalariaPfalciparumModel.plot_combined_models import pop_model_output
########################################################################################################################


class WH_PKPD():
    def __init__(self, PK_time, PK_concentration, mus, PD_kappa, PD_EC50, PD_n, pop_dynamics, mdl: any = 1*1e8):

        self.PK_time = PK_time
        self.PK_concentration = PK_concentration
        self.PD_kappa = PD_kappa
        self.PD_EC50 = PD_EC50
        self.PD_n = PD_n
        self.mus = mus
        self.pop_dynamics = pop_dynamics

        self.mdl = mdl

    #################################################################

    def pharmacodynamics(self):

        conc_res = pd.DataFrame([self.PK_time, self.PK_concentration], index=['Time', 'Conc']).T
        conc_res['mus'] = self.mus + ((self.PD_kappa - 1) * self.mus * conc_res['Conc'] ** self.PD_n / (self.PD_EC50 ** self.PD_n + conc_res['Conc'] ** self.PD_n))

        return conc_res

    def plot_model(self, show_irbc: bool = True, show_g: bool = False, save_as: str = None):

        self.t_df, self.pop_with_drug, self.drug_start = pop_pkpd(self.PD_kappa, self.PD_EC50, self.PD_n, self.PK_time,
                                                                  self.PK_concentration, self.mus, self.pop_dynamics)

        pop_model_output(self.t_df, self.PK_concentration, self.drug_start, self.pop_dynamics, self.pop_with_drug,
                         show_irbc, show_g, save_as)

    ###################################################################

    def parasite_reduction_ratio(self):

        max_par_pos = np.argmax(self.pop_with_drug[self.drug_start:])

        num_par_before_cl = self.pop_with_drug[self.drug_start + max_par_pos]

        num_par_after_cl_48 = self.pop_with_drug[self.drug_start + max_par_pos + 480]

        PPT = num_par_before_cl / num_par_after_cl_48

        return print(r'Parasite reduction ratio = {}'.format(PPT))

    def parasite_clearance_time(self):
        i = 0
        count_pct = 0

        while i < len(self.pop_with_drug[self.drug_start:]):

            if self.pop_with_drug[self.drug_start+10:][i] >= self.mdl:
                count_pct = count_pct + 1
            else:
                break

            i += 1

        self.PCT = count_pct

        return print(r'Parasite clearance time = {} {}'.format(self.PCT / 10, 'hr'))

    def recrudescence(self, end: any=None):

        if end == None:
            if any(k >= self.mdl for k in self.pop_with_drug[self.drug_start + self.PCT:]):
                j = 0
                count_rec = 0
                while j < len(self.pop_with_drug[self.drug_start + self.PCT:]):
                    if self.pop_with_drug[self.drug_start + self.PCT:][j] < self.mdl:
                        count_rec = count_rec + 1
                    else:
                        break
                    j += 1
                print(r'Recrudescent time = {} {}'.format(count_rec / 10, 'hr'))
            else:
                print('no recrudescence')

        else:
            start = self.drug_start + self.PCT
            end = int(start + end/0.1)
            if any(k >= self.mdl for k in self.pop_with_drug[start: end]):
                j = 0
                count_rec = 0
                while j < len(self.pop_with_drug[start: end]):
                    if self.pop_with_drug[start: end][j] < self.mdl:
                        count_rec = count_rec + 1
                    else:
                        break
                    j += 1
                print(r'Recrudescent time = {} {}'.format(count_rec / 10, 'hr'))
            else:
                print('no recrudescence')
