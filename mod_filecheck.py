#libraries
import requests
import config
import mimetypes
import time
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
    def analyze_file(my_file):
        #Obtaining parameters
        file_name = my_file.split("/")[-1]
        mime_type = mimetypes.guess_type(file_name)[0]

        #api origin
        url = "https://www.virustotal.com/api/v3/files"

        #container for the file
        files = {"file": (file_name, open(my_file, "rb"), mime_type)}
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
        time.sleep(20)
        newurl = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
        newresponse = requests.get(newurl, headers=headers)
        newresponse_dict = newresponse.json()
        stat1 = newresponse_dict["data"]["attributes"]["stats"]["malicious"]
        stat2 = newresponse_dict["data"]["attributes"]["stats"]["suspicious"]
        stat3 = newresponse_dict["data"]["attributes"]["stats"]["undetected"]
        stat4 = newresponse_dict["data"]["attributes"]["stats"]["harmless"]
        head = f"Analysis Results for\n[{file_name}]:"
        stats = f"Malicious: {stat1}\nSuspicious: {stat2}\nUndetected: {stat3}\nHarmless: {stat4}"
        #getting comments on the results
        comments = []
        comments.append(head)
        if stat1 != 0 or stat2 != 0:
            comments.append(stats)
            comments.append("Comments about your analysis:")
            comments.append(">> Direct report <<")
            for name in newresponse_dict["data"]["attributes"]["results"]:
                category_result = newresponse_dict["data"]["attributes"]["results"][name]["result"]
                if category_result != "clean" and category_result != "unrated":
                    name_result = newresponse_dict["data"]["attributes"]["results"][name]["engine_name"]
                    comments.append(f"By {name_result}: {category_result}")
            comments.append(">> Be careful using this file <<")
        elif stat1 == 0 and stat2 == 0 and stat3 == 0 and stat4 == 0:
            #If API does not respond:
            c1 = "Direct data from your analysis is not available now \nRetry your analysis later."
            comments.append(c1)
        else:
            comments.append(stats)
            comments.append("This file is out of threats :)")
        rows = f"{'\n'.join(str(i) for i in comments)}"
        return rows
FILEcm = FileCheckerModule