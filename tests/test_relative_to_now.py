"""Run a few basic tests."""

import datetime
import time
import pytest
from RelativeToNow import relative_to_now


def test_datetime():
    """Test datetime.datetime."""
    assert (
        relative_to_now(datetime.datetime.now() + datetime.timedelta(days=1))
        == "1 day from now"
    )
    assert (
        relative_to_now(datetime.datetime.now() + datetime.timedelta(minutes=2))
        == "2 minutes from now"
    )
    assert (
        relative_to_now(datetime.datetime.now() - datetime.timedelta(minutes=2))
        == "2 minutes ago"
    )

    assert (
        relative_to_now(datetime.datetime.now() - datetime.timedelta(seconds=2))
        == "2 seconds ago"
    )

    assert (
        relative_to_now(datetime.datetime.now() + datetime.timedelta(seconds=2))
        == "2 seconds from now"
    )

    assert (
        relative_to_now(
            datetime.datetime.now().astimezone() - datetime.timedelta(hours=5)
        )
        == "5 hours ago"
    )

    assert (
        relative_to_now(datetime.datetime.now() + datetime.timedelta(days=8))
        == "1 week from now"
    )

    assert (
        relative_to_now(datetime.datetime.now() - datetime.timedelta(days=8))
        == "1 week ago"
    )

    assert (
        relative_to_now(datetime.datetime.now() + datetime.timedelta(days=367))
        == "1 year from now"
    )

    assert (
        relative_to_now(datetime.datetime.now() - datetime.timedelta(days=367))
        == "1 year ago"
    )


def test_date():
    """Test datetime.date."""
    assert (
        relative_to_now(datetime.date.today() + datetime.timedelta(days=1))
        == "1 day from now"
    )
    assert (
        relative_to_now(datetime.date.today() + datetime.timedelta(days=2))
        == "2 days from now"
    )
    assert (
        relative_to_now(datetime.date.today() - datetime.timedelta(days=2))
        == "2 days ago"
    )


def test_time():
    """Test time."""
    assert relative_to_now(time.time()) == "just now"


def test_bad_date():
    """Test date error."""
    with pytest.raises(Exception) as exc_info:
        relative_to_now("asdf")

    assert str(exc_info.value) == "type must be date or datetime."
