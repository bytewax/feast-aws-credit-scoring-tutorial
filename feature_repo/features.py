from datetime import timedelta

from feast import Entity, Feature, FeatureView, RedshiftSource, ValueType, Field
from feast.types import Float32, Float64, Int64, String

zipcode = Entity(name="zipcode", value_type=ValueType.INT64)

zipcode_source = RedshiftSource(
    name="zipcode_features_source",
    query="SELECT * FROM spectrum.zipcode_features",
    timestamp_field="event_timestamp",
)

zipcode_features = FeatureView(
    name="zipcode_features",
    source=zipcode_source,
    entities=[zipcode],
    ttl=timedelta(days=3650),
    schema=[
        Field(name="city", dtype=String),
        Field(name="state", dtype=String),
        Field(name="location_type", dtype=String),
        Field(name="tax_returns_filed", dtype=Int64),
        Field(name="population", dtype=Int64),
        Field(name="total_wages", dtype=Int64),
    ],
)

dob_ssn = Entity(
    name="dob_ssn",
    value_type=ValueType.STRING,
    description="Date of birth and last four digits of social security number",
)

credit_history_source = RedshiftSource(
    name="credit_history_source",
    query="SELECT * FROM spectrum.credit_history",
    timestamp_field="event_timestamp",
)

credit_history = FeatureView(
    name="credit_history",
    source=credit_history_source,
    entities=[dob_ssn],
    ttl=timedelta(days=90),
    schema=[
        Field(name="credit_card_due", dtype=Int64),
        Field(name="mortgage_due", dtype=Int64),
        Field(name="student_loan_due", dtype=Int64),
        Field(name="vehicle_loan_due", dtype=Int64),
        Field(name="hard_pulls", dtype=Int64),
        Field(name="missed_payments_2y", dtype=Int64),
        Field(name="missed_payments_1y", dtype=Int64),
        Field(name="missed_payments_6m", dtype=Int64),
        Field(name="bankruptcies", dtype=Int64),
    ],
)
