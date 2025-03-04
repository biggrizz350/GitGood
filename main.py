import tkinter as tk
import random

# Simulated repository state
repo = {
    "initialized": False,
    "name": "",
    "staged_files": [],
    "commits": [],
    "branches": ["main"],
    "current_branch": "main"
}

# Git quiz questions with more complexity
quiz_questions = [
    ("How do you check the status of your repository?", "git status"),
    ("How do you create a new branch called 'feature' and switch to it?", "git checkout -b feature"),
    ("How do you stage all changes for commit?", "git add ."),
    ("How do you commit changes with a message?", "git commit -m 'message'"),
    ("How do you push changes to the remote repository?", "git push"),
    ("How do you pull the latest changes from the remote repository?", "git pull"),
    ("How do you merge the 'feature' branch into 'main'?", "git merge feature"),
    ("How do you list all branches?", "git branch"),
    ("How do you switch to an existing branch called 'dev'?", "git checkout dev"),
    ("How do you create a new branch named 'test' without switching to it?", "git branch test"),
    ("How do you delete a local branch called 'old-feature'?", "git branch -d old-feature"),
    ("How do you pull from a remote repository called 'alpha'?", "git pull origin alpha"),
    ("How do you rebase the current branch onto 'main'?", "git rebase main"),
    ("How do you stash changes temporarily?", "git stash"),
    ("How do you apply the last stashed changes?", "git stash pop")
]

current_quiz = None
quiz_active = False

def ask_quiz_question():
    global current_quiz
    current_quiz = random.choice(quiz_questions)
    return current_quiz[0]

def check_quiz_answer(answer):
    global current_quiz
    if answer.strip().lower() == current_quiz[1]:
        return "Correct!" + "\n" + ask_quiz_question()
    else:
        return f"Incorrect. The correct answer is: {current_quiz[1]}" + "\n" + ask_quiz_question()

def on_enter(event):
    global current_quiz, quiz_active
    current_index = text_area.index("insert")
    
    last_line_start = text_area.search("PS C:\\Users\\User>", current_index, backwards=True, stopindex="1.0")
    if last_line_start:
        command_start = f"{last_line_start} + 17 chars"
        user_input = text_area.get(command_start, "end-1c").strip()
        
        if quiz_active:
            if user_input.lower() == "stop":
                quiz_active = False
                output = "Quiz session ended."
            else:
                output = check_quiz_answer(user_input)
        else:
            output = process_command(user_input)
        
        text_area.insert("end", f"\n{output}\nPS C:\\Users\\User> ")
        text_area.see("end")  
        text_area.mark_set("insert", "end")  
        
        return "break"

