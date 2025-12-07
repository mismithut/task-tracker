"""
Unit tests for the Task Tracker application.
Run with: python -m pytest test_task_tracker.py
"""

import os
import json
import pytest
from task_tracker import TaskTracker


@pytest.fixture
def tracker():
    """Create a TaskTracker instance with a temporary file."""
    test_file = 'test_tasks.json'
    tracker = TaskTracker(test_file)
    yield tracker
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)


def test_add_task(tracker):
    """Test adding a new task."""
    tracker.add_task("Learn Git basics")
    assert len(tracker.tasks) == 1
    assert tracker.tasks[0]['description'] == "Learn Git basics"
    assert tracker.tasks[0]['completed'] == False


def test_complete_task(tracker):
    """Test completing a task."""
    tracker.add_task("Write code")
    tracker.complete_task(1)
    assert tracker.tasks[0]['completed'] == True


def test_delete_task(tracker):
    """Test deleting a task."""
    tracker.add_task("Task to delete")
    tracker.delete_task(1)
    assert len(tracker.tasks) == 0


def test_persistence(tracker):
    """Test that tasks are saved and loaded correctly."""
    tracker.add_task("Persistent task")
    
    # Create a new tracker instance with the same file
    tracker2 = TaskTracker(tracker.filename)
    assert len(tracker2.tasks) == 1
    assert tracker2.tasks[0]['description'] == "Persistent task"
