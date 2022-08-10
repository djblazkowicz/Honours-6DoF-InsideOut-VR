"""
Simple VIO result visualizer Python. Reads JSONL outputs from the
Spectacular AI SDK and plots them in real time.

Plug in the device to an USB3 port using an USB3 cable before running.

Modified to send VIO data via UDP socket on port 50000 - Gabor Nemeth 2022
"""
import json
import subprocess
import threading
import matplotlib.pyplot as plt
import os

import socket
import re

from time import sleep


#set up UDP socket
UDP_IP = "127.0.0.1"
UDP_PORT = 50000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


VIO_EXECUTABLE = './vio_jsonl'
if not os.path.isfile(VIO_EXECUTABLE): VIO_EXECUTABLE += ".exe"
if not os.path.isfile(VIO_EXECUTABLE): raise Exception("Couldn't find vio_jsonl binary!")

def read_vio():
    vio_process = subprocess.Popen([VIO_EXECUTABLE], stdout=subprocess.PIPE)
    while True:
        line = vio_process.stdout.readline()
        if not line: break
        # hacky, ignore any possible warnings from depthai in stdout
        # (which should not be there in the first place)
        if b'warning' in line: continue
        try:
            d = json.loads(line)
        except:
            # Swallow all exceptions from JSON parsing
            continue
        if 'position' not in d: continue
        #print(d[0])
        #print(d.position)
        yield(d)

def make_plotter():
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = Axes3D(fig)
    fig.add_axes(ax)

    ax_bounds = (-0.5, 0.5) # meters
    ax.set(xlim=ax_bounds, ylim=ax_bounds, zlim=ax_bounds)
    ax.view_init(azim=-140) # initial plot orientation

    vio_plot = ax.plot(
        xs=[], ys=[], zs=[],
        linestyle="-",
        marker="",
        #label='VIO trajectory',
    )
    #ax.legend()
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")

    title = ax.set_title("VIO trajectory")

    data = { c: [] for c in 'xyz' }

    control = { 'close': False }
    fig.canvas.mpl_connect('close_event', lambda _: control.update({'close': True}))

    def update_data(vio_out):
        if control['close']: return False
        for c in 'xyz':
            data[c].append(vio_out['position'][c])
        return True

    def update_graph(frames):
        x, y, z = [np.array(data[c]) for c in 'xyz']
        vio_plot[0].set_data(x, y)
        vio_plot[0].set_3d_properties(z)
        # plt.draw()
        # plt.pause(0.01)
        return (vio_plot[0],)

    from matplotlib.animation import FuncAnimation
    anim = FuncAnimation(fig, update_graph, interval=15, blit=True)
    return update_data, anim

if __name__ == '__main__':
    plotter, anim = make_plotter()

    def reader_loop():
        for vio_out in read_vio():

            X = '%+.04f' % vio_out['position']['x']
            Y = '%+.04f' % vio_out['position']['z']
            Z = '%+.04f' % vio_out['position']['y']
            Z = float(Z) * -1
            qW = '%+.04f' % vio_out['orientation']['z']
            qX = '%+.04f' % vio_out['orientation']['w']
            qY = '%+.04f' % vio_out['orientation']['y']
            qZ = '%+.04f' % vio_out['orientation']['x']

            XS = str(X).replace('+','')
            YS = str(Y).replace('+','')
            ZS = str(Z).replace('+','')
            qWS = str(qW).replace('+','')
            qXS = str(qX).replace('+','')
            qYS = str(qY).replace('+','')
            qZS = str(qZ).replace('+','')
            output_data = (XS + ' ' + YS + ' ' + ZS + ' ' + qWS + ' ' + qXS + ' ' + qYS + ' ' + qZS + ' ')
            sock.sendto(bytes(output_data, "utf-8"), (UDP_IP, UDP_PORT))
            print(output_data)
            if not plotter(vio_out): break

    reader_thread = threading.Thread(target = reader_loop)
    reader_thread.start()
    plt.show()
    reader_thread.join()
