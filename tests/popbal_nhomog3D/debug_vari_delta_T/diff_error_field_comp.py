#code to quantify errors
# Analyse and know what are the reasons the error is propogaing  
########################################################################################################################################################################################################

CANNOT WORK !!!!!!!!!!!!! AS THE ELAPSED TIME VALUES ARE DIFFERENT FOR ALL CAESES................ 
BUT THERE IS WAY USING RANGE AND GETTING SPECIFIC VALUES AT SPECIFIC INTERVALS........ LITTLE BIT OF LOGIC NOTHING ELSE ........
TRY IT OUT LATER 

########################################################################################################################################################################################################
import fluidity_tools
import os 
import matplotlib.pyplot as plt
stat1 = fluidity_tools.stat_parser("PV_05_TS-2/popbal_nhomog3D.stat")
stat2 = fluidity_tools.stat_parser("PV_min_TS-3/popbal_nhomog3D.stat")
stat3 = fluidity_tools.stat_parser("PV_min_TS-4/popbal_nhomog3D.stat")
stat4 = fluidity_tools.stat_parser("PV_min_TS-5/popbal_nhomog3D.stat")
#first graph
T_2_m0 = stat1["fluid"]["diff_m0"]["l2norm"]
T_3_m0 = stat2["fluid"]["diff_m0"]["l2norm"]
T_4_m0 = stat3["fluid"]["diff_m0"]["l2norm"]
T_5_m0 = stat4["fluid"]["diff_m0"]["l2norm"]
# Second graph 
T_2_m1 = stat1["fluid"]["diff_m1"]["l2norm"]
T_3_m1 = stat2["fluid"]["diff_m1"]["l2norm"]
T_4_m1 = stat3["fluid"]["diff_m1"]["l2norm"]
T_5_m1 = stat4["fluid"]["diff_m1"]["l2norm"]
# Third Graph
T_2_m2 = stat1["fluid"]["diff_m2"]["l2norm"]
T_3_m2 = stat2["fluid"]["diff_m2"]["l2norm"]
T_4_m2 = stat3["fluid"]["diff_m2"]["l2norm"]
T_5_m2 = stat4["fluid"]["diff_m2"]["l2norm"]
#fourth graph
T_2_m3 = stat1["fluid"]["diff_m3"]["l2norm"]
T_3_m3 = stat2["fluid"]["diff_m3"]["l2norm"]
T_4_m3 = stat3["fluid"]["diff_m3"]["l2norm"]
T_5_m3 = stat4["fluid"]["diff_m3"]["l2norm"]
#T_3 = stat2["fluid"]["m0_anal"]["l2norm"]
# plotting
# for now T-5 is being ommitted as the simulation is going on wil be addded later
t = stat1["ElapsedTime"]["value"]
plt.title("Difference Fileds for Moment zero at varied timesteps") 
plt.subplot(2,2,1)
plt.plot(t,T_2_m0,"-r",t,T_3_m0, "-b",t,T_4_m0, "-g")
plt.xlabel("Time")
plt.ylabel("Moment 0")
plt.legend()
plt.subplot(2,2,2)
plt.plot(t,T_2_m1,"-r",t,T_3_m1, "-b",t,T_4_m1, "-g")
plt.xlabel("Time")
plt.ylabel("Moment 1")
plt.legend()
plt.subplot(2,2,3)
plt.plot(t,T_2_m2,"-r",t,T_3_m2, "-b",t,T_4_m2, "-g")
plt.xlabel("Time")
plt.ylabel("Moment 2")
plt.legend()
plt.subplot(2,2,4)
plt.plot(t,T_2_m3,"-r",t,T_3_m3, "-b",t,T_4_m3, "-g")
plt.xlabel("Time")
plt.ylabel("Moment 3")
plt.legend()
plt.show()
