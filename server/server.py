import socket
import pickle
import openvr_device
from pythonosc import udp_client
import time

# Set UDP server
UDP_IP = '192.168.0.2'
UDP_PORT = 56120
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Set OSC client
OSC_IP = '127.0.0.1'
OSC_PORT = 39570
client = udp_client.SimpleUDPClient('127.0.0.1', 39570)

# openvr setting
v = openvr_device.openvr_device()


def udp_get():
    data, addr = sock.recvfrom(65535)
    if not data:
        return False
    data = pickle.loads(data)
    return data


def osc_send(index, enable, timeoffset, px, py, pz, qx, qy, qz, qw):
    print(f"Device[{index}, {enable}, {timeoffset}]\n position[{px}, {py}, {pz}]\n rotation[{qx}, {qy}, {qz}, {qw}]")
    client.send_message("/VMT/Room/Unity", [index, enable, timeoffset, px, py, pz, qx, qy, qz, qw])


def hmd_device():
    return v.devices['hmd_1'].get_pose_quaternion()


def run():
    while True:
        data = udp_get()
        if data is None:
            time.sleep(0.001)
            continue
        if not data:
            time.sleep(0.001)
            continue
        print(data)

        # Get HMD pos, rot data
        hmd_data = hmd_device()
        if hmd_data is None:
            continue

        # calibrate pose data with HMD data
        hmd_x, hmd_y, hmd_z = hmd_data[0], hmd_data[1], hmd_data[2]
        calib_x = hmd_x - data[0][3]
        calib_y = hmd_y - data[0][4]
        calib_z = hmd_z - data[0][5]

        for i in range(len(data)):
            data[i][3] = data[i][3] + calib_x
            data[i][4] = data[i][4] + calib_y
            data[i][5] = data[i][5] + calib_z

            osc_send(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9])


if __name__ == "__main__":
    run()