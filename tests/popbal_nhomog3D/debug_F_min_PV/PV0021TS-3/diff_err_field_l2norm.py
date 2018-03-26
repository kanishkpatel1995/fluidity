#code to quantify errors
# Analyse and know what are the reasons the error is propogaing  
import fluidity_tools
import matplotlib.pyplot as plt
stat1 = fluidity_tools.stat_parser("popbal_nhomog3D.stat")
T_2_m0 = stat1["fluid"]["diff_m0"]["l2norm"]
T_2_m1 = stat1["fluid"]["diff_m1"]["l2norm"]
T_2_m2 = stat1["fluid"]["diff_m2"]["l2norm"]
T_2_m3 = stat1["fluid"]["diff_m3"]["l2norm"]
#T_3 = stat2["fluid"]["m0_anal"]["l2norm"]
t = stat1["ElapsedTime"]["value"]
plt.subplot(2,2,1)
plt.plot(t,T_2_m0,"-r")
plt.xlabel("Time")
plt.ylabel("Moment 0")
plt.subplot(2,2,2)
plt.plot(t,T_2_m1,"-r")
plt.xlabel("Time")
plt.ylabel("Moment 1")
plt.subplot(2,2,3)
plt.plot(t,T_2_m2,"-r")
plt.xlabel("Time")
plt.ylabel("Moment 2")
plt.subplot(2,2,4)
plt.plot(t,T_2_m3,"-r")
plt.xlabel("Time")
plt.ylabel("Moment 3")
plt.show()
