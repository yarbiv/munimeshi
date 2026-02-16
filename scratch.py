import os
import requests

from dotenv import load_dotenv

load_dotenv()

host = "http://api.511.org/"
operators_endpoint = "transit/operators"
lines_endpoint = "transit/lines"
stops_endpoint = "transit/stops"
stop_timetable_endpoint = "transit/StopMonitoring"

api_key = os.getenv("TRANSIT_API_KEY")
operator = "SF"
line_id="22"
stop_id="17763"

resp = requests.get(host + stop_timetable_endpoint, {"api_key": api_key, "agency": operator, "stopCode": stop_id})

print(resp.text)