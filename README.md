# 🚀 Task Tracker - Learn Development by Building!

Welcome to your first development project! This simple task tracker will teach you essential development concepts while building something actually useful.

## 📚 What You'll Learn

### 1. **Git & Version Control**
- **Repository (Repo)**: This folder is your repository - where all your code lives
- **Commit**: Saving a snapshot of your code at a point in time
- **Branch**: A separate version of your code to try new things
- **Pull Request (PR)**: Asking to merge your changes into the main code
- **Push/Pull**: Sending your changes to the cloud or getting others' changes

### 2. **Development Workflow**
- **Local Development**: Working on your computer (what we're doing now)
- **Testing**: Making sure your code works before sharing
- **Documentation**: Explaining what your code does (like this README!)

### 3. **Pipeline/CI/CD** (Coming later!)
- **Pipeline**: Automated steps that test/build your code
- **Continuous Integration (CI)**: Automatically testing code when you make changes
- **Continuous Deployment (CD)**: Automatically releasing working code

## 🎯 Your First Project: Task Tracker

A command-line tool to manage your to-do list. Perfect for learning because:
- ✅ Simple enough to understand every line
- ✅ Complex enough to teach real concepts
- ✅ Actually useful for tracking your learning progress!

## 🛠️ How to Use

### Run the Task Tracker

```powershell
# Show all commands
python task_tracker.py

# Add a task
python task_tracker.py add "Learn what Git is"

# View your tasks
python task_tracker.py list

# Complete a task (use the ID from list)
python task_tracker.py complete 1

# Delete a task
python task_tracker.py delete 1
```

### Run Tests

```powershell
# Install test framework (one time only)
pip install pytest

# Run tests
python -m pytest test_task_tracker.py -v
```

## 📖 Learning Path

### Step 1: Get Git Started (You are here! 📍)
**Goal**: Understand what a repository is and make your first commit

```powershell
# Initialize Git in this folder (creates a "repository")
git init

# See what files Git notices
git status

# Add files to be tracked
git add .

# Make your first "commit" (snapshot)
git commit -m "Initial commit: Task tracker project"

# See your commit history
git log
```

**Concepts learned**: Repository, commit, staging, git status

### Step 2: Try Making Changes
**Goal**: Experience the edit-commit-repeat workflow

1. Use the task tracker to add a task about learning Git
2. Check what changed: `git status`
3. See exactly what's different: `git diff`
4. Add and commit your changes
5. View your history: `git log --oneline`

**Concepts learned**: Working directory, staging area, commit history

### Step 3: Create a Branch
**Goal**: Understand branches - the superpower of Git!

```powershell
# Create and switch to a new branch
git checkout -b feature/add-priority

# Make changes to the code (add a priority field to tasks)
# Then commit those changes

# Switch back to main
git checkout main

# See your branches
git branch
```

**Concepts learned**: Branching, switching contexts, isolated changes

### Step 4: Connect to GitHub
**Goal**: Put your code in the cloud (remote repository)

1. Create a GitHub account if you don't have one
2. Create a new repository on GitHub
3. Connect your local repo:
   ```powershell
   git remote add origin https://github.com/YOUR-USERNAME/task-tracker.git
   git push -u origin main
   ```

**Concepts learned**: Remote repository, push, origin, upstream

### Step 5: Make a Pull Request
**Goal**: Learn the team collaboration workflow

1. Create a new branch for a feature
2. Make changes and commit
3. Push the branch: `git push origin feature-name`
4. On GitHub, create a Pull Request
5. Review and merge it

**Concepts learned**: Pull requests, code review, merge

### Step 6: Add a Pipeline (Advanced!)
**Goal**: Automate testing with GitHub Actions

1. Create `.github/workflows/test.yml`
2. Configure it to run tests automatically
3. Push changes and watch it work!

**Concepts learned**: CI/CD, automation, GitHub Actions

## 🎓 Quick Reference

### Git Commands Cheatsheet
```powershell
git init                 # Start tracking this folder
git status              # What's changed?
git add <file>          # Stage a file for commit
git add .               # Stage all changes
git commit -m "message" # Save a snapshot
git log                 # View history
git branch              # List branches
git checkout -b <name>  # Create and switch to branch
git merge <branch>      # Merge branch into current
git push                # Send to GitHub
git pull                # Get changes from GitHub
```

### Task Tracker Commands
```powershell
python task_tracker.py list              # Show tasks
python task_tracker.py add "description" # Add task
python task_tracker.py complete <id>     # Mark done
python task_tracker.py delete <id>       # Remove task
```

## 💡 Ideas to Extend This Project

As you learn more, try adding:
- [ ] Task priorities (high, medium, low)
- [ ] Due dates for tasks
- [ ] Categories/tags
- [ ] Search functionality
- [ ] Color-coded output
- [ ] Export to CSV
- [ ] Web interface (Flask)
- [ ] Database storage (SQLite)

Each addition teaches new concepts while keeping the project manageable!

## 🆘 Common Issues

**"python not recognized"**
- Install Python from python.org
- Make sure to check "Add to PATH" during installation

**"git not recognized"**
- Install Git from git-scm.com
- Restart VS Code after installation

**"No module named pytest"**
- Install it: `pip install pytest`

## 🎉 Next Steps

1. **Start with Step 1** in the Learning Path above
2. Actually use the task tracker to manage your learning!
3. Add a task for each step you complete
4. Experiment! Break things and fix them - that's learning!

---

**Remember**: Every developer started exactly where you are. The only way to learn is to build, break, and fix things. You've got this! 💪
