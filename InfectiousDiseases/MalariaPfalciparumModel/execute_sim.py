from InfectiousDiseases.MalariaPfalciparumModel.within_host_models import pf_dynamics_with_imm

from TwoCompartment.PK_model.oral_dose_simulations import two_comp_single_dose_simulation, two_comp_multi_dose_simulation, two_comp_multi_dose_sim_delay

from InfectiousDiseases.MalariaPfalciparumModel.integrated_models import pop_pkpd

from InfectiousDiseases.MalariaPfalciparumModel.simulation_plot import pop_pk_output


pop_df = pf_dynamics_with_imm(10000)

# tc, C = pk_multi_dose_sim_delay(40, 3, 24, [1000, 1000, 1000], [5, 0])

tc, C = two_comp_single_dose_simulation(40, [1000, 1000, 1000])

mus = 0.5/24

t_df, dynamics_with_drug, d_start = pop_pkpd(1.5, 10, tc, C, mus, pop_df)

pop_pk_output(t_df, C, d_start, pop_df, dynamics_with_drug, show_irbc=True, show_g=False)