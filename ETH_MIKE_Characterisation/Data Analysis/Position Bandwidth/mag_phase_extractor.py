#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def mag_phase_extractor(mike_version,freq):
    
    from nptdms import TdmsFile # https://nptdms.readthedocs.io/en/stable/
    import numpy as np
    from scipy import signal as sig
    import control

    file = TdmsFile.read("tdms/mike"+str(mike_version)+"_PB_"+str(freq)+".tdms")
    
    p_set = file["Position_Bandwidth"]["Position Setpoint [deg]"][:]
    p_meas = file["Position_Bandwidth"]["Position [deg]"][:]
    time = file["Position_Bandwidth"]["Time (s) "][:]
    time = time - time[0]
    
    # delete data for which the setpoint is zero
    p_meas = p_meas[np.nonzero(p_set)]
    time = time[np.nonzero(p_set)]
    p_set = p_set[np.nonzero(p_set)]
    
    # filtering
    fs = 1/np.mean(np.diff(time))
    if freq >= 1:
        fc = 60
    else:
        fc = 10
    b,a = sig.butter(1,fc/(fs/2),'low')
    p_meas = sig.filtfilt(b,a,p_meas)
    
    distance = (1/(3*freq))/0.001 # minimal x-distance in measurements between two conscuitve peaks
    m_loc_max, m_peaks_max = sig.find_peaks(p_meas, distance = distance)
    s_loc_max, s_peaks_max = sig.find_peaks(p_set, height=4) # peak must be at a minimum height of 4
    m_loc_min, m_peaks_min = sig.find_peaks(-p_meas, distance = distance)
    s_loc_min, s_peaks_min = sig.find_peaks(-p_set, height=4)

    m_peaks_max = p_meas[m_loc_max]
    s_peaks_max = p_set[s_loc_max]
    m_peaks_min = p_meas[m_loc_min]
    s_peaks_min = p_set[s_loc_min]

    # the first peak always is an overshoot due to the step input and therefore leads to false results --> it is deleted and neglected
    if freq > 0.2:
        m_peaks_max = np.delete(m_peaks_max, 0)
        s_peaks_max = np.delete(s_peaks_max, 0)
        m_loc_max = np.delete(m_loc_max, 0)
        s_loc_max = np.delete(s_loc_max, 0)

    # as only the measurements are taken into account where the setpoint is not zero, the last setpoint peaked is not reached in the measured signal due to phase shift --> delete the last setpoints peak
    if freq >= 4:
        s_peaks_min = s_peaks_min[:-1]
        s_loc_min = s_loc_min[:-1]

    # for large frequencies, the system need some time to get into transient state --> only use the last twenty peak measurements
    if freq >= 8:
        m_peaks_max = m_peaks_max[-20:]
        s_peaks_max = s_peaks_max[-20:]
        m_loc_max = m_loc_max[-20:]
        s_loc_max = s_loc_max[-20:]

        m_peaks_min = m_peaks_min[-20:]
        s_peaks_min = s_peaks_min[-20:]
        m_loc_min = m_loc_min[-20:]
        s_loc_min = s_loc_min[-20:]

    # for small frequencies delete all negative peaks in the max peak measurements and all positive peaks in the negative measurements
    if freq < 1:
        indices = np.nonzero(m_peaks_max < 0)
        m_peaks_max = np.delete(m_peaks_max,indices)
        m_loc_max = np.delete(m_loc_max,indices)
        indices = np.nonzero(m_peaks_min > 0)
        m_peaks_min = np.delete(m_peaks_min,indices)
        m_loc_min = np.delete(m_loc_min,indices)

    # delete peak measurements when the time of their appearance is earlier than the corresponding measurement in the setpoint signals --> eliminate measurement errors
    for i in range(0,np.size(s_loc_max)):
        if np.size(m_loc_max) == np.size(s_loc_max):
            break
        if m_loc_max[i] < s_loc_max[i]:
            m_loc_max = np.delete(m_loc_max,i)
            m_peaks_max = np.delete(m_peaks_max,i)

    for i in range(0,np.size(s_loc_min)):
        if np.size(m_loc_min) == np.size(s_loc_min):
            break
        if m_loc_min[i] < s_loc_min[i]:
            m_loc_min = np.delete(m_loc_min,i)
            m_peaks_min = np.delete(m_peaks_min,i)

    mag_max = np.mean(m_peaks_max/s_peaks_max)
    mag_min = np.mean(m_peaks_min/s_peaks_min)
    mag = 0.5*(mag_max+mag_min)
    mag_db = control.mag2db(mag)

    phase = np.mean(freq*(time[s_loc_max]-time[m_loc_max])*360)

    return [mag_db, phase]

