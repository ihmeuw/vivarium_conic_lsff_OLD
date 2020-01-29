import itertools
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

NEONATAL_CAUSES = [
    causes.neonatal_sepsis_and_other_neonatal_infections.name,
    causes.neonatal_encephalopathy_due_to_birth_asphyxia_and_trauma.name,
    causes.hemolytic_disease_and_other_neonatal_jaundice.name,
    causes.neural_tube_defects.name
]

OTHER_CAUSES = [
    causes.diarrheal_diseases.name,
    causes.lower_respiratory_infections.name,
    causes.measles.name,
    causes.meningitis.name
]

CAUSE_MEASURES = dict(
    {causes.all_causes.name: ['cause_specific_mortality_rate'],
     causes.measles.name: [c for c in DEFAULT_CAUSE_LIST if c != 'remission_rate']},
    **{neonatal_cause: NEONATAL_CAUSE_LIST for neonatal_cause in NEONATAL_CAUSES},
    **{other_cause: DEFAULT_CAUSE_LIST for other_cause in OTHER_CAUSES if other_cause != causes.measles.name}
)
TREATMENT_GROUPS = ['treated', 'untreated']
AGE_GROUPS = ['early_neonatal', 'late_neonatal', 'post_neonatal', '1_to_4']
YEARS = list(range(2020, 2026))
SEX = ['male', 'female']

STRATIFICATION_GROUPS = list(itertools.product(YEARS, SEX, AGE_GROUPS, TREATMENT_GROUPS))

# tracked metrics
PERSON_TIME = 'person_time'
DEATH = 'death'
YLLS = 'ylls'
YLDS = 'ylds'
DALYS = 'dalys'


# States and Transitions
SUSCEPTIBLE_NEONATAL_SEPSIS = 'susceptible_neonatal_sepsis'
ACTIVE_NEONATAL_SEPSIS = 'active_neonatal_sepsis'
NEONATAL_SEPSIS_STATES = [SUSCEPTIBLE_NEONATAL_SEPSIS, ACTIVE_NEONATAL_SEPSIS]
NEONATAL_SEPSIS_TRANSITIONS = [f'{SUSCEPTIBLE_NEONATAL_SEPSIS}_to_{ACTIVE_NEONATAL_SEPSIS}',
                               f'{ACTIVE_NEONATAL_SEPSIS}_to_{SUSCEPTIBLE_NEONATAL_SEPSIS}']

SUSCEPTIBLE_NEONATAL_ENCEPHALOPATHY = 'susceptible_neonatal_encephalopathy'
ACTIVE_NEONATAL_ENCEPHALOPATHY = 'active_neonatal_encephalopathy'
NEONATAL_ENCEPHALOPATHY_STATES = [SUSCEPTIBLE_NEONATAL_ENCEPHALOPATHY, ACTIVE_NEONATAL_ENCEPHALOPATHY]
NEONATAL_ENCEPHALOPATHY_TRANSITIONS = [
    f'{SUSCEPTIBLE_NEONATAL_ENCEPHALOPATHY}_to_{ACTIVE_NEONATAL_ENCEPHALOPATHY}',
    f'{ACTIVE_NEONATAL_ENCEPHALOPATHY}_to_{SUSCEPTIBLE_NEONATAL_ENCEPHALOPATHY}'
]

SUSCEPTIBLE_NEONATAL_JAUNDICE = 'susceptible_neonatal_jaundice'
ACTIVE_NEONATAL_JAUNDICE = 'active_neonatal_jaundice'
NEONATAL_JAUNDICE_STATES = [SUSCEPTIBLE_NEONATAL_JAUNDICE, ACTIVE_NEONATAL_JAUNDICE]
NEONATAL_JAUNDICE_TRANSITIONS = [f'{SUSCEPTIBLE_NEONATAL_JAUNDICE}_to_{ACTIVE_NEONATAL_JAUNDICE}',
                                 f'{ACTIVE_NEONATAL_JAUNDICE}_to_{SUSCEPTIBLE_NEONATAL_JAUNDICE}']

SUSCEPTIBLE_DIARRHEA = 'susceptible_diarrhea'
ACTIVE_DIARRHEA = 'active_diarrhea'
DIARRHEA_STATES = [SUSCEPTIBLE_DIARRHEA, ACTIVE_DIARRHEA]
DIARRHEA_TRANSITIONS = [f'{SUSCEPTIBLE_DIARRHEA}_to_{ACTIVE_DIARRHEA}', f'{ACTIVE_DIARRHEA}_to_{SUSCEPTIBLE_DIARRHEA}']

SUSCEPTIBLE_LRI = 'susceptible_lower_respiratory_infection'
ACTIVE_LRI = 'active_lower_respiratory_infection'
LRI_STATES = [SUSCEPTIBLE_LRI, ACTIVE_LRI]
LRI_TRANSITIONS = [f'{SUSCEPTIBLE_LRI}_to_{ACTIVE_LRI}' f'{ACTIVE_LRI}_to_{SUSCEPTIBLE_LRI}']

SUSCEPTIBLE_MEASLES = 'susceptible_measles'
ACTIVE_MEASLES = 'active_measles'
EXPOSED_MEASLES = 'exposed_measles'
MEASLES_STATES = [SUSCEPTIBLE_MEASLES, ACTIVE_MEASLES, EXPOSED_MEASLES]
MEASLES_TRANSITIONS = [f'{SUSCEPTIBLE_MEASLES}_to_{ACTIVE_MEASLES}', f'{ACTIVE_MEASLES}_to_{EXPOSED_MEASLES}']

