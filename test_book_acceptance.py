import pytest
from book_reservation import BookReservationSystem


@pytest.fixture
def library():
    return BookReservationSystem(
        students={"S001", "S002"},
        books={"B001": 2}
    )


def test_acceptance_successful_reservation(library):
    """
    Given: A valid student and an available book.
    When: The student reserves the book.
    Then: The reservation succeeds and stock decreases by one.
    """
    # Given
    initial_stock = library.check_availability("B001")

    # When
    result = library.reserve("S001", "B001")

    # Then
    assert result is True
    assert library.check_availability("B001") == initial_stock - 1


def test_acceptance_prevent_duplicate_reservation(library):
    """
    Given: A student already has an active reservation.
    When: The student attempts to reserve the same book again.
    Then: The second reservation is rejected and stock is unchanged.
    """
    # Given
    library.reserve("S001", "B001")
    stock_after_first_reservation = library.check_availability("B001")

    # When
    result = library.reserve("S001", "B001")

    # Then
    assert result is False
    assert (
        library.check_availability("B001")
        == stock_after_first_reservation
    )