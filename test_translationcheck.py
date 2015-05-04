import linecheck
import pytest

def test_it_returns_lines_if_key_is_not_found():
    checker = linecheck.Checker({})
    test_lines = ["foo=bar", "bar=baz"]
    assert(test_lines == checker.get_lines(test_lines))

def test_it_omits_lines_if_key_is_found():
    checker = linecheck.Checker({"foo":"boo"})
    test_lines = ["foo=bar", "bar=baz"]
    assert(["bar=baz"] == checker.get_lines(test_lines))

def test_it_handles_property_values_with_equal_sign():
    checker = linecheck.Checker({})
    test_lines = ["foo=bar", "bar=baz=quux"]
    assert(test_lines == checker.get_lines(test_lines))

def test_it_returns_non_property_lines_if_key_is_not_found():
    checker = linecheck.Checker({})
    test_lines = ["foo=bar", "#comment", "bar=baz"]
    assert(test_lines == checker.get_lines(test_lines))
    test_lines = ["#comment1", "#comment2", "foo=bar", "bar=baz"]
    assert(test_lines == checker.get_lines(test_lines))

def test_it_returns_non_property_lines_if_some_keys_are_not_found():
    checker = linecheck.Checker({"bar":"boo"})
    test_lines = ["#comment", "foo=bar", "bar=baz"]
    assert(["#comment", "foo=bar"] == checker.get_lines(test_lines))

def test_it_omits_last_property_lines_if_key_is_found():
    checker = linecheck.Checker({"bar":"boo"})
    test_lines = ["foo=bar", "#comment1", "#comment2", "bar=baz"]
    assert(["foo=bar"] == checker.get_lines(test_lines))

def test_it_treats_comments_with_equal_signs_as_non_property_lines():
    checker = linecheck.Checker({})
    test_lines = ["# comment=foo", "bar=baz"]
    assert(test_lines == checker.get_lines(test_lines))

def test_it_recognizes_and_omits_multiline_properties_if_key_is_found():
    checker = linecheck.Checker({"bar":"boo"})
    test_lines = ["bar=baz \\\n","quux", "foo=bar"]
    assert(["foo=bar"] == checker.get_lines(test_lines))    

def test_it_recognizes_and_return_multiline_properties_if_key_is_found():
    checker = linecheck.Checker({})
    test_lines = ["bar=baz \\\n", "quux", "foo=bar"]
    assert(test_lines == checker.get_lines(test_lines))    