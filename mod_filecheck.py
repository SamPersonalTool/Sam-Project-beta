#libraries
import requests
import config
import os

class FileCheckerModule:
    def validate_file(my_path):
        my_file_size = os.path.getsize(my_path) / (1024 * 1024) #convert bytes to MB
        if my_file_size > 32:
            invalid_file_warning = f"File exceeds size limit (up to 32 MB) \n(Your file is: {my_file_size:.2f} MB)"
            return invalid_file_warning
        else:
            analyzed_file = FileCheckerModule.analyze_file(my_path)
            return analyzed_file
    def find_file_type(file_extension):
        if file_extension == ".txt":
            my_file_type = "text/plain"
            return my_file_type
        elif file_extension == ".py":
            my_file_type = "text/x-python"
            return my_file_type
        elif file_extension == ".sql":
            my_file_type = "application/octect-stream"
            return my_file_type
        elif file_extension == ".exe":
            my_file_type = "application/x-msdownload"
            return my_file_type
        elif file_extension == ".rar":
            my_file_type = "application/x-compressed"
            return my_file_type
        elif file_extension == ".pdf":
            my_file_type = "application/pdf"
            return my_file_type
        elif file_extension == ".png":
            my_file_type = "image/png"
            return my_file_type
        elif file_extension == ".jpg":
            my_file_type = "image/jpeg"
            return my_file_type
        else:
            return "Invalid Type"
    def analyze_file(my_file):
        #Obtaining parameters
        file_name = my_file.split("/")[-1]
        file_extension = "."+file_name.split(".")[-1]
        file_type = FileCheckerModule.find_file_type(file_extension)

        #api origin
        url = "https://www.virustotal.com/api/v3/files"

        #container for the file
        files = {"file": (file_name, open(my_file, "rb"), file_type)}
        #parameters
        my_api_key = config.decrypted_api_key
        headers = {
            "accept": "application/json",
            "x-apikey": my_api_key
        }
        #result of the analysis
        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 200:
            response_dict = response.json()
            scan_id = response_dict["data"]["id"]
        else:
            rsc = f"Error code: {response.status_code}, retry your analysis later"
            return rsc
        #getting the results
        newurl = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
        newresponse = requests.get(newurl, headers=headers)
        newresponse_dict = newresponse.json()
        stat1 = newresponse_dict["data"]["attributes"]["stats"]["malicious"]
        stat2 = newresponse_dict["data"]["attributes"]["stats"]["suspicious"]
        stat3 = newresponse_dict["data"]["attributes"]["stats"]["undetected"]
        stat4 = newresponse_dict["data"]["attributes"]["stats"]["harmless"]
        stats = f"Analysis Results: \nMalicious: {stat1}\nSuspicious: {stat2}\nUndetected: {stat3}\nHarmless: {stat4}"
        return stats
FILEcm = FileCheckerModule