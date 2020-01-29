from gbd_mapping import causes, risk_factors


CLUSTER_PROJECT = 'proj_cost_effect_conic'
PROJECT_NAME = 'vivarium_conic_lsff'

LOCATIONS = ['India', 'Nigeria', 'Ethiopia']
LOCATIONS_WITH_DATA_PROBLEMS = ['India']

RISK_FACTOR_VITAMIN_A = risk_factors.vitamin_a_deficiency.name

DEFAULT_CAUSE_LIST = ['cause_specific_mortality_rate', 'excess_mortality_rate', 'disability_weight',
         'incidence_rate', 'prevalence', 'remission_rate', 'restrictions']
NEONATAL_CAUSE_LIST = ['cause_specific_mortality_rate', 'excess_mortality_rate', 'disability_weight',
         'birth_prevalence', 'prevalence', 'restrictions']

CAUSE_MEASURES = {
    causes.all_causes.name: ['cause_specific_mortality_rate'],
    causes.diarrheal_diseases.name: DEFAULT_CAUSE_LIST,
    causes.lower_respiratory_infections.name: DEFAULT_CAUSE_LIST,
    causes.measles.name: [c for c in DEFAULT_CAUSE_LIST if c not in ['remission_rate']],
    causes.neonatal_sepsis_and_other_neonatal_infections.name: NEONATAL_CAUSE_LIST,
    causes.neonatal_encephalopathy_due_to_birth_asphyxia_and_trauma.name: NEONATAL_CAUSE_LIST,
    causes.hemolytic_disease_and_other_neonatal_jaundice.name: NEONATAL_CAUSE_LIST,
    causes.neural_tube_defects.name: NEONATAL_CAUSE_LIST,
}

NEONATAL_SEPSIS_IR_MEID=1594