SUSCEPTIBLE_MENINGITIS = 'susceptible_meningitis'
ACTIVE_MENINGITIS = 'active_meningitis'
MENINGITIS_STATES = [SUSCEPTIBLE_MENINGITIS, ACTIVE_MENINGITIS]
MENINGITIS_TRANSITIONS = [f'{SUSCEPTIBLE_MENINGITIS}_to_{ACTIVE_MENINGITIS}',
                          f'{ACTIVE_MENINGITIS}_to_{SUSCEPTIBLE_MENINGITIS}']

STATES = (NEONATAL_SEPSIS_STATES + NEONATAL_ENCEPHALOPATHY_STATES + NEONATAL_JAUNDICE_STATES + DIARRHEA_STATES
          + LRI_STATES + MEASLES_STATES + MENINGITIS_STATES)

TRANSITIONS = (NEONATAL_SEPSIS_TRANSITIONS + NEONATAL_ENCEPHALOPATHY_TRANSITIONS + NEONATAL_JAUNDICE_TRANSITIONS
               + DIARRHEA_TRANSITIONS + LRI_TRANSITIONS + MEASLES_TRANSITIONS + MENINGITIS_TRANSITIONS)

#################################
# Results columns and variables #
#################################

TOTAL_POP_COLUMN = 'total_population'
TOTAL_YLLS_COLUMN = 'years_of_life_lost'
TOTAL_YLDS_COLUMN = 'years_lived_with_disability'
TOTAL_PERSON_TIME_COLUMN = 'person_time'
RANDOM_SEED_COLUMN = 'random_seed'
INPUT_DRAW_COLUMN = 'input_draw'
SCENARIO_COLUMN = 'scenario'
COUNTRY_COLUMN = 'country'

STANDARD_COLUMNS = {
    'total_population': TOTAL_POP_COLUMN,
    'total_ylls': TOTAL_YLLS_COLUMN,
    'total_ylds': TOTAL_YLDS_COLUMN,
    'total_person_time': TOTAL_PERSON_TIME_COLUMN,
    'random_seed': RANDOM_SEED_COLUMN,
    'input_draw': INPUT_DRAW_COLUMN,
    'scenario': SCENARIO_COLUMN,
    'country': COUNTRY_COLUMN
}

METRIC_COLUMN_TEMPLATE = '{METRIC}_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'
PERSON_TIME_BY_STATE_COLUMN_TEMPLATE = 'person_time_{STATE}_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'
YLDS_COLUMN_TEMPLATE = 'ylds_due_to_{CAUSE_OF_DISABILITY}_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'
YLLS_COLUMN_TEMPLATE = 'ylls_due_to_{CAUSE_OF_DEATH}_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'
DALYS_COLUMN_TEMPLATE = 'dalys_due_to_{CAUSE_OF_DEATH}_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'
DEATH_COLUMN_TEMPLATE = 'death_due_to_{CAUSE_OF_DEATH}_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'
COUNT_COLUMN_TEMPLATE = '{COUNT_EVENT}_count_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'
TRANSITION_COLUMN_TEMPLATE = '{TRANSITION}_event_count_in_age_group_{AGE_GROUP}_treatment_group_{TREATMENT_GROUP}'

COLUMN_TEMPLATES = {
    'metrics': METRIC_COLUMN_TEMPLATE,
    'person_time_by_state': PERSON_TIME_BY_STATE_COLUMN_TEMPLATE,
    'ylds': YLDS_COLUMN_TEMPLATE,
    'ylls': YLLS_COLUMN_TEMPLATE,
    'dalys': DALYS_COLUMN_TEMPLATE,
    'death': DEATH_COLUMN_TEMPLATE,
    'counts': COUNT_COLUMN_TEMPLATE,
    'transitions': TRANSITION_COLUMN_TEMPLATE
}

CAUSES_OF_DISABILITY = [cause for cause in CAUSE_MEASURES.keys() if cause != causes.all_causes.name]
CAUSES_OF_DEATH = CAUSES_OF_DISABILITY + ['other_causes']
COUNT_EVENTS = []

METRICS = [PERSON_TIME, DEATH, YLLS, YLDS, DALYS] + [
    f'{stat}_{metric}'
    for metric in []
    for stat in ['mean', 'sd']
]

TEMPLATE_FIELD_MAP = {
    'TREATMENT_GROUP': TREATMENT_GROUPS,
    'AGE_GROUP': AGE_GROUPS,
    'CAUSE_OF_DISABILITY': CAUSES_OF_DISABILITY,
    'CAUSE_OF_DEATH': CAUSES_OF_DEATH,
    'COUNT_EVENT': COUNT_EVENTS + NEONATAL_CAUSES,
    'METRIC': METRICS,
    'STATE': STATES,
    'TRANSITION': TRANSITIONS
}

NEONATAL_SEPSIS_IR_MEID=1594


def result_columns(kind='all'):
    if kind not in COLUMN_TEMPLATES and kind != 'all':
        raise ValueError(f'Unknown result column type {kind}')
    columns = []
    if kind == 'all':
        for k in COLUMN_TEMPLATES:
            columns += result_columns(k)
        columns = list(STANDARD_COLUMNS.values()) + columns
    else:
        template = COLUMN_TEMPLATES[kind]
        filtered_field_map = {field: values
                              for field, values in TEMPLATE_FIELD_MAP.items() if f'{{{field}}}' in template}
        fields, value_groups = filtered_field_map.keys(), itertools.product(*filtered_field_map.values())
        for value_group in value_groups:
            columns.append(template.format(**{field: value for field, value in zip(fields, value_group)}))
    return columns
