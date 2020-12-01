import requests
import re
import json

def getData():
    URL = 'https://covid19.saglik.gov.tr/'
    response = requests.get(URL)
    response.close()
    body = response.text
    regex = r"\[{(.*)}\]"
    matches = re.finditer(regex, body, re.MULTILINE)
    matchList = list(matches)
    data = matchList[0].group(0).strip()
    parsedData = json.loads(data)
    returnData = parsedData[0]
    return returnData