def process_command(command):
    global repo
    parts = command.split()
    if not parts:
        return ""
    
    cmd = parts[0].lower()
    if cmd == "git":
        if len(parts) < 2:
            return "git: missing command"
        
        subcommand = parts[1].lower()
        
        if subcommand == "init":
            repo_name = parts[2] if len(parts) > 2 else "my_project"
            repo["initialized"] = True
            repo["name"] = repo_name
            repo["staged_files"].clear()
            repo["commits"].clear()
            return f"Initialized empty Git repository in C:/Users/User/{repo_name}/.git/"
        
        elif subcommand == "branch":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            if len(parts) == 2:
                return "\n".join([f"* {b}" if b == repo["current_branch"] else f"  {b}" for b in repo["branches"]])
            new_branch = parts[2]
            if new_branch in repo["branches"]:
                return f"fatal: A branch named '{new_branch}' already exists."
            repo["branches"].append(new_branch)
            return f"Branch '{new_branch}' created."
        
        elif subcommand == "checkout":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            if len(parts) < 3:
                return "git checkout: missing branch name"
            if parts[2] == "-b":
                new_branch = parts[3] if len(parts) > 3 else ""
                if not new_branch:
                    return "git checkout -b: missing branch name"
                if new_branch in repo["branches"]:
                    return f"fatal: A branch named '{new_branch}' already exists."
                repo["branches"].append(new_branch)
                repo["current_branch"] = new_branch
                return f"Switched to a new branch '{new_branch}'"
            else:
                branch_name = parts[2]
                if branch_name not in repo["branches"]:
                    return f"error: pathspec '{branch_name}' did not match any file(s) known to git"
                repo["current_branch"] = branch_name
                return f"Switched to branch '{branch_name}'"
                
        elif subcommand == "status":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            staged = ", ".join(repo["staged_files"]) if repo["staged_files"] else "No changes staged for commit."
            return f"On branch {repo['current_branch']}\n{staged}"
        
        elif subcommand == "add":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            file = parts[2] if len(parts) > 2 else "all changes"
            repo["staged_files"].append(file)
            return f"{file} staged for commit."
        
        elif subcommand == "commit":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            if not repo["staged_files"]:
                return "nothing to commit, working tree clean"
            commit_msg = " ".join(parts[3:]) if len(parts) > 3 else "No message"
            repo["commits"].append({"message": commit_msg, "files": repo["staged_files"][:]})
            repo["staged_files"].clear()
            return f"[{repo['current_branch']}] {commit_msg}"
        
        elif subcommand == "push":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            if not repo["commits"]:
                return "Everything up-to-date"
            repo["remote_repo"].extend(repo["commits"])
            repo["commits"].clear()
            return f"Pushed commits to remote repository on branch {repo['current_branch']}."
        
        elif subcommand == "pull":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            return f"Pulled latest changes from remote repository into {repo['current_branch']}."
        
        elif subcommand == "merge":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            branch = parts[2] if len(parts) > 2 else ""
            if branch and branch in repo["branches"]:
                return f"Merged {branch} into {repo['current_branch']} successfully."
            return "Merge failed: Branch does not exist."
        
        elif subcommand == "rebase":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            base_branch = parts[2] if len(parts) > 2 else "main"
            if base_branch in repo["branches"]:
                return f"Rebased {repo['current_branch']} onto {base_branch}."
            return "Rebase failed: Branch does not exist."
        
        elif subcommand == "stash":
            if not repo["initialized"]:
                return "fatal: not a git repository"
            repo["stashed_changes"].append("Stashed changes")
            return "Changes stashed."
        
        elif subcommand == "stash" and len(parts) > 2 and parts[2] == "pop":
            if repo["stashed_changes"]:
                repo["stashed_changes"].pop()
                return "Stashed changes reapplied."
            return "No stashed changes to apply."
        
        elif subcommand == "reset":
            return "Repository reset to previous state."

        elif subcommand == "quizzed":
            global quiz_active
            quiz_active = True
            return ask_quiz_question()
        
        elif subcommand == "help":
            return "\n".join([
                "git init - Initialize a new Git repository",
                "git status - Show the working tree status",
                "git add - Stage files for commit",
                "git commit - Record changes to the repository",
                "git push - Upload changes to a remote repository",
                "git pull - Fetch and integrate changes from remote",
                "git branch - Manage branches",
                "git checkout - Switch branches",
                "git merge - Merge branches",
                "git rebase - Reapply commits on top of another base",
                "git stash - Temporarily store changes",
                "git reset - Reset current HEAD to a specified state",
                "git quizzed - Start a Git quiz session"
            ])
        
        else:
            return f"git: '{subcommand}' is not a git command"
    
    return f"{command}: command not found"

root = tk.Tk()
root.title("Windows PowerShell")
root.configure(bg="#012456")
root.geometry("800x500")

text_area = tk.Text(root, bg="#012456", fg="white", font=("Consolas", 12),
                    insertbackground="white", wrap="word", borderwidth=0)
text_area.pack(expand=True, fill="both")
text_area.insert("end", "Practice your Git commands here and use 'git quizzed' to be tested.\n\n")
text_area.insert("end", "Windows PowerShell\nCopyright (C) Microsoft Corporation. All rights reserved.\n\nPS C:\\Users\\User> ")
text_area.bind("<Return>", on_enter)
text_area.mark_set("insert", "end")
text_area.focus_set()
root.mainloop()