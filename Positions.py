

#Different positions for Nao to move to, with neutral_pos being the initialisation position to ensure Nao is straped in the same each time
#TFLI - Torso forward Legs in
#TFLO- Torso forward legs out
#TBLI- Torso back legs in
#TBLO -Torso back legs out

#prev_lean_back - maximum amount Nao could lean back before hitting the seat before holes were drilled

#note all angles are radians



neutral_pos = {
    'LShoulderPitch': 1.402034044265747, 
    'LHipPitch': -0.6350340843200684, 
    'LElbowYaw': -0.9971418380737305, 
    'LAnklePitch': 0.10120201110839844, 
    'LWristYaw': -0.7532360553741455, 
    'RWristYaw': 0.7532360553741455, 
    'HeadYaw': 0.01683211326599121, 
    'RHipPitch': -0.6350340843200684, 
    'HeadPitch': 0.514872133731842, 
    'RElbowYaw': 0.9971418380737305, 
    'RShoulderPitch': 1.402034044265747, 
    'RKneePitch': 1.1565940380096436, 
    'LShoulderRoll': 0.5276541709899902, 
    'RHipYawPitch': -0.0367741584777832, 
    'RShoulderRoll': -0.5276541709899902, 
    'LHipYawPitch': -0.0367741584777832, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch': 0.1120201110839844, 
    'LKneePitch': 1.1565940380096436, 
    'LHipRoll': -0.0014920234680175781, 
    'RAnkleRoll': -0.019900083541870117, 
    'LElbowRoll': -1.463394045829773, 
    'RElbowRoll': 1.463394045829773, 
    'RHipRoll': -0.0014920234680175781}

#-0.321368873119 to gravity


TFLI = {
    'LShoulderPitch': 1.463394045829773, 
    'LHipPitch': -0.7362780570983887, 
    'LElbowYaw': -1.0278220176696777, 
    'LAnklePitch': 0.10120201110839844, #0.760822057723999, 
    'LWristYaw': -0.5890979766845703, 
    'RWristYaw': 0.5890979766845703, 
    'HeadYaw': -0.0061779022216796875, 
    'RHipPitch': -0.7362780570983887, 
    'HeadPitch': 0.49697399139404297, 
    'RElbowYaw': 1.0278220176696777, 
    'RShoulderPitch': 1.463394045829773, 
    'RKneePitch': 1.3989660739898682, 
    'LShoulderRoll': 0.5414600372314453, 
    'RHipYawPitch': -0.038308143615722656, 
    'RShoulderRoll': -0.5414600372314453, 
    'LHipYawPitch': -0.038308143615722656, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch':0.10120201110839844, #                         0.760822057723999, 
    'LKneePitch': 1.3989660739898682, 
    'LHipRoll': -0.0014920234680175781, 
    'RAnkleRoll': -0.019900083541870117, 
    'LElbowRoll': -1.480268120765686, 
    'RElbowRoll': 1.480268120765686, 
    'RHipRoll': -0.0014920234680175781}

  #  -0.239109218121 to gravity

TFLO = {
    'LShoulderPitch': 1.4495880603790283, 
    'LHipPitch': -0.7378120422363281, 
    'LElbowYaw': -1.0339579582214355, 
    'LAnklePitch':0.10120201110839844,                                        #        -0.11816000938415527, 
    'LWristYaw': -0.5538160800933838, 
    'RWristYaw': 0.5538160800933838, 
    'HeadYaw': -0.0061779022216796875, 
    'RHipPitch': -0.7378120422363281, 
    'HeadPitch': 0.49697399139404297, 
    'RElbowYaw': 1.0339579582214355, 
    'RShoulderPitch': 1.4495880603790283, 
    'RKneePitch': -0.09054803848266602, 
    'LShoulderRoll': 0.550663948059082, 
    'RHipYawPitch': -0.038308143615722656, 
    'RShoulderRoll': -0.550663948059082, 
    'LHipYawPitch': -0.038308143615722656, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch':0.10120201110839844,                             #-0.11816000938415527, 
    'LKneePitch': -0.09054803848266602, 
    'LHipRoll': -0.0030260086059570312, 
    'RAnkleRoll': -0.019900083541870117, 
    'LElbowRoll': -1.515550136566162, 
    'RElbowRoll': 1.515550136566162, 
    'RHipRoll': -0.0030260086059570312}
    

