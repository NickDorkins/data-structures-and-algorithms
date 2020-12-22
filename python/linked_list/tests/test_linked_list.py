from linked_list import LinkedList, Node


def test_import():
    assert LinkedList

def test_creates_empty_list():
    emptyList = LinkedList()
    actual = emptyList.head
    expected = None
    assert expected == actual

def test_insert_new_node_added_to_head():
    insertList = LinkedList()
    insertList.insert("string")
    expected = "string"
    actual = insertList.head.nodeValue
    assert expected == actual



def test_create_head_and_point_to_first_value():
    pointToHeadList = LinkedList()
    pointToHeadList.insert("WON")
    pointToHeadList.insert("TOO")
    expected = "WON"
    actual = pointToHeadList.head.nodeValue



def test_multi_value_insert():
    multiInputList = LinkedList()
    multiInputList.insert("WON")
    multiInputList.insert("TOO")
    multiInputList.insert("THR33")
    actual = [multiInputList.head.nodeValue, multiInputList.head.nextNodeValue.nodeValue, multiInputList.head.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33"]


def test_true_boolean_return_for_existing_in_list():
    trueList = LinkedList()
    trueList.insert("WON")
    trueList.insert("TOO")
    trueList.insert("THR33")
    actual = trueList.includes("WON")
    expected = True
    assert actual == expected



def test_false_boolean_return_for_existing_in_list():
    falseList = LinkedList()
    falseList.insert("WON")
    falseList.insert("TOO")
    falseList.insert("THR33")
    actual = falseList.includes("FOR")
    expected = False
    assert actual == expected


def test_complete_list_return_as_string():
    returnedList = LinkedList()
    returnedList.insert("THR33")
    returnedList.insert("TOO")
    returnedList.insert("WON")
    actual = [returnedList.head.nodeValue, returnedList.head.nextNodeValue.nodeValue, returnedList.head.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33"]
    assert actual == expected
