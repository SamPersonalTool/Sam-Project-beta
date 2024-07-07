## General Description
SAM is a university project developed to fulfill the proposal of a system corresponding to the thesis work at the University of Margarita (UNIMAR), in the state of Nueva Esparta, Venezuela. SAM is a simple and effective alternative that seeks to offer users a new antimalware analysis system that can guarantee their security. Thanks to the free version of the VirusTotal API, SAM can perform analysis on URLs, in order to ensure the security of users against threats from the web. On the other hand, it can also perform analysis on files with a maximum weight of 32 MB.

## Description of the interaction between SAM and the VirusTotal API
Initially, a personal key for the VirusTotal API must be obtained, which will be encrypted using the "cryptography" library, which will generate two files, one with the personal API key being encrypted and another with the key necessary to decrypt the file that will have the encrypted key when the system modules are used. The "cryptography" library operates with the AES (Advanced Encryption Standard) symmetric encryption algorithm in CBC (Cipher Block Chaining) mode.

In the case of the module corresponding to URL analysis, SAM integrates the VirusTotal API through the use of the "requests" library, which is responsible for receiving the URL to be analyzed to send it to the API as a parameter, so that the API can return the analysis report and its identifier [id], which will be read locally by SAM to consult the results obtained and show them to the user.

In the case of the file analysis module, SAM receives the file, verifies if it weighs less than 32 MB, and identifies its MIME (Multipurpose Internet Mail Extension) type. Both the file and its MIME type are sent as parameters to the API so that it can perform the analysis and return the results, which will be consulted to display them to the user.

## Installation and Configuration Instructions
Currently, SAM only works on Windows 10 64-bit or higher. If you have the required operating system, you can proceed with the installation.

1- Enter the repository.

2- Download or clone the repository.

3- Install the necessary libraries for the code to function. (see: ## External Libraries Used)

4- Configure your personal VirusTotal API key within the code (to obtain your personal APIKey, you will need to log in to the VirusTotal website, create an account, and request the APIKey).

4.1- Copy and paste the personal VirusTotal API key into the "encrypt.py" file

4.2- Run the "encrypt.py" file, this will generate two files (key.key and encrypted_api_key.txt) which will be used to encrypt the API key and use it securely.

5- Compile the code using the setup.py file and the terminal command 
> python setup.py build

6- The previous step will generate a folder where the executable file called main.exe will be located.

## External Libraries Used:

- requests (v2.32.2)

- customtkinter (v5.2.2)

- pillow (v10.3.0)

- cryptography (v42.0.8)

- cx_Freeze (7.1.1)

(Check if these modules are installed using CMD)

> pip freeze

(If the modules are not installed, open CMD and enter)

> pip install module_name

example:

> pip install pillow

## Internal Libraries Used:

- webbrowser

- threading

- mimetypes

- time

- OS

## Usage
The system has a simple and intuitive graphical interface, with a main view where the buttons to access each function are displayed. The first button takes us to the LinkChecker function, the second button takes us to the FileChecker function, we have an Exit button that allows us to close the application, and we also have an "About Us" button that provides information to the user about the project developers.

Within the LinkChecker function, we have a text box where users can enter the selected URL, and then, with the "GO" button, the URL analysis will start. We also have a "CLEAN" button that will help users clear the existing data on the screen. Finally, we have a button to return to the main window.

Similarly, the view of the "FileCheker" function is very similar to the previous one, with the difference that it has a button that allows the user to open their file explorer and thus be able to select the file to be analyzed.

The results of the malware analyzes corresponding to each function will be displayed in the form of text with detailed analysis data.

## Contributions to Consider

1- Improve the graphical interface while maintaining simplicity and low resource consumption.

2- Develop an alternative to the VirusTotal API that allows breaking through the limitations it includes in its free version.

## License

This project is distributed under the terms of the MIT License. The MIT license is one of the most permissive and popular software licenses. It allows the use, copying, modification, merging, publication, distribution, sublicensing, and/or sale of the software, subject to the following conditions:

- The copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

- The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Software or the use or other dealings in the Software.

## Additional Resources

- Tkinter Documentation: https://docs.python.org/es/3/library/tk.html

- CustomTkinter Documentation: https://customtkinter.tomschimansky.com/documentation/

- VirusTotal API Documentation: https://docs.virustotal.com/reference/overview

- cx_Freeze Documentation: https://cx-freeze.readthedocs.io/en/stable/

- cryptography Documentation: https://cryptography.io/en/latest/
