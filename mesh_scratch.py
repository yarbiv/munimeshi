import asyncio
from meshcore import MeshCore, EventType

from src.transit_api import get_stop_monitoring

import pprint

# PORT = "/dev/tty.usbserial-0001"
PORT = "/dev/tty.usbmodem8CFD49B543041"
BAUDRATE = 115200

async def main():
    mc = await MeshCore.create_serial(PORT, BAUDRATE)

    # Get contacts and send to a specific one
    resp = get_stop_monitoring("SF", "15401")
    stops_by_line_and_id = {}
    for stop in resp["ServiceDelivery"]["StopMonitoringDelivery"]["MonitoredStopVisit"]:
        line = stop["MonitoredVehicleJourney"]["LineRef"]
        stop_id = stop["MonitoringRef"]
        lines = stops_by_line_and_id.get(stop_id, {})
        stops = lines.get(line, [])
        stops.append(stop)
        lines[line] = stops 
        stops_by_line_and_id[stop_id] = lines

    print(str(stops_by_line_and_id))
    
    await mc.commands.send_chan_msg(1, str(stops_by_line_and_id)[0:100])
    result = await mc.commands.get_contacts()
    if result.type == EventType.ERROR:
        print(f"Error getting contacts: {result.payload}")
    else:
        contacts = result.payload
        for key, contact in contacts.items():
            print(key, contact)
        #     if contact["adv_name"] == "Alice":
        #         # Option 1: Pass the contact object directly
        #         result = await meshcore.commands.send_msg(contact, "Hello Alice!")
        #         if result.type == EventType.ERROR:
        #             print(f"Error sending message: {result.payload}")
                
        #         # Option 2: Use the public key string
        #         result = await meshcore.commands.send_msg(contact["public_key"], "Hello again Alice!")
        #         if result.type == EventType.ERROR:
        #             print(f"Error sending message: {result.payload}")
                
        #         # Option 3 (backward compatible): Convert the hex key to bytes
        #         dst_key = bytes.fromhex(contact["public_key"])
        #         result = await meshcore.commands.send_msg(dst_key, "Hello once more Alice!")
        #         if result.type == EventType.ERROR:
        #             print(f"Error sending message: {result.payload}")
        #         break

        # # You can also directly use a contact found by name
        # contact = meshcore.get_contact_by_name("Bob")
        # if contact:
        #     result = await meshcore.commands.send_msg(contact, "Hello Bob!")
        #     if result.type == EventType.ERROR:
        #         print(f"Error sending message: {result.payload}")  
                
        await mc.disconnect()

asyncio.run(main())