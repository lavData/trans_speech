import json
import base64
import requests

class trans_lt:
    def __init__(self) -> None:
        self.apikey = None
        self.url = None
        self.headers = {}
        self.data = {}

    def trans(self, apikey, url, content_type, text, model_id, version):
        self.apikey = apikey
        self.url = f"{url}/v3/translate?version={version}"
    
        apikey = f"apikey:{self.apikey}"
        apikey_bytes = apikey.encode("ascii")
        base64_bytes = base64.b64encode(apikey_bytes)
        base64_apikey = base64_bytes.decode("ascii")

        self.headers["Content-Type"] = content_type
        self.headers["Authorization"] = f"Basic {base64_apikey}"

        self.data["text"] = text
        self.data["model_id"] = model_id
        data_json = json.dumps(self.data, indent=2)
        resp = requests.post(url=self.url, headers=self.headers, data=data_json)

        return resp