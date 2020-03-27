import pandas as pd 
import matplotlib.pyplot as plt
from random import randint
import bs4
import matplotlib.patches as mpatches

# data = pd.read_csv('goiana.csv')

# plt.bar(x=data['Committed dose LB'],height=data['Number of people'],width=data['Committed dose UB']-data['Committed dose LB'],align='edge',color='m',edgecolor='black')
# plt.xlabel(r'Committed dose (70 years) / Sv')
# plt.ylabel('Number of people')
# plt.title('DOSES INCURRED IN THE ACCIDENT IN GOIANIA')
# plt.show()

data = pd.read_csv('tableData.csv')
data.sort_values('Fatalities')
ax = plt.bar(x=data['Incident'][:17],height=data['Fatalities'][:17],color='m',edgecolor='black')
plt.xticks(rotation='vertical',fontsize=9)
plt.ylabel('Fatalities')
plt.xlabel('Incident')
ax[1].set_color('r')
ax[2].set_color('r')
ax[3].set_color('r')
ax[0].set_color('r')
ax[14].set_color('g')
red_patch = mpatches.Patch(color='r', label='disputed')
green_patch = mpatches.Patch(color='g', label='Goiana Accident')
plt.legend(handles=[red_patch,green_patch])
plt.show()
