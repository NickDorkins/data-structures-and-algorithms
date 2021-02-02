from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation as val







def test_bracket_validation():
    actual = val('')
    expected = False
    assert actual == expected 

def test_bracket_validation1():
    actual = val('()')
    expected = True
    assert actual == expected 

def test_bracket_validation2():
    actual = val('(Code)')
    expected = True
    assert actual == expected 