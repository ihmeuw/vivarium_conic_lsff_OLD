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
    'all_causes': ['cause_specific_mortality_rate'],
    'diarrheal_diseases': DEFAULT_CAUSE_LIST,
    'lower_respiratory_infections': DEFAULT_CAUSE_LIST,
    'measles': [c for c in DEFAULT_CAUSE_LIST if c not in ['remission_rate']],
    'neonatal_sepsis_and_other_neonatal_infections': NEONATAL_CAUSE_LIST,
    'neonatal_encephalopathy_due_to_birth_asphyxia_and_trauma': NEONATAL_CAUSE_LIST,
    'hemolytic_disease_and_other_neonatal_jaundice': NEONATAL_CAUSE_LIST,
    'neural_tube_defects': NEONATAL_CAUSE_LIST,
}

NEONATAL_SEPSIS_IR_MEID=1594


