from pathlib import Path
from loguru import logger

import pandas as pd

from gbd_mapping import causes
from vivarium import Artifact
from vivarium.framework.artifact import get_location_term
from vivarium.framework.artifact.hdf import EntityKey

from vivarium_inputs.data_artifact.loaders import loader
from vivarium_inputs.data_artifact.utilities import split_interval

import vivarium_conic_lsff.globals as lsff_globals


DIRECTORY_PERMS = 0o775
def build_artifact(path, location):
    # ensure the project artifact directory exists and has the correct permission
    Path(path).mkdir(exist_ok=True, parents=True)
    Path(path).chmod(DIRECTORY_PERMS)

    sanitized_location = location.lower().replace(" ", "_").replace("'", "-")
    artifact = create_new_artifact(path / f'{sanitized_location}.hdf', location)

    write_demographic_data(artifact, location)

    for disease in lsff_globals.CAUSES_WITH_INCIDENCE:
        logger.info(f'{location}: Writing disease data for "{disease}"')
        write_disease_data(artifact, location, disease)

    for disease in lsff_globals.CAUSES_NEONATAL:
        logger.info(f'{location}: Writing neonatal disease data for "{disease}"')
        write_neonatal_disease_data(artifact, location, disease)


def create_new_artifact(path: str, location: str) -> Artifact:
    if Path(path).is_file():
        Path(path).unlink()

    art = Artifact(path, filter_terms=[get_location_term(location)])
    art.write('metadata.locations', [location])
    return art


def get_load(location):
    return lambda key: loader(EntityKey(key), location, set())


def write_demographic_data(artifact, location):
    load = get_load(location)

    prefix = 'population.'
    measures = ["structure", "age_bins", "theoretical_minimum_risk_life_expectancy", "demographic_dimensions"]
    for m in measures:
        key = prefix + m
        write(artifact, key, load(key))

    key = 'cause.all_causes.cause_specific_mortality_rate'
    write(artifact, key, load(key))

    key = 'covariate.live_births_by_sex.estimate'
    write(artifact, key, load(key))


def write_common_disease_data(artifact, location, disease):
    load = get_load(location)

    # Metadata
    key = f'cause.{disease}.sequelae'
    sequelae = load(key)
    write(artifact, key, sequelae)
    key = f'cause.{disease}.restrictions'
    write(artifact, key, load(key))
    # Measures for Disease Model
    key = f'cause.{disease}.cause_specific_mortality_rate'
    write(artifact, key, load(key))

    # Measures for Disease States
    p, dw = load_prev_dw(sequelae, location)
    write(artifact, f'cause.{disease}.prevalence', p)
    write(artifact, f'cause.{disease}.disability_weight', dw)
    write(artifact, f'cause.{disease}.excess_mortality_rate', load(f'cause.{disease}.excess_mortality_rate'))


def write_disease_data(artifact, location, disease):
    write_common_disease_data(artifact, location, disease)

    # Measures for Transitions
    load = get_load(location)
    key = f'cause.{disease}.incidence_rate'
    assert getattr(causes, disease).incidence_rate_exists
    write(artifact, key, load(key))


def write_neonatal_disease_data(artifact, location, disease):
    write_common_disease_data(artifact, location, disease)

    # Measures for Transitions
    load = get_load(location)
    key = f'cause.{disease}.birth_prevalence'
    write(artifact, key, load(key))


def load_prev_dw(sequela, location):
    load = get_load(location)
    prevalence = [load(f'sequela.{s}.prevalence') for s in sequela]
    disability_weight = [load(f'sequela.{s}.disability_weight') for s in sequela]
    total_prevalence = sum(prevalence)
    total_disability_weight = sum([p * dw for p, dw in zip(prevalence, disability_weight)]) / total_prevalence
    return total_prevalence, total_disability_weight


def write(artifact, key, data, skip_interval_processing=False):
    if skip_interval_processing:
        tmp = data
    else:
        tmp = data.copy(deep='all') if isinstance(data, pd.DataFrame) else data
        tmp = split_interval(tmp, interval_column='age', split_column_prefix='age')
        tmp = split_interval(tmp, interval_column='year', split_column_prefix='year')
    artifact.write(key, tmp)

