import naoqi
from naoqi import ALProxy
import lean_positions
import Positions as P
import lean_positions as LP
import numpy as np
import positions_arrays as PA
import time as time

class Robot():
    """Defines the class to access the robot which will have act as the way to interface with Nao"""

    def __init__(self, ip="192.168.1.3", port=9559, Initailisation = False):

        """sets up connection to Nao, initialises proxys's and sets Nao to initial position


        ip: string, ip adress of Nao
        port: int, port number as to access Nao
        
        """

        self.move_proxy = ALProxy("ALMotion", ip, port)
        self.mem_proxy = ALProxy("ALMemory", ip, port)
        self.tts = ALProxy("ALTextToSpeech", ip, port)
        self.move_proxy.setStiffnesses(P.neutral_pos.keys(), 1)

        if Initailisation == True:
            self.move_proxy.angleInterpolation(P.neutral_pos.keys(),P.neutral_pos.values(), 2, True)


    def read_acceleration(self):
        """function that finds current acceleration data from Nao's inertial system, with the XYZ values being along Nao's internal axis, all data in meters per secons. Note how data from Nao's inertial data is susceptible
        to some offset of the true value
        
    

        Returns: list containing accerlation along Nao's X-axis, Y-axis and Z-axis
        """

        Acc_x = Mem_proxy.getData('Device/SubDeviceList/InertialSensor/AccelerometerX/Sensor/Value')
        Acc_y = Mem_proxy.getData('Device/SubDeviceList/InertialSensor/AccelerometerY/Sensor/Value')
        Acc_z = Mem_proxy.getData('Device/SubDeviceList/InertialSensor/AccelerometerZ/Sensor/Value')

        return [Acc_x, Acc_y, Acc_z]



    def read_gyroscope(self):
        """function that finds current gyroscope data from Nao's inertial system, with the XYZ values being along Nao's internal axis, all data in radians per second. Note how data from Nao's inertial data is susceptible
        to some offset of the true value
        
    

        Returns: list containing angular velocity about Nao's X-axis, Y-axis and Z-axis
        """

        Gyr_x = Mem_proxy.getData('Device/SubDeviceList/InertialSensor/GyroscopeX/Sensor/Value')
        Gyr_y = Mem_proxy.getData('Device/SubDeviceList/InertialSensor/GyroscopeY/Sensor/Value')
        Gyr_z = Mem_proxy.getData('Device/SubDeviceList/InertialSensor/GyroscopeZ/Sensor/Value')

        return [Gyr_x, Gyr_y, Gyr_z]

    
    def talk(self):
        self.tts.say("hello")



    def position_change(self, speed_frac, pos_frac, end_pos):

        current_pos = self.Position_measure()
        dist = LP.Ang_distance(current_pos, end_pos)

        target_pos= {}

        for key in end_pos:
            target_pos[key] = (dist[key]*pos_frac) + current_pos[key]


        # print(end_pos)
        # print(target_pos)


        dist = LP.Ang_distance(current_pos, target_pos)
        fastest_time = LP.quickest_time(current_pos, target_pos)[1]

        #print(fastest_time)
        self.move_proxy.angleInterpolation(target_pos.keys(), target_pos.values(), fastest_time/(speed_frac), True )
   

    def current_pos_array(self):
        joints = [
            'LShoulderPitch',
            'LHipPitch',
            'LElbowYaw',
            'LAnklePitch',
            'LWristYaw', 
            'RWristYaw', 
            'HeadYaw' , 
            'RHipPitch', 
            'HeadPitch', 
            'RElbowYaw', 
            'RShoulderPitch', 
            'RKneePitch', 
            'LShoulderRoll', 
            'RHipYawPitch',  
            'RShoulderRoll', 
            'LHipYawPitch',  
            'LAnkleRoll',  
            'RAnklePitch', 
            'LKneePitch',  
            'LHipRoll',  
            'RAnkleRoll',  
            'LElbowRoll',  
            'RElbowRoll', 
            'RHipRoll']

        current_pos = np.zeros(24)

        current_angles = self.move_proxy.getAngles(joints, True)
        return np.array(current_angles)


    def new_move(self, speed_frac, end_pos):
                """ takes in a fraction of max speed as well a target position as an array with the order of the joints illustrated position arrays
        Args:
            end_pos = array of final joint position angles in radians and in order  illustrated in position arrays
            speed_frac = fraction of max speed for movement to be completed in 

            
        returns
            move Nao to desired position at desired fraction of speed in a smooth motion
        """





        current_pos = self.current_pos_array()

        dist = np.abs(np.array(end_pos) - current_pos)
        
        
        longest_time = np.max(dist/PA.max_speeds)


        


        self.move_proxy.angleInterpolation(PA.joints, end_pos, longest_time/(speed_frac), True)


    def leg_kick_out(self):   
        self.move_proxy.angleInterpolation(LP.leg_forward.keys(), LP.leg_forward.values(), 0.46, True )

    def leg_kick_in(self):
        self.move_proxy.angleInterpolation(LP.leg_back.keys(), LP.leg_back.values(), 0.46, True )


    def setAng(self, joint, angle, speed):
        self.move_proxy.setAngles(joint, angle, speed)



    def mirrored(self, pos_dict):

        """ Takes a position dictionary and mirrors all positions of the joints on the left of Nao to the right and returns the
        symetrical position dictionary, but not for some joints when mirrored require a change of signa as to make Nao symetric
            
        Args:
            pos_dict = position dictionary for which the joints on the left shall be mirrored to the right

            
        returns
            mirrored_pos = dictionary of positions of Nao's joints mirrored such that hes symetric

        """
            #takes position dict and correctly mirrors left to right side and accounts for sign
        mirrored_pos = pos_dict.copy()

        for key in mirrored_pos:
            if key[0] == 'R':
                r = mirrored_pos[key] #value of right version of joint for indexed joint
                l = mirrored_pos['L'+key[1:]] # value of left version of joint for indexed joint

                if key == 'RWristYaw':

                    mirrored_pos[key] = -l

                    
                elif key == 'RElbowRoll':
                    mirrored_pos[key] = -l
                
                elif key == 'RShoulderRoll':
                    mirrored_pos[key] = -l
                
                elif key == 'RElbowYaw':
                    mirrored_pos[key] = -l
                else:
                    mirrored_pos[key] = l
                
        return mirrored_pos


    def Position_measure(self, mirror = False):

        """method that finds position of all of Nao's joints and returns a dictionary with keys as joint names and values as positions in 
        radians, note that joint sensors have accuracy to 0.0017 radians 
        
        Args: 

            mirror = Boolean value, if set to False will simply return the positions of all joints as the sensors read them 
            if True will mirror all joint positions on the left side of Nao to the right as to make him symetric 
        


            returns:
                joint_positions = dictionary of Naos joints with values being angle of joints in current position (radians)
                symetric_joint_positions = dictionary of Naos joints with values being angle of joints (radians) with left sight mirrored 
                to right


        """



        joint_list = ['LWristYaw', 'RWristYaw', 'HeadYaw', 'RHipPitch', 'RElbowYaw', 'RShoulderPitch', 'LShoulderRoll', 'LKneePitch', 'RAnkleRoll', 'LShoulderPitch', 'LHipPitch', 'LElbowYaw', 'LAnklePitch', 'RHipYawPitch', 'HeadPitch', 'LElbowRoll', 'RShoulderRoll', 'LHipYawPitch', 'LAnkleRoll', 'RAnklePitch', 'LHipRoll', 'RHipRoll', 'RElbowRoll', 'RKneePitch']

        joint_positions = {}

        for joint in joint_list:
            angle = self.move_proxy.getAngles(joint, True)[0]
            joint_positions[joint] = angle

        if mirror == False:
            return joint_positions

        if mirror == True:

            symetric_joint_positions = mirrored(joint_positions)
            return symetric_joint_positions










