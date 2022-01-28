from forecasting_framework.data.pipeline import data_pipeline
from dagster import execute_pipeline


def test_pre_process():
    """
    test to check if pipeline runs successfully
    """
    result = execute_pipeline(data_pipeline)
    assert result.success
