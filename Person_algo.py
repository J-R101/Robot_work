import socket,pickle

import time
import Nao_interface as Nao
import lean_positions as LP
import Positions as P
import numpy as np
import positions_arrays as PA

#swinging algorithm to implemet rotational swinging algorithm with a desired offset from peaks of motion



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
calibration = [get_Encoder_data() - time.time() for i in range(200)]
cal_avg = np.average(calibration)
print("done")


offset = 0 #input offset for motion to be enacted before Naos motion
max_speed_frac = 1 # input desired fraction of max speed for motion to be completed in

Robo = Nao.Robot(Initailisation = True) # initialises robot class


while True:

    
    encoder_data = get_Encoder_data() # note encoder_data[0] is time of next negative peak, encoder_data[1] is time of next positive peak, and encoder_data[0] is time of equalibrium position
   # print(encoder_data[0]-time.time())

    
    

    # causes Nao to move torso back and kick legs out at back of swing motion with desired delay
    if np.abs(encoder_data[0]- time.time()-cal_avg-offset) < 0.08:
        Robo.new_move(max_speed_frac, PA.TBLO)


   
    # causes Nao to move torso forward and kick legs in at back of swing motion with desired delay
    if np.abs(encoder_data[1]- time.time()-cal_avg-offset) < 0.08:
        Robo.new_move(max_speed_frac, PA.TFLI)


        
s.close()