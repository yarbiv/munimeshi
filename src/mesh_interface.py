import asyncio
from meshcore import MeshCore, EventType

PORT = "/dev/tty.usbserial-0001"
BAUDRATE = 115200

async def main():
    mc = await MeshCore.create_serial(PORT, BAUDRATE)

    print(mc.self_info)
    
    await mc.disconnect()

asyncio.run(main())