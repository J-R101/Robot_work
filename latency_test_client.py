import socket,pickle
import numpy as np
import time

HOST = '192.168.1.100'  # The server's IP address: 192.168.1.100   For testing on local: 147.188.37.23
PORT = 10000        # The port used by the server: 10000   For testing on local: 1111 



#Mathews code used to test latency on laptop, i do not claim as my own 






def get_Encoder_data():
    # Call this function when you need the encoder data from the server
    # Output Large_angle_array in degrees (1), Small_angle_array in degrees (4) , time (1) in seconds
    # For small encoders angles relative to the robot swinging forward - top +, bottom -, bottom +, top - 
    
    s.sendall(pickle.dumps('Hello'))
    
    data = s.recv(4096)

    return pickle.loads(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
    
    ###### EXAMPLE that returns encoder data when enter is pressed ########
    # Add code in here and call get_Encoder_data() to get encoder data #


latency = [time.time() - get_Encoder_data() for i in range(1000)]
        
        
        
        
s.close()

print (np.average(latency))
print (np.std(latency))

#print (latency)

