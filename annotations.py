# This script gives you all annotations and COG letter (even repeated ones)

import re                                                          # Import the package
import os                                                          # Import the package

Data = []                                                          # Create an empty list to store the future obtained data
cwd = os.getcwd()                                                  # Gets the current work directory
#print(cwd)
files = os.listdir(cwd)                                            # Store in the variable "files" all the files in the variable "cwd" (which is the current directory)
#print(len(files))

for i in range (len(files)):                                       # To iterate through all files in directory
    for file in files:                                             # For each file in "files" variable do:
#if str(file).endswith(".annotations"):                            # This line is if you only want to read an specific type of file ) ej: you can ignore the .py files
        with open (file, "r") as f:                                # Open file in "files" as "f" variable
            for lines in f:                                        # Read through each line of the file (one by one)
                no_enter = lines.strip()                           # Strip (divide) each line and store it in "no_enter" variable
                if not no_enter.startswith("#") :                  # If "no_enter" (the line in the file) NOT starts with "#", do:
                    splited_lines = re.split("\t+", no_enter)      # Split the lines in "no enter" by tabs (\t+) and store them in "splited lines"
                    #print(splited_lines)
                    Data.append(splited_lines[-2:])                # Append the last 2 columns of "splited_lines" in the "Data" list (which is COG letter and annotation)

print(Data)
#print(len(Data))
