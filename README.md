# Exploit Automation Toolkit Documentation
###THIS TOOL IS UNDERDEVELOPMENT
## Introduction

The NightShadeOps Toolkit provides a collection of scripts written in Python for automating various tasks involved in penetration testing and exploit development.

## Functionality

### Payload Generation

- **Generate Reverse Shell Payload**: Generates reverse shell payloads for Linux, Windows, and macOS.
- **Generate Bind Shell Payload**: Generates bind shell payloads for Linux.

### File Manipulation

- **Encrypt File**: Encrypts a specified file using 7-Zip.
- **Hide Payload**: Embeds a payload file within an image using steganography.
- **Exfiltrate Data**: Exfiltrates a file to a specified URL using curl.
- **Manipulate Data**: Performs text replacement within a file using sed.

### System Manipulation

- **Escalate Privileges**: Runs LinPEAS script to identify privilege escalation opportunities.
- **Establish Persistence**: Appends a cron job to the user's crontab for persistence.

### Analysis and Networking

- **Evade Antivirus Detection**: Scans a payload file for antivirus detection using clamscan.
- **Connect Reverse Shell**: Connects to a reverse shell using Netcat.
- **Analyze Traffic**: Captures network traffic using tcpdump.
- **List Files**: Lists files in the current directory.

### Post-Exploitation

- **Automate Post-Exploitation**: Launches Metasploit Framework console for automated post-exploitation tasks.

## Usage

1. Clone the repository to your local machine.
2. Ensure all prerequisites are installed and configured.
3. Run the `NightShadeOps.py` script using Python.
4. Follow the on-screen menu to choose the desired functionality.

## Contributing

Contributions are welcome! If you'd like to add new features, improve existing ones, or fix bugs, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

