from graph.graph import Graph, Vertex, Edge
import pytest

def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected


def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'b'
    assert actual != expected

def test_add_node():
    graph = Graph()
    expected = 'a'
    actual = graph.add_node('a').value
    assert actual == expected

def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True

def test_add_edge_true_2():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True

def test_size_pass():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 2
    actual = len(graph)
    assert actual == expected 

def test_size_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 3
    actual = len(graph)
    assert actual != expected 


def test_get_node_pass():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.get_node(b)
    assert True

def test_get_node_fail():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    actual = graph.get_node('c') 
    expected = 'Value not found'
    assert actual == expected
        