import fluidity_tools
import matplotlib.pyplot as plt
stat1 = fluidity_tools.stat_parser("popbal_nhomog3D.stat")
T_2_ma0 = stat1["fluid"]["m0_anal"]["l2norm"]
T_2_m0 = stat1["fluid"]["Moment_0"]["l2norm"]
T_2_ma1 = stat1["fluid"]["m1_anal"]["l2norm"]
T_2_m1 = stat1["fluid"]["Moment_1"]["l2norm"]
T_2_ma2 = stat1["fluid"]["m2_anal"]["l2norm"]
T_2_m2 = stat1["fluid"]["Moment_2"]["l2norm"]
T_2_ma3 = stat1["fluid"]["m3_anal"]["l2norm"]
T_2_m3 = stat1["fluid"]["Moment_3"]["l2norm"]
#T_3 = stat2["fluid"]["m0_anal"]["l2norm"]
t = stat1["ElapsedTime"]["value"]
#################
plt.subplot(2,2,1)
plt.plot(t,T_2_m0,"-r", label = "Numerical" )
plt.plot(t, T_2_ma0, "-g", label = "Analytical")
plt.xlabel("Time")
plt.ylabel("Moment 0")
plt.legend()
################################
plt.subplot(2,2,2)
plt.plot(t,T_2_m1,"-r", label = "Numerical")
plt.plot(t, T_2_ma1, "-og", label = "Analytical")
plt.xlabel("Time")
plt.ylabel("Moment 1")
plt.legend()
####################
plt.subplot(2,2,3)
plt.plot(t,T_2_m2,"-r", label = "Numerical")
plt.plot(t, T_2_ma2, "-g", label = "Analytical")
plt.xlabel("Time")
plt.ylabel("Moment 2")
plt.legend()
####################
plt.subplot(2,2,4)
plt.plot(t,T_2_m3,"-r", label = "Numerical")
plt.plot(t, T_2_ma3, "-g", label = "Analytical")
plt.xlabel("Time")
plt.ylabel("Moment 3")
plt.legend()
plt.show()
