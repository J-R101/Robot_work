from scipy.signal import find_peaks
import numpy as np


#note code from prev year and matthew, but in this file as needed for other files




########### definitions
# what - max,min, or zero point in the swing
# all_data - dictionary of all values

def find_last_peak_index(data):
    peaks = find_peaks(data, prominence=1)[0]
        
    if len(peaks) < 1:
        return 0
    else:
        return peaks[-1]

def interpolate_to_find_zero_time(angle_data,time_data):
    min_time = []
    #### Got rid of ev = encoder_values, tv = times to make it easier to read
    for i in range(len(angle_data)-1):
        if np.sign(angle_data[i+1]) != np.sign(angle_data[i]):
            time_diff = abs(time_data[i] - time_data[i+1])
            interpolate = time_diff * np.abs(angle_data[i]) / abs(angle_data[i] - angle_data[i+1])
            min_time.append(time_data[i] + interpolate)## Error was - instead of +

    if len(min_time) < 1:
        return 0
    else:
        return min_time[-1]
    
def last_key_point_time(all_data):
    
    times = all_data[:,-1]#
    encoder_values = all_data[:,0]#
    
    #last_times = times[-10:]

    max_ang_time = times[find_last_peak_index(encoder_values)]
    min_ang_time = times[find_last_peak_index(-encoder_values)]
    zero_ang_time = interpolate_to_find_zero_time(encoder_values,times)
        
    return [max_ang_time, min_ang_time, zero_ang_time]
    
def last_key_point_angle(all_data):
    
    #times = all_data[:,1]#
    encoder_values = all_data[:,0]#
    
    #last_times = times[-10:]

    max_ang = encoder_values[find_last_peak_index(encoder_values)]
    min_ang = encoder_values[find_last_peak_index(-encoder_values)]

    return [max_ang,min_ang,0]  

def next_points(last_key_points):
    # last_key_points - a list ordered max,min,zero
    event_that_happened_last = np.argmax(last_key_points)

    half_period = abs(last_key_points[0] - last_key_points[1])
    
    if event_that_happened_last == 0:# Max
        
        next_max = last_key_points[0] + 2*half_period
        next_min = last_key_points[0] + half_period
        next_zero = last_key_points[0] + half_period/2
        
    elif event_that_happened_last == 1:# Min
        next_max = last_key_points[1] + half_period
        next_min = last_key_points[1] + 2*half_period
        next_zero = last_key_points[1] + half_period/2
    	
    elif event_that_happened_last == 2:# Zero
        
        if last_key_points[1] > last_key_points[0]:
            next_max = last_key_points[2] + half_period/2
            next_min = last_key_points[2] + 1.5*half_period
            next_zero = last_key_points[2] + half_period
        else:
            next_max = last_key_points[2] + 1.5*half_period
            next_min = last_key_points[2] + half_period/2
            next_zero = last_key_points[2] + half_period
            
        
    return next_max, next_min, next_zero
