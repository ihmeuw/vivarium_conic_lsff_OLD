from gbd_mapping import causes, risk_factors


CLUSTER_PROJECT = 'proj_cost_effect_conic'
PROJECT_NAME = 'vivarium_conic_lsff'

LOCATIONS = ['India', 'Nigeria', 'Ethiopia']
LOCATIONS_WITH_DATA_PROBLEMS = ['India']

CAUSE_MEASLES = causes.measles.name
CAUSE_DIARRHEAL = causes.diarrheal_diseases.name
CAUSE_LOWER_RESPIRATORY_INFECTIONS = causes.lower_respiratory_infections.name
CAUSE_NEONATAL_NEURAL_TUBE_DEFECTS = causes.neural_tube_defects.name
CAUSE_NEONATAL_ENCEPHALOPATHY = causes.neonatal_encephalopathy_due_to_birth_asphyxia_and_trauma.name
CAUSE_NEONATAL_SEPSIS = causes.neonatal_sepsis_and_other_neonatal_infections.name
CAUSE_NEONATAL_JAUNDICE = causes.hemolytic_disease_and_other_neonatal_jaundice.name

RISK_FACTOR_VITAMIN_A = risk_factors.vitamin_a_deficiency.name


CAUSES_WITH_INCIDENCE = [
    CAUSE_MEASLES,
    CAUSE_DIARRHEAL,
    CAUSE_LOWER_RESPIRATORY_INFECTIONS,
]

CAUSES_NEONATAL = [
    CAUSE_NEONATAL_NEURAL_TUBE_DEFECTS,
    CAUSE_NEONATAL_ENCEPHALOPATHY,
    CAUSE_NEONATAL_SEPSIS,
    CAUSE_NEONATAL_JAUNDICE,
]


# ========================================================================
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
    #'neonatal_preterm_birth':[c for c in NEONATAL_CAUSE_LIST if c not in ['birth_prevalence', 'prevalence']]
}



