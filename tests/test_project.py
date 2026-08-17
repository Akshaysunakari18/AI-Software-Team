import pytest
from workspace.student_marks_management import *

def test_add_student():
    management = StudentMarksManagement()
    management.add_student('Alice', 85)
    assert management.students == [{'name': 'Alice', 'marks': 85}]

def test_add_multiple_students():
    management = StudentMarksManagement()
    management.add_student('Alice', 85)
    management.add_student('Bob', 92)
    management.add_student('Charlie', 78)
    assert management.students == [{'name': 'Alice', 'marks': 85}, {'name': 'Bob', 'marks': 92}, {'name': 'Charlie', 'marks': 78}]

def test_calculate_average():
    management = StudentMarksManagement()
    management.add_student('Alice', 85)
    management.add_student('Bob', 92)
    management.add_student('Charlie', 78)
    assert management.calculate_average() == 85.0

def test_calculate_average_empty():
    management = StudentMarksManagement()
    assert management.calculate_average() == 0

def test_find_highest_scorer():
    management = StudentMarksManagement()
    management.add_student('Alice', 85)
    management.add_student('Bob', 92)
    management.add_student('Charlie', 78)
    assert management.find_highest_scorer() == {'name': 'Bob', 'marks': 92}

def test_find_highest_scorer_empty():
    management = StudentMarksManagement()
    assert management.find_highest_scorer() is None

def test_find_lowest_scorer():
    management = StudentMarksManagement()
    management.add_student('Alice', 85)
    management.add_student('Bob', 92)
    management.add_student('Charlie', 78)
    assert management.find_lowest_scorer() == {'name': 'Charlie', 'marks': 78}

def test_find_lowest_scorer_empty():
    management = StudentMarksManagement()
    assert management.find_lowest_scorer() is None