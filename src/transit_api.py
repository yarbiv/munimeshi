import os
from typing import Optional
import requests


from dotenv import load_dotenv

from src.types import StopMonitoringResp

load_dotenv()

host = "http://api.511.org"
operators_endpoint = "transit/operators"
lines_endpoint = "transit/lines"
stops_endpoint = "transit/stops"

api_key = os.getenv("TRANSIT_API_KEY")

def get_stop_monitoring(operator: str, stop_id: Optional[str]) -> StopMonitoringResp:
    print(f"Getting stop monitoring for operator {operator} and stop_id {stop_id}")
    params = {"api_key": api_key, "agency": operator}
    if stop_id is not None:
        params["stopCode"] = stop_id
    resp = requests.get(f"{host}/transit/StopMonitoring", params=params)
    resp.encoding = "utf-8-sig"
    return resp.json()