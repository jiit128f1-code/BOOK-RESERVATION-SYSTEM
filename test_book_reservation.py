import pytest

from book_reservation import BookReservationSystem


@pytest.fixture
def library():
    return BookReservationSystem(
        students={"S001", "S002"},
        books={"B001": 2, "B002": 1}
    )


def test_reserve_available_book(library):
    assert library.reserve("S001", "B001") is True
    assert library.check_availability("B001") == 1


def test_check_book_availability(library):
    assert library.check_availability("B001") == 2
    assert library.check_availability("B002") == 1


def test_prevent_duplicate_reservation(library):
    assert library.reserve("S001", "B001") is True
    assert library.reserve("S001", "B001") is False
    assert library.check_availability("B001") == 1


def test_cancel_reservation(library):
    assert library.reserve("S001", "B001") is True
    assert library.cancel("S001", "B001") is True
    assert library.check_availability("B001") == 2


def test_reject_unavailable_book(library):
    assert library.reserve("S001", "B002") is True
    assert library.reserve("S002", "B002") is False
    assert library.check_availability("B002") == 0


def test_reject_invalid_student(library):
    assert library.reserve("INVALID", "B001") is False


def test_reject_invalid_book(library):
    assert library.reserve("S001", "INVALID") is False


def test_cannot_cancel_nonexistent_reservation(library):
    assert library.cancel("S001", "B001") is False