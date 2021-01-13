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
    pointToHeadList.insert("TOO")
    pointToHeadList.insert("WON")
    expected = "WON"
    actual = pointToHeadList.head.nodeValue
    assert actual == expected



def test_multi_value_insert():
    multiInputList = LinkedList()
    multiInputList.insert("THR33")
    multiInputList.insert("TOO")
    multiInputList.insert("WON")
    actual = [multiInputList.head.nodeValue, multiInputList.head.nextNodeValue.nodeValue, multiInputList.head.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33"]
    assert actual == expected


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



def test_append():
    appendList = LinkedList()
    appendList.insert("THR33")
    appendList.insert("TOO")
    appendList.insert("WON")
    appendList.append("FOR")
    actual = [appendList.head.nodeValue, appendList.head.nextNodeValue.nodeValue, appendList.head.nextNodeValue.nextNodeValue.nodeValue, appendList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33", "FOR"]
    assert actual == expected


def test_multiple_append():
    multipleAppendList = LinkedList()
    multipleAppendList.insert("THR33")
    multipleAppendList.insert("TOO")
    multipleAppendList.insert("WON")
    multipleAppendList.append("FOR")
    multipleAppendList.append("F1V3")
    actual = [multipleAppendList.head.nodeValue, multipleAppendList.head.nextNodeValue.nodeValue, multipleAppendList.head.nextNodeValue.nextNodeValue.nodeValue, multipleAppendList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue, multipleAppendList.head.nextNodeValue.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33", "FOR", "F1V3"]
    assert actual == expected


def test_insert_before_value():
    insertBeforeList = LinkedList()
    insertBeforeList.insert("THR33")
    insertBeforeList.insert("TOO")
    insertBeforeList.insert("WON")
    insertBeforeList.insertBefore("TOO", "INSERTER")
    actual = [insertBeforeList.head.nodeValue, insertBeforeList.head.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "INSERTER", "TOO", "THR33"]
    assert actual == expected



def test_insert_before_head_value():
    insertBeforeList = LinkedList()
    insertBeforeList.insert("THR33")
    insertBeforeList.insert("TOO")
    insertBeforeList.insert("WON")
    insertBeforeList.insertBefore("WON", "Z3R0")
    actual = [insertBeforeList.head.nodeValue, insertBeforeList.head.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["Z3R0", "WON", "TOO", "THR33"]
    assert actual == expected


def test_insert_in_middle_value():
    insertToMiddle = LinkedList()
    insertToMiddle.insert("THR33")
    insertToMiddle.insert("TOO")
    insertToMiddle.insert("WON")
    insertToMiddle.insertAfter("WON", "FORE")
    actual = [insertToMiddle.head.nodeValue, insertToMiddle.head.nextNodeValue.nodeValue, insertToMiddle.head.nextNodeValue.nextNodeValue.nodeValue, insertToMiddle.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "FORE", "TOO", "THR33"]
    assert actual == expected

def test_insert_to_end_value():
    insertToEnd = LinkedList()
    insertToEnd.insert("THR33")
    insertToEnd.insert("TOO")
    insertToEnd.insert("WON")
    insertToEnd.insertAfter("THR33", "FORE")
    actual = [insertToEnd.head.nodeValue, insertToEnd.head.nextNodeValue.nodeValue, insertToEnd.head.nextNodeValue.nextNodeValue.nodeValue, insertToEnd.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33", "FORE"]
    assert actual == expected