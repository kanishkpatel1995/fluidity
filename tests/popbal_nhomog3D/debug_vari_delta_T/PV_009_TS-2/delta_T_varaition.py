import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# Reading csv files using python's "pandas" library..
time_o2 = pd.read_csv('PV009TS-2.csv')
time_o3 = pd.read_csv('../PV_min_TS-3/PV_min_TS-3.csv')
time_o4 = pd.read_csv('../PV_min_TS-4/PV_min_TS-4.csv')
time_o5 = pd.read_csv('../PV_min_TS-5/PV_min_TS-5.csv')
# Setting all pandas tables into an array to make loop construction easier
#Extracting values of moments from csv files and forming an array 
time_moment0_array = [time_o2['Moment_0'],time_o3['Moment_0'],time_o4['Moment_0'],time_o5['Moment_0']]
time_moment1_array = [time_o2['Moment_1'],time_o3['Moment_1'],time_o4['Moment_1'],time_o5['Moment_1']]
time_moment2_array = [time_o2['Moment_2'],time_o3['Moment_2'],time_o4['Moment_2'],time_o5['Moment_2']]
time_moment3_array = [time_o2['Moment_3'],time_o3['Moment_3'],time_o4['Moment_3'],time_o5['Moment_3']]
time_moment_array = [time_moment0_array, time_moment1_array, time_moment2_array, time_moment3_array]
# Index to quantify cahnge in Moments, So will remain same for all the graphs making quantification easier. 
x = list(range(len(time_o2['Moment_0'])))
# Array construction to old zeroth numerical moments when time for differnt timesteps.
#Moment_0_arr = []
#for i in range(4):
 #   Moment_0_arr.append(time_o[i]['Moment_0'])
#Loop for plotting values of Moment_0 obtained at different delta_t in same graph
for j in range(4):
	plt.subplot(2,2,j+1) #for debugging 
# colours for different plots in same graphs 
	colour = ['r','g','b','y']
	name_legend = ['T-2','T-3','T-4','T-5']
# T-2 refers to the case when the timestep was the order of 10^-2, similarly T-3 for 10^-3 and so on......
        plt.title('MOMENT ' + str(j))
	for k in range(4):
	    plt.plot(x,time_moment_array[j][k],colour[k], label = name_legend[k])
            plt.xlabel('Index')
            plt.ylabel('Respective Moment value')
	plt.legend()
plt.show()
# executed at last so that all the plots can be shown in one plot 

def singular_graph() :
# Shows the variation of graphs along the line on which the plots of moment are obtained with respect to the Inde number of point data
	for f in range(4):
		plt.subplot(2,2,f+1)
                plt.title('For TimeStep ' + str(-(f+2)))
		plt.plot(x,time_moment_array[0][f],colour[f])
		plt.xlabel('Index')
		plt.ylabel('Moment 0')
	plt.show()

