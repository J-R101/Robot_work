# a collection of test functions and practice either later implemeted or scrapped, please ignore
  
  
  
  
    def TBLOtoTFLI(self, speed_frac):

        
        TFLI = {
            'LShoulderPitch': 1.463394045829773, 
            'LHipPitch': -0.7362780570983887, 
            'LElbowYaw': -1.0278220176696777, 
            'LAnklePitch': 0.760822057723999, 
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
            'RAnklePitch': 0.760822057723999, 
            'LKneePitch': 1.3989660739898682, 
            'LHipRoll': -0.0014920234680175781, 
            'RAnkleRoll': -0.019900083541870117, 
            'LElbowRoll': -1.480268120765686, 
            'RElbowRoll': 1.480268120765686, 
            'RHipRoll': -0.0014920234680175781}



        normalised_max_speed_dict = {
            'LWristYaw': 0.016483945069956023, 
            'RWristYaw': 0.022955564823096276,
            'HeadYaw': 0.0053441179425677155, 
            'RHipPitch': 0.4324873648954178,
            'RElbowYaw': 0.007959950732056895, 
            'RShoulderPitch': 0.20721183278729813, 
            'LShoulderPitch': 0.2041607069023573, 
            'LKneePitch': 1.0, 
            'RAnkleRoll': 0.0015693044751984562, 
            'LShoulderRoll': 0.26124562166252424,
            'LHipPitch': 0.43254370765789374, 
            'LElbowYaw': 0.003201495468528727, 
            'LAnklePitch': 0.59011328576745,
            'RHipYawPitch': 0.029746447968779864,
            'HeadPitch': 0.005538721677171022,
            'LElbowRoll': 0.6920699876263523, 
            'RShoulderRoll': 0.2639644791846046, 
            'LHipYawPitch': 0.029746447968779864,
            'LAnkleRoll': 0.0031386089503969124, 
            'RAnklePitch': 0.5900569480069948, 
            'LHipRoll': 0.0015328090222868644,
            'RHipRoll': 0.0015328090222868644,
            'RElbowRoll': 0.6857864544843684, 
            'RKneePitch': 0.9999436572375239}
        for key in normalised_max_speed_dict:
            self.move_proxy.setAngles(key, TFLI[key], normalised_max_speed_dict[key]*speed_frac, True)


    def pos_move(self, speed_frac, end_pos):
        #start = time.time()
        current_pos = self.current_pos_array()
        diff = np.abs(np.array(end_pos) - current_pos)+0.00001
        times = np.abs(diff/np.array(PA.max_speeds))
        quickest_time = np.max(times)

        #speeds = diff/quickest_time
                
       # frac_of_max = speeds/np.array(PA.max_speeds)

        
        self.move_proxy.angleInterpolation(PA.joints, end_pos, quickest_time, True )
        

        
        

        #print(max_speed_frac)


        #end = time.time()

        
#Nao = Robot(Initailisation = True)









    def quick_move(self, speed_frac, end_pos):
        current_pos = self.current_pos_array()


        dist = np.abs(np.array(end_pos) - current_pos)

        longest_time = np.max(dist/PA.max_speeds)

        speed_array = dist/longest_time

        frac_of_max = speed_array/PA.max_speeds

        #print(end_pos)
        #print(dist)

        # print(frac_of_max)

        for counter, value in enumerate(frac_of_max):
            if frac_of_max[counter] == 0:
                frac_of_max[counter] = 1


        for counter, value in enumerate(PA.joints):
            
             
            self.move_proxy.setAngles(value,end_pos[counter], speed_frac*np.abs(frac_of_max[counter]), True)



    def none_block_position_change(self, speed_frac, pos_frac, end_pos):

        current_pos = self.Position_measure()
        dist = LP.Ang_distance(current_pos, end_pos)

        target_pos= {}

        for key in end_pos:
            target_pos[key] = (dist[key]*pos_frac) + current_pos[key]


        # print(end_pos)
        # print(target_pos)


        dist = LP.Ang_distance(current_pos, target_pos)
        fastest_time = LP.quickest_time(current_pos, target_pos)[1]

        # print(dist)
        print(fastest_time)


       # fracmax_dict = 
        
        #print(fracmax_dict)
             
            # if frac_of_max == 0:
            #     frac_of_max=0.01
            # self.move_proxy.setAngles(key, target_pos[key], np.abs(frac_of_max*speed_frac))