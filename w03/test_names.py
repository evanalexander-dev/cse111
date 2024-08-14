from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John", "Whitmer") == "Whitmer; John"
    assert make_full_name("Billy-Bob", "Joe") == "Joe; Billy-Bob"
    assert make_full_name("Hank", "Green") == "Green; Hank"
    assert make_full_name("Inigo", "Montoya") == "Montoya; Inigo"
    assert make_full_name("HelloMyNameIsBob", "HelloMyLastNameIsBillyBobJoeTheSmithTheThird") == "HelloMyLastNameIsBillyBobJoeTheSmithTheThird; HelloMyNameIsBob"
    assert make_full_name("Hubert Blaine", "Wolfeschlegelsteinhausenbergerdorff") == "Wolfeschlegelsteinhausenbergerdorff; Hubert Blaine"

def test_extract_family_name():
    assert extract_family_name("Whitmer; John") == "Whitmer"
    assert extract_family_name("Joe; Billy-Bob") == "Joe"
    assert extract_family_name("Green; Hank") == "Green"
    assert extract_family_name("Montoya; Inigo") == "Montoya"
    assert extract_family_name("HelloMyLastNameIsBillyBobJoeTheSmithTheThird; HelloMyNameIsBob") == "HelloMyLastNameIsBillyBobJoeTheSmithTheThird"
    assert extract_family_name("Wolfeschlegelsteinhausenbergerdorff; Hubert Blaine") == "Wolfeschlegelsteinhausenbergerdorff"

def test_extract_given_name():
    assert extract_given_name("Whitmer; John") == "John"
    assert extract_given_name("Joe; Billy-Bob") == "Billy-Bob"
    assert extract_given_name("Green; Hank") == "Hank"
    assert extract_given_name("Montoya; Inigo") == "Inigo"
    assert extract_given_name("HelloMyLastNameIsBillyBobJoeTheSmithTheThird; HelloMyNameIsBob") == "HelloMyNameIsBob"
    assert extract_given_name("Wolfeschlegelsteinhausenbergerdorff; Hubert Blaine") == "Hubert Blaine"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
