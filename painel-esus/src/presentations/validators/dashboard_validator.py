from .base_validation import _validation
from .schema.age_groups_gender_schema import schema as age_group_gender_schema
from .schema.age_groups_location_schema import age_groups_location_schema
from .schema.hypertension_complications_schema import \
    hypertension_complications_schema
from .schema.professionals_count_schema import professionals_count_schema


def age_group_gender_validator(entry):
    return _validation(entry, age_group_gender_schema)


def age_group_location_validator(entry):
    return _validation(entry, age_groups_location_schema)


def professionals_count(entry):
    return _validation(entry, professionals_count_schema)


def hypertension_complications(entry):
    return _validation(entry, hypertension_complications_schema)
