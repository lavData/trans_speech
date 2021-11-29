from abc import abstractproperty
import requests
import base64

class speech_2_text:
    def __init__(self) -> None:
        self.apikey = None
        self.url = None
        self.headers = {}
        self.locate_file = None


    def tranfor(self, apikey,url,content_type,locate_file):
        self.apikey = apikey
        self.url = f"{url}/v1/recognize"
        self.locate_file = locate_file

        apikey = f"apikey:{self.apikey}"
        apikey_bytes = apikey.encode("ascii")
        base64_bytes = base64.b64encode(apikey_bytes)
        base64_apikey = base64_bytes.decode("ascii")

        self.headers["Content-Type"] = content_type
        self.headers["Authorization"] = f"Basic {base64_apikey}"
        
        with open(self.locate_file, "rb") as f:
            data = f.read()
        resp = requests.post(url=self.url, headers=self.headers, data=data)

        return resp

# apikey = "8zsBWEW299pT0E6W8Eze5J0qN2K8CcgnCnyMDd7NM_fB"
# url = "https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/a5d5c76e-7a48-4a6a-b791-90dd324fa135"
# content_type = "audio/flac"
# locate_file = "./speech.flac"
# temp = speech_2_text().tranfor(apikey=apikey, url=url, content_type=content_type, locate_file=locate_file)
# print(temp.content)
