from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 Main St, Springfield, IL 62701") == "Springfield"
    assert extract_city("456 NotMain Ave, Chicago, IL 60601") == "Chicago"
    assert extract_city("789 Backup Cir, New York, NY 10001") == "New York"

def test_extract_state():
    assert extract_state("123 Main St, Springfield, IL 62701") == "IL"
    assert extract_state("456 NotMain Ave, Chicago, IL 60601") == "IL"
    assert extract_state("789 Backup Cir, New York, NY 10001") == "NY"

def test_extract_zipcode():
    assert extract_zipcode("123 Main St, Springfield, IL 62701") == "62701"
    assert extract_zipcode("456 NotMain Ave, Chicago, IL 60601") == "60601"
    assert extract_zipcode("789 Backup Cir, New York, NY 10001") == "10001"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
