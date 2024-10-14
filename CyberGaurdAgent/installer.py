import subprocess
from .utils import is_installed

def install_filebeat():
    """Install Filebeat if not already installed."""
    if is_installed('filebeat'):
        print("Filebeat is already installed.")
    else:
        print("Installing Filebeat...")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', 'filebeat', '-y'], check=True)
        print("Filebeat installed successfully.")
