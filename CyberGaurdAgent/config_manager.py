import os
import json

CONFIG_FILE_PATH = os.path.expanduser("~/.filebeat_config.json")

def check_config():
    """Check if configuration file exists."""
    return os.path.isfile(CONFIG_FILE_PATH)

def create_config():
    """Create configuration file with remote SIEM server details."""
    siem_host = input("Enter your SIEM server IP/Hostname: ")
    siem_port = input("Enter your SIEM server port: ")

    config_data = {
        "siem_host": siem_host,
        "siem_port": siem_port
    }

    with open(CONFIG_FILE_PATH, 'w') as config_file:
        json.dump(config_data, config_file)
    print(f"Configuration saved to {CONFIG_FILE_PATH}.")

def load_config():
    """Load configuration file."""
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        return json.load(config_file)
