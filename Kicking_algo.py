import socket,pickle

import time
import Nao_interface as Nao
import lean_positions as LP
import Positions as P
import numpy as np
import positions_arrays as PA

#basic test just to get Nao to kick at peaks of motion






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
calibration = [get_Encoder_data() - time.time() for i in range(200)] # calibration needed as encoders seem to develop offset values between sessions
cal_avg = np.average(calibration)



Robo = Nao.Robot(Initailisation = True)




legs = ["RKneePitch", "LKneePitch"]
while True:

    
    encoder_data = get_Encoder_data()

    
  

    # so if the time of the next peak predicted by peak predict minus the current time is below 0.08 Nao will enact motion ( note less than used as they will only match up perfectly occasionally due to latency)


    #kick legs out at forward max
    if np.abs(encoder_data[0]- time.time()-cal_avg) < 0.08:
        Robo.move_proxy.angleInterpolation(legs, [-0.09, -0.09],  0.24, True)
    

    
#tuck legs in at negative max
    if np.abs(encoder_data[1]- time.time()-cal_avg) < 0.08:
        Robo.move_proxy.angleInterpolation(legs, [1.4, 1.4],  0.24, True)


 

  







        
s.close()