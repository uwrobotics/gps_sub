import lcm
from ins import ins_t

def my_handler(channel, data):
    msg = ins_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print('time: ', msg.time)
    print('week: ', msg.week)
    print('utcTime: ', msg.utcTime)
    print('insStatus: ', msg.insStatus)
    print('yaw: ', msg.yaw)
    print('pitch: ', msg.pitch)
    print('roll: ', msg.roll)
    print('latitude: ', msg.latitude)
    print('longitude: ', msg.longitude)
    print('altitude: ', msg.altitude)
    print('nedVelX: ', msg.nedVelX)
    print('nedVelY: ', msg.nedVelY)
    print('nedVelZ: ', msg.nedVelZ)

lc = lcm.LCM()
subscription = lc.subscribe("loc-ins", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass