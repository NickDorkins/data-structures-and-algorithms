from hashtable import __version__


def test_version():
    assert __version__ == '0.1.0'

from hashtable.hashtable import Hashtable

def test_create():
    hashtable = Hashtable()
    assert hashtable


def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable._size


def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary

# Adding a key/value to your hashtable results in the value being in the data structure


# Retrieving based on a key returns the value stored


# Successfully returns null for a key that does not exist in the hashtable


# Successfully handle a collision within the hashtable


# Successfully retrieve a value from a bucket within the hashtable that has a collision


# Successfully hash a key to an in-range value