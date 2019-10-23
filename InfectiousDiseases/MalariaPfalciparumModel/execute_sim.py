from InfectiousDiseases.MalariaPfalciparumModel.within_host_models import pf_dynamics_with_imm

from TwoCompartment.PK_model.pk_2C_model_simulations import two_comp_single_dose_simulation, two_comp_multi_dose_simulation, two_comp_multi_dose_with_delay_simulation
from InfectiousDiseases.MalariaPfalciparumModel.integrated_models import pop_pkpd
from InfectiousDiseases.MalariaPfalciparumModel.simulation_plot import pop_pk_output

from pqsp.pqsp_single_dose_simulations import SingleDose
from pqsp.pqsp_multi_dose_simulations import MultipleDose
from pqsp.pqsp_multi_dose_delay_simulations import MultipleDoseDelay

from PharmacokineticModeling.pk_model_and_par import my_model, model_parameters

pop_df = pf_dynamics_with_imm(10000)

# tc, C = two_comp_multi_dose_with_delay_simulation(40, 3, 24, [1000, 1000, 1000], [5, 0])

# tc, C = two_comp_single_dose_simulation(40, [1000, 1000, 1000])

mymodel = SingleDose(my_model, model_parameters, number_of_compartments=3)
tc, C = mymodel.simulation(simulation_time=50, time_unit='days', dose_mg=[1000], compartment_pos=[1])

mus = 0.5/24

t_df, dynamics_with_drug, d_start = pop_pkpd(10.5, 100, tc, C, mus, pop_df)

pop_pk_output(t_df, C, d_start, pop_df, dynamics_with_drug, show_irbc=True, show_g=False)