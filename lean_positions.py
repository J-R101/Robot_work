import numpy as np


# list of extreme posistions for Nao with positions only containing information for joints involved in only torso motion or only leg motion

leaning_forward = {
    'LShoulderPitch': 1.463394045829773, 
    'LHipPitch': -0.7362780570983887, 
    'LElbowYaw': -1.0278220176696777, 
    'LWristYaw': -0.5890979766845703, 
    'RWristYaw': 0.5890979766845703, 
    'HeadYaw': -0.0061779022216796875, 
    'RHipPitch': -0.7362780570983887, 
    'HeadPitch': 0.49697399139404297, 
    'RElbowYaw': 1.0278220176696777, 
    'RShoulderPitch': 1.463394045829773, 
    'LShoulderRoll': 0.5414600372314453, 
    'RHipYawPitch': -0.038308143615722656, 
    'RShoulderRoll': -0.5414600372314453, 
    'LHipYawPitch': -0.038308143615722656, 
    'LHipRoll': -0.0014920234680175781,  
    'LElbowRoll': -1.480268120765686, 
    'RElbowRoll': 1.480268120765686, 
    'RHipRoll': -0.0014920234680175781}

leaning_back = {
    'LShoulderPitch': 1.1197781562805176, 
    'LHipPitch': -0.09353208541870117, 
    'LElbowYaw': -1.0339579582214355, 
    'LWristYaw': -0.714885950088501, 
    'RWristYaw': 0.714885950088501, 
    'HeadYaw': -0.0061779022216796875, 
    'RHipPitch': -0.09353208541870117, 
    'HeadPitch': 0.4954400062561035, 
    'RElbowYaw': 1.0339579582214355, 
    'RShoulderPitch': 1.1197781562805176, 
    'LShoulderRoll': 0.09506607055664062, 
    'RHipYawPitch': -0.009161949157714844, 
    'RShoulderRoll': -0.09506607055664062,
    'LHipYawPitch': -0.009161949157714844, 
    'LHipRoll': -0.0030260086059570312, 
    'LElbowRoll': -0.30675792694091797, 
    'RElbowRoll': 0.30675792694091797, 
    'RHipRoll': -0.0030260086059570312}



#a dictionary of total angle travelled by all joints in torso from leaning forward to leaning back
lean_full_dist = {
    'LShoulderPitch': 0.34361588954925537, 
    'LShoulderRoll': 0.4463939666748047, 
    'LHipPitch': -0.6427459716796875, 
    'LElbowYaw': 0.0061359405517578125, 
    'LHipYawPitch': -0.029146194458007812, 
    'LWristYaw': 0.12578797340393066, 
    'RWristYaw': -0.12578797340393066, 
    'HeadYaw': 0.0, 
    'RShoulderRoll': -0.4463939666748047, 
    'LHipRoll': 0.0015339851379394531, 
    'RHipPitch': -0.6427459716796875, 
    'RShoulderPitch': 0.34361588954925537, 
    'HeadPitch': 0.0015339851379394531, 
    'RHipYawPitch': -0.029146194458007812, 
    'RElbowYaw': -0.0061359405517578125, 
    'RElbowRoll': 1.173510193824768, 
    'RHipRoll': 0.0015339851379394531, 
    'LElbowRoll': -1.173510193824768}

#note in the transition between full lean back and lean forward the max speed is 0.15s which as its limited by Elbow roll




leg_back = {
    'LAnklePitch': 0.760822057723999, 
    'RKneePitch': 1.3989660739898682, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch': 0.760822057723999, 
    'LKneePitch': 1.3989660739898682, 
    'RAnkleRoll': -0.019900083541870117}

leg_forward = {

    'LAnklePitch': -0.11816000938415527, 
    'RKneePitch': -0.09054803848266602, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch': -0.11816000938415527, 
    'LKneePitch': -0.09054803848266602, 
    'RAnkleRoll': -0.019900083541870117,     
     }

#a dictionary of total angle travelled by all joints in legs from tucked to outstretched
leg_kick_dist = {
    'LAnklePitch': 0.8789820671081543, 
    'LAnkleRoll': 0.0,
    'RAnklePitch': 0.8789820671081543, 
    'LKneePitch': 1.4895141124725342, 
    'RAnkleRoll': 0.0, 
    'RKneePitch': 1.4895141124725342}

#note in the transition between leg_forward and leg back is limited by knee pitch to max time of  0.2327



#dictionary containg calculated max speeds of all joints
max_speed_dict =  {
    'LShoulderPitch': 8.523, 
    'LHipPitch':  6.4,
    'LElbowYaw': 8.235, 
    'LAnklePitch': 6.4, 
    'LWristYaw': 24.391, 
    'RWristYaw': 24.39, 
    'RHipPitch': 6.4, 
    'HeadPitch': 7.14, 
    'RElbowYaw': 8.235, 
    'RShoulderPitch': 8.523, 
    'RKneePitch': 6.4, 
    'LShoulderRoll': 7.14, 
    'RHipYawPitch': 4.21, 
    'RShoulderRoll': 7.14,
    'LHipYawPitch': 4.21, 
    'RAnklePitch': 6.4, 
    'LKneePitch': 6.4, 
    'LElbowRoll': 7.4, 
    'RElbowRoll': 7.4, 
    'LAnkleRoll':4.2,
    'RAnkleRoll':4.2,
    'HeadYaw': 7.4,
    'LHipRoll': 4.3,
    'RHipRoll': 4.3


   }

#function to calculate angular distance of all joints between initail and final position, not only a quikc test hence no doc string 
def Ang_distance(pos_dict1, pos_dict2):
    diff_dict = {}
    for key in pos_dict1:
        try:
            diff_dict[key] = pos_dict2[key] - pos_dict1[key]
        except KeyError:
            pass
    
    return diff_dict

#function to calculate longest time if all joints travelled at max speed to move between two positions, note only a quikc test hence no doc string 
def quickest_time(pos_dict1,pos_dict2):

    displacement_dict =Ang_distance(pos_dict1, pos_dict2)

    distance_dict = {}

    for key in displacement_dict:
        try:
            distance_dict[key] = np.sqrt((displacement_dict[key])**2)
        except KeyError:
            pass

    time = {}
    for key in pos_dict1:
        try:
            time[key] = distance_dict[key]/max_speed_dict[key]
        except KeyError:
            pass
    
    slowest_joint = max(time, key = time.get)

    #return time
    return (slowest_joint, time[slowest_joint])

    

#shortest time to enact full torso motion and full leg motion
max_speed_pos_change = {"full_kick":0.23273658007383347, "full_lean":0.15858245862496864}









