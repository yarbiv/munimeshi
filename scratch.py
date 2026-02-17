import json

from src.transit_api import get_stop_monitoring
from src.types import StopMonitoringResp

operator = "SF"
line_id="22"
stop_id="13291"

resp: StopMonitoringResp = get_stop_monitoring(operator, stop_id=stop_id)

stops_by_line_and_id = {}
for stop in resp["ServiceDelivery"]["StopMonitoringDelivery"]["MonitoredStopVisit"]:
    line = stop["MonitoredVehicleJourney"]["LineRef"]
    stop_id = stop["MonitoringRef"]
    lines = stops_by_line_and_id.get(stop_id, {})
    stops = lines.get(line, [])
    stops.append(stop)
    lines[line] = stops 
    stops_by_line_and_id[stop_id] = lines

with open("sample_output/16th_mission_grouped_trips.json", "w") as f:
    json.dump(stops_by_line_and_id, f, indent=2)