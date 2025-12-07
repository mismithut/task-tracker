#!/usr/bin/env python3
"""
Task Tracker - A simple command-line task management tool
This is your first development project to learn Git and development workflows!
"""

import json
import os
from datetime import datetime


class TaskTracker:
    """Manages a list of tasks with basic CRUD operations."""
    
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, description):
        """Add a new task."""
        # TODO: Add priority field (high, medium, low) in future update
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task added: {description}")
    
    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks yet! Add one with: python task_tracker.py add 'Your task'")
            return
        
        print("\n📋 Your Tasks:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
        print("-" * 50)
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"✓ Task {task_id} marked as complete!")
                return
        print(f"❌ Task {task_id} not found")
    
    def delete_task(self, task_id):
        """Delete a task."""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted = self.tasks.pop(i)
                self.save_tasks()
                print(f"✓ Deleted: {deleted['description']}")
                return
        print(f"❌ Task {task_id} not found")


def main():
    """Main entry point for the task tracker."""
    import sys
    
    tracker = TaskTracker()
    
    if len(sys.argv) < 2:
        print("Task Tracker - Learn Development by Building!")
        print("\nUsage:")
        print("  python task_tracker.py list              - Show all tasks")
        print("  python task_tracker.py add 'description' - Add a new task")
        print("  python task_tracker.py complete <id>     - Mark task as done")
        print("  python task_tracker.py delete <id>       - Delete a task")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'list':
        tracker.list_tasks()
    elif command == 'add':
        if len(sys.argv) < 3:
            print("❌ Please provide a task description")
        else:
            tracker.add_task(' '.join(sys.argv[2:]))
    elif command == 'complete':
        if len(sys.argv) < 3:
            print("❌ Please provide a task ID")
        else:
            tracker.complete_task(int(sys.argv[2]))
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("❌ Please provide a task ID")
        else:
            tracker.delete_task(int(sys.argv[2]))
    else:
        print(f"❌ Unknown command: {command}")


if __name__ == '__main__':
    main()
