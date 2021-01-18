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
    assert relative_to_now(time.time()) == "0 seconds from now"
