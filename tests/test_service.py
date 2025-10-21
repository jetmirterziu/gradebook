"""
tests/test_service.py
Unit tests for the Gradebook service layer using pytest.
"""

import pytest
from gradebook import service, storage


@pytest.fixture(autouse=True)
def clean_data(tmp_path, monkeypatch):
    """Use a temporary file for clean testing."""
    fake_file = tmp_path / "gradebook.json"
    monkeypatch.setattr(storage, "DATA_FILE", str(fake_file))
    storage.save_data({"students": [], "courses": [], "enrollments": []})


def test_add_student():
    s = service.add_student("Alice")
    assert s.name == "Alice"
    data = storage.load_data()
    assert len(data["students"]) == 1


def test_add_course():
    c = service.add_course("CS101", "Intro to CS")
    assert c.code == "CS101"
    assert c.title == "Intro to CS"


def test_enroll_and_add_grade():
    s = service.add_student("Bob")
    c = service.add_course("MATH101", "Math Basics")
    e = service.enroll_student(s.id, c.code)
    assert e.course_code == "MATH101"

    service.add_grade(s.id, c.code, 90)
    data = storage.load_data()
    assert data["enrollments"][0]["grades"] == [90]


def test_compute_average_and_gpa():
    s = service.add_student("Carol")
    c = service.add_course("PHY101", "Physics")
    service.enroll_student(s.id, c.code)
    service.add_grade(s.id, c.code, 100)
    service.add_grade(s.id, c.code, 80)
    avg = service.compute_average(s.id, c.code)
    gpa = service.compute_gpa(s.id)
    assert avg == 90.0
    assert gpa == 90.0


# ❌ Intentionally failing test
def test_invalid_grade_should_fail():
    s = service.add_student("Dan")
    c = service.add_course("ENG101", "English")
    service.enroll_student(s.id, c.code)
    with pytest.raises(ValueError):
        service.add_grade(s.id, c.code, 150)
