import subprocess


def run_git_command(command):
    """
    Run a Git command and return the result.
    """

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return {
        "success": result.returncode == 0,
        "output": result.stdout + result.stderr
    }


def git_status():
    return run_git_command(
        ["git", "status", "--short"]
    )


def git_add_all():
    return run_git_command(
        ["git", "add", "."]
    )


def git_commit(message):
    return run_git_command(
        ["git", "commit", "-m", message]
    )


def git_push_developer():
    return run_git_command(
        ["git", "push", "origin", "developer"]
    )