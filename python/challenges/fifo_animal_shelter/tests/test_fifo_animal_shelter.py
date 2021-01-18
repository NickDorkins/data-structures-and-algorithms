from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter, InvalidOperationError

from fifo_animal_shelter import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_enqueue_values():
    q = AnimalShelter()
    q.enqueue("cat")
    q.enqueue("dog")
    actual = q.front.value
    expected = "cat"
    assert actual == expected
