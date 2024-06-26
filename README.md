# clip-replacer

## Description
README for File Replacement Tool
Overview
This README provides instructions on how to run the File Replacement Tool, a simple graphical application that allows users to replace files from a source directory to a destination directory on your Mac or PC. This tool uses Python and the Tkinter library for its graphical user interface.

Prerequisites
Before running the application, ensure that you have Python installed on your computer. This script has been tested with Python 3.8 and above. You can download and install Python from python.org.

## Installation
1. No installation is required for this script beyond having Python and the necessary libraries. However, you do need to ensure the Tkinter library, which usually comes with the Python installation. If not, you can install it via pip:
    ```bash
    pip install tk
    ```


## Running-The-Application

1. Save the provided Python script to a file named script.py on your computer.

2. Open Terminal or Command Prompt
macOS: Open Terminal from Applications > Utilities or search for it using Spotlight.
Windows: Search for Command Prompt and open it.
Navigate to the Script Location
Change to the directory where script.py is saved:
    ```bash
    cd path/to/your/script
    ```
Replace path/to/your/script with the actual file location.

3. Execute the Script
Run the script by typing:
    ```bash
    py script.py
    ```


## Usage
1. Select Source Directory: Click "Select" next to the Source Directory field to choose the directory from which files will be copied.


2. Select Destination Directory: Click "Select" next to the Destination Directory field to choose the target directory for file replacement.

3. Replace Files: With both directories selected, click "Replace Files". A message will confirm the success or report any errors.



## Troubleshoot
Tkinter not found: Confirm Python installation includes Tkinter or install it using pip.
Permission issues: Ensure you have appropriate read and write permissions for the directories you are accessing.

For further assistance, consult Python and Tkinter documentation or community forums such as StackOverflow.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.