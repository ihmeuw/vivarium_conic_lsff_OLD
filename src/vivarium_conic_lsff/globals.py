from gbd_mapping import causes


CLUSTER_PROJECT = 'proj_cost_effect_conic'
PROJECT_NAME = 'vivarium_conic_lsff'

LOCATIONS = ['India', 'Nigeria', 'Ethiopia']

CAUSE_MEASLES = causes.cause.measles.name
CAUSE_DIARRHEAL = causes.cause.diarrheal_diseases.name
CAUSE_LOWER_RESPIRATORY_INFECTIONS = causes.cause.lower_respiratory_infections.name
CAUSE_NEONATAL_NEURAL_TUBE_DEFECTS = causes.cause.neural_tube_defects.name
CAUSE_NEONATAL_ENCEPHALOPATHY = causes.cause.neonatal_encephalopathy_due_to_birth_asphyxia_and_trauma.name
CAUSE_NEONATAL_SEPSIS = causes.cause.neonatal_sepsis_and_other_neonatal_infections.name
CAUSE_NEONATAL_JAUNDICE = causes.cause.hemolytic_disease_and_other_neonatal_jaundice.name

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


