import requests
import config
import time

class URLCheckerModule:
    def analyze_url(my_link):
        #api origin
        url = "https://www.virustotal.com/api/v3/urls"
        #container for the link
        payload = { "url":my_link }
        #parameters
        my_api_key = config.decrypted_api_key
        headers = {
            "accept": "application/json",
            "x-apikey": my_api_key,
            "content-type": "application/x-www-form-urlencoded"
        }
        #result of the analysis
        response = requests.post(url, data=payload, headers=headers)
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
        stats = f"Analysis Results for\n[{payload['url']}]: \nMalicious: {stat1}\nSuspicious: {stat2}\nUndetected: {stat3}\nHarmless: {stat4}"
        #getting comments on the results
        comments = []
        comments.append(stats)
        comments.append("Comments about your analysis:")
        if stat1 != 0 or stat2 != 0:
            comments.append(">> Direct report <<")
            for name in newresponse_dict["data"]["attributes"]["results"]:
                category_result = newresponse_dict["data"]["attributes"]["results"][name]["result"]
                if category_result != "clean" and category_result != "unrated":
                    name_result = newresponse_dict["data"]["attributes"]["results"][name]["engine_name"]
                    comments.append(f"By {name_result}: {category_result}")
            comments.append(">> Your page could be used for: <<")
            newurl2 = f"https://www.virustotal.com/api/v3/analyses/{scan_id}/item"
            newresponse2 = requests.get(newurl2, headers=headers)
            newresponse2_dict = newresponse2.json()
            for name in newresponse2_dict["data"]["attributes"]["categories"]:
                description = newresponse2_dict["data"]["attributes"]["categories"][name]
                comments.append(f"By {name}: For {description}")
            comments.append(">> Be careful using this page <<")
        else:
            comments.append("This page is out of threats :)")
        rows = f"{'\n'.join(str(i) for i in comments)}"
        return rows
URLcm = URLCheckerModule