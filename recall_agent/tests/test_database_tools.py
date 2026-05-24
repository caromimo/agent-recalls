import pytest
from recall_agent.tools.database_tools import Tool

tools = Tool("./recall_agent/tests/data/TestData.csv")

def test_count_recalls_by_month_and_year_valid():
    # Test a known valid count using the test dataset - expect 5 recalls in May 2025
    result = tools.count_recalls_by_month_and_year(2025, "May")
    assert isinstance(result, int)
    assert result == 5

def test_count_recalls_by_month_and_year_formatting():
    # Test that case and whitespace are handled correctly
    result_upper = tools.count_recalls_by_month_and_year(2025, "  MAY  ")
    assert result_upper == 5

def test_count_recalls_by_month_and_year_invalid_month():
    # Test that providing an invalid month raises a ValueError
    with pytest.raises(ValueError, match="Invalid month name provided."):
        tools.count_recalls_by_month_and_year(2025, "smay")