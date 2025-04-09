"""Test functions in CL20_module"""

from CL20_module import hehe, count_regs


def test_hehe() -> (
    None
):  # inside function def call hehe and make sure output is what we expect it to be; return  value not necesary
    """Test hehe function."""
    assert hehe(3) == 0  # assert <boolean expression>


def test_count_regs_use() -> (
    None
):  # no value has to be returned back to where it was called
    """Test a USE CASE for count_regs."""
    assert count_regs("Orange", ["Wake", "Orange", "Orange", "Durham"])


def test_count_regs_egde() -> None:
    "Test EDGE CASE for count regs." ""
    assert count_regs("Orange", []) == 0


# type <python -m pytest CL20_module_test.py> in terminal to test.


def test_count_regs_mutate() -> None:
    """Test whether count_regs mutates list."""
    cs: list[str] = ["Durham", "Wake", "Lee"]
    count_regs("Wake", cs)
    assert cs == ["Durham", "Wake", "Lee"]