# -0.116774253547 to gravity



TBLI = {
    'LShoulderPitch': 1.1197781562805176, 
    'LHipPitch': -0.09353208541870117, 
    'LElbowYaw': -1.0339579582214355, 
    'LAnklePitch': 0.10120201110839844, #0.760822057723999, 
    'LWristYaw': -0.714885950088501, 
    'RWristYaw': 0.714885950088501, 
    'HeadYaw': -0.0061779022216796875, 
    'RHipPitch': -0.09353208541870117, 
    'HeadPitch': 0.4954400062561035, 
    'RElbowYaw': 1.0339579582214355, 
    'RShoulderPitch': 1.1197781562805176, 
    'RKneePitch': 1.4005000591278076, 
    'LShoulderRoll': 0.09506607055664062, 
    'RHipYawPitch': -0.009161949157714844, 
    'RShoulderRoll': -0.09506607055664062,
    'LHipYawPitch': -0.009161949157714844, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch': 0.10120201110839844, # 0.760822057723999, 
    'LKneePitch': 1.4005000591278076, 
    'LHipRoll': -0.0030260086059570312, 
    'RAnkleRoll': -0.019900083541870117, 
    'LElbowRoll': -0.30675792694091797, 
    'RElbowRoll': 0.30675792694091797, 
    'RHipRoll': -0.0030260086059570312}

   # -0.893543899059 to gravity



TBLO = {
    'LShoulderPitch': 1.104438066482544, 
    'LHipPitch': -0.09199810028076172, 
    'LElbowYaw': -1.0339579582214355, 
    'LAnklePitch': 0.10120201110839844, #-0.11816000938415527, 
    'LWristYaw': -0.7118179798126221, 
    'RWristYaw': 0.7118179798126221, 
    'HeadYaw': -0.0061779022216796875, 
    'RHipPitch': -0.09199810028076172, 
    'HeadPitch': 0.49697399139404297, 
    'RElbowYaw': 1.0339579582214355, 
    'RShoulderPitch': 1.104438066482544, 
    'RKneePitch': -0.09054803848266602, 
    'LShoulderRoll': 0.09353208541870117, 
    'RHipYawPitch': -0.009161949157714844, 
    'RShoulderRoll': -0.09353208541870117, 
    'LHipYawPitch': -0.009161949157714844, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch': 0.10120201110839844, # -0.11816000938415527, 
    'LKneePitch': -0.09054803848266602, 
    'LHipRoll': -0.0030260086059570312, 
    'RAnkleRoll': -0.019900083541870117, 
    'LElbowRoll': -0.309826135635376, 
    'RElbowRoll': 0.309826135635376, 
    'RHipRoll': -0.0030260086059570312}
    #-0.874177157879
    





prev_lean_back = {
    'LShoulderPitch': 1.3728880882263184, 
    'LHipPitch': -0.5015759468078613, 
    'LElbowYaw': -1.032423973083496, 
    'LAnklePitch': -0.11816000938415527, 
    'LWristYaw': -0.6627299785614014, 
    'RWristYaw': 0.6627299785614014, 
    'HeadYaw': 0.013764142990112305, 
    'RHipPitch': -0.5015759468078613, 
    'HeadPitch': 0.4893040657043457, 
    'RElbowYaw': 1.032423973083496, 
    'RShoulderPitch': 1.3728880882263184, 
    'RKneePitch': 0.7347440719604492, 
    'LShoulderRoll': 0.4080021381378174, 
    'RHipYawPitch': -0.033705949783325195, 
    'RShoulderRoll': -0.4080021381378174, 
    'LHipYawPitch': -0.033705949783325195, 
    'LAnkleRoll': -0.019900083541870117, 
    'RAnklePitch': -0.11816000938415527, 
    'LKneePitch': 0.7347440719604492, 
    'LHipRoll': -0.0014920234680175781, 
    'RAnkleRoll': -0.019900083541870117, 
    'LElbowRoll': -1.198012113571167, 
    'RElbowRoll': 1.198012113571167, 
    'RHipRoll': -0.0014920234680175781}



