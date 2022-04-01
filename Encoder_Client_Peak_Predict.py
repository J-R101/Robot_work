import socket,pickle

import time
import Nao_interface as Nao
import lean_positions as LP
import Positions as P
import numpy as np
import positions_arrays as PA


HOST = '192.168.1.100'  # The server's IP address: 192.168.1.100   For testing on local: 147.188.37.23
PORT = 10000        # The port used by the server: 10000   For testing on local: 1111 







def get_Encoder_data():
    # Call this function when you need the encoder data from the server
    # Output Large_angle_array in degrees (1), Small_angle_array in degrees (4) , time (1) in seconds
    # For small encoders angles relative to the robot swinging forward - top +, bottom -, bottom +, top - 
    
    s.sendall(pickle.dumps('Hello'))
    
    data = s.recv(4096)
    
    return pickle.loads(data)


s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

Robo = Nao.Robot(Initailisation = True)





while True:

    
    encoder_data = get_Encoder_data()

    
    # print(encoder_data[0]- time.time())

    start = time.time()
    if np.abs(encoder_data[0]- time.time()) < 0.037:
        Robo.move_proxy.setAngles("RKneePitch", 0, 1, True)
        Robo.move_proxy.setAngles("LKneePitch", 0, 1, True)
    end = time.time()

    print(start-end)

    if np.abs(encoder_data[1]- time.time()) < 0.037:
        Robo.move_proxy.setAngles("RKneePitch", 1.4,1,  True)
        Robo.move_proxy.setAngles("LKneePitch", 1.4,1,  True)
    


 

  







        
s.close()