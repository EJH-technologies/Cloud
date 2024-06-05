import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import os
import sys
import subprocess

def submit_values(event=None):
    email = email_entry.get()
    file_path = file_path_entry.get()
    number = number_entry.get()
    
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get the directory path of the executable
    executable_path = sys.executable
    executable_directory = os.path.dirname(executable_path)

    # Create the file paths in the executable's directory
    # input_file_path = os.path.join(executable_directory, "input_values.txt")
    log_file_path = os.path.join(executable_directory, "input_log.txt")

    try:
        # Save the values to the input file
       # with open(input_file_path, "w") as file:
       #     file.write(f"Email: {email}\n")
        #    file.write(f"File Path: {file_path}\n")
        #    file.write(f"Number: {number}\n")
        #print(f"Data saved to: {input_file_path}")
        
        # Append the values to the log file
        with open(log_file_path, "a") as log_file:
            log_file.write(f"Timestamp: {timestamp}\n")
            log_file.write(f"Email: {email}\n")
            log_file.write(f"Number: {number}\n")
            log_file.write("---\n")
        print(f"Data appended to: {log_file_path}")
        
        # Execute the PowerShell script
        powershell_script = os.path.join(executable_directory, "input_values.ps1")
        subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", powershell_script], shell=True)

        # Clear the input fields
        email_entry.delete(0, tk.END)
        file_path_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
        
        window.destroy()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)

# Create the main window
window = tk.Tk()
window.title("Jira Onboarding")

# Set the custom icon (replace "path/to/icon.ico" with the actual path to your icon file)
window.iconbitmap("C:\\Users\\matt.hebert\\OneDrive - Cybersoft Technologies\\Desktop\\CS_Icon.ico")

# Set the dialog box size
window.geometry("500x200")  # Adjust the size as needed (width x height)

# Configure the font style and size for labels and buttons
label_font = ("Arial", 12)  # Adjust the font style and size as needed
button_font = ("Arial", 10)  # Adjust the font style and size as needed

# Create and grid the input fields
email_label = tk.Label(window, text="Enter Your Email:", font=label_font)
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(window, font=label_font)
email_entry.grid(row=0, column=1, padx=5, pady=5)

file_path_label = tk.Label(window, text="Select API Key File:", font=label_font)
file_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
file_path_entry = tk.Entry(window, font=label_font)
file_path_entry.grid(row=1, column=1, padx=5, pady=5)
browse_button = tk.Button(window, text="Browse", command=browse_file, font=button_font)
browse_button.grid(row=1, column=2, padx=5, pady=5)

number_label = tk.Label(window, text="Ticket Number:", font=label_font)
number_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
number_entry = tk.Entry(window, font=label_font)
number_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(window, text="Create User", command=submit_values, font=button_font)
submit_button.grid(row=3, column=1, padx=5, pady=5)

# Bind 'Enter' key to submit_values function
window.bind('<Return>', lambda event: submit_values())

# Start the Tkinter event loop
window.mainloop()