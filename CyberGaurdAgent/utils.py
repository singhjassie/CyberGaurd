import subprocess

def is_installed(package_name):
    """Check if a package is installed."""
    try:
        subprocess.run([package_name, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
