from .config_manager import check_config, create_config, load_config
from .installer import install_filebeat
from .configurator import configure_filebeat

def main():
    # Step 1: Check for configuration file
    if not check_config():
        create_config()

    # Step 2: Load SIEM configuration
    config = load_config()
    siem_host = config['siem_host']
    siem_port = config['siem_port']

    # Step 3: Install Filebeat if not installed
    install_filebeat()

    # Step 4: Configure Filebeat to send logs to the SIEM
    configure_filebeat(siem_host, siem_port)

if __name__ == "__main__":
    main()
