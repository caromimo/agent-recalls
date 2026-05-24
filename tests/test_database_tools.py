import pytest
from recall_agent.tools.database_tools import Tool


tools = Tool()

def test_count_recalls_by_month_and_year_valid():
    # Test a known valid count (July 2022 has 96 recalls in the dataset)
    result = tools.count_recalls_by_month_and_year(2022, "july")
    assert isinstance(result, int)
    assert result == 96

def test_count_recalls_by_month_and_year_formatting():
    # Test that case and whitespace are handled correctly
    result_upper = tools.count_recalls_by_month_and_year(2022, "  JULY  ")
    assert result_upper == 96

def test_count_recalls_by_month_and_year_invalid_month():
    # Test that providing an invalid month raises a ValueError
    with pytest.raises(ValueError, match="Invalid month name provided."):
        tools.count_recalls_by_month_and_year(2022, "smarch")