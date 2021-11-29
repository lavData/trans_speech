from speech_2_text import speech_2_text
from trans_lt import trans_lt
import infor

apikey = infor.info().apikey_st
url = infor.info().url_st
content_type = "audio/mp3"
locate_file = "./hi.mp3"
respond = speech_2_text().tranfor(apikey=apikey,\
     url=url, content_type=content_type, locate_file=locate_file)

text = []
respond = respond.json()["results"]
for i in respond:
    text.append(i["alternatives"][0]["transcript"])

with open("text.txt", "w") as f:
    for i in text:
        f.write(i + "\n")

apikey = infor.info().apikey_tr
url = infor.info().utl_tr
content_type = "application/json"
text = respond
model_id = "en-vi"
version = "2020-10-23"

respond = trans_lt().trans(apikey=apikey, url=url, content_type=content_type\
    , text=text, model_id=model_id, version=version)

with open("trans.txt", "w") as f:
    for i in respond.json()["translations"]:
        f.write(str(i) + "\n")