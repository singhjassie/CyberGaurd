import os
import subprocess

def configure_filebeat(siem_host, siem_port):
    """Configure Filebeat to send logs to the specified SIEM server."""
    filebeat_config_path = '/etc/filebeat/filebeat.yml'
    
    config_content = f"""
filebeat.inputs:
- type: syslog
  protocol.udp:
    host: "0.0.0.0:514"

output.elasticsearch:
  hosts: ["{siem_host}:{siem_port}"]
  protocol: "https"
  username: "your_username"
  password: "your_password"
  ssl.verification_mode: "none"

setup.kibana:
  host: "{siem_host}:5601"
"""

    try:
        with open(filebeat_config_path, 'w') as f:
            f.write(config_content)
        subprocess.run(['sudo', 'systemctl', 'enable', 'filebeat'], check=True)
        subprocess.run(['sudo', 'systemctl', 'start', 'filebeat'], check=True)
        print(f"Filebeat configured to send logs to {siem_host}:{siem_port}")
    except Exception as e:
        print(f"Error configuring Filebeat: {e}")
