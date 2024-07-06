#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data1=pd.read_csv(r"C:\Users\Deba123\OneDrive\Documents\WorldCupMatches.csv")
data2=pd.read_csv(r"C:\Users\Deba123\OneDrive\Documents\WorldCupPlayers.csv")
data3=pd.read_csv(r"C:\Users\Deba123\OneDrive\Documents\WorldCups.csv")


# In[6]:


data1.head()


# In[7]:


data2.head()


# In[8]:


data3.head()


# In[9]:


import plotly as py
from plotly.offline import iplot
py.offline.init_notebook_mode(connected=True)


# In[10]:


# COUNTRY WISE ANALYSIS


# In[11]:


data_countries = pd.DataFrame(data3['Winner'].value_counts())
data_countries


# In[12]:


# Insight 1 : Brazil has won the tournament most number of times


# In[13]:


data_winner=pd.DataFrame(data3['Winner'].value_counts())
data_runner_up=pd.DataFrame(data3['Runners-Up'].value_counts())
data_third=pd.DataFrame(data3['Third'].value_counts())


# In[14]:


data_winner.head()


# In[15]:


plt.figure(figsize=(10, 6))
data_countries.plot(kind='bar', color='blue')
plt.title('Countries who have won worldcups')
plt.xlabel('Countries')
plt.ylabel('Winner')
plt.xticks(rotation=90)
plt.show()


# In[16]:


data_runner_up.head()


# In[17]:


data_third.head()


# In[18]:


teams = pd.concat([data_winner, data_runner_up, data_third], axis = 1)
teams


# In[19]:


# Dealing with NaN values

teams.fillna(0,inplace=True)


# In[20]:


teams=teams.astype(int)


# In[21]:


plt.figure(figsize=(10, 6))
teams.plot(kind='bar', color='Purple')
plt.title('Country wise analysis')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[22]:


# NUMBER OF GOALS PER COUNTRY 


# In[23]:


data1.head()


# In[24]:


# Seperating data based on goals scored by teams
data_home=data1[['Home Team Name','Home Team Goals']].dropna()
data_away=data1[['Away Team Name','Away Team Goals']].dropna()


# In[25]:


data_home.head()


# In[26]:


data_away.head()


# In[27]:


# Setting up the columns in both the tables
data_home.columns= ['Countries','Goals']
data_away.columns= ['Countries','Goals']


# In[28]:


data_country_goals = pd.concat([data_home, data_away], ignore_index=True)


# In[29]:


data_country_goals


# In[30]:


# The above table do contain all the goals both home and away but con have different values for same countries, so...

data_final_country_goal=data_country_goals.groupby('Countries').sum()


# In[31]:


# Arranging by number of goals
final_data=data_final_country_goal.sort_values(by='Goals',ascending=False)


# In[32]:


final_data=final_data[:10]
final_data


# In[2]:


# Insight 3 : Brazil scored the most number of goals thrughout the history of worldcup followed by Argentina and Germany.
teams.plot(kind='bar', color='red')
plt.title('Countries with maximum number of goals')
plt.xlabel('Country')
plt.ylabel('No of Goals')
plt.xticks(rotation=90)
plt.show()


# In[34]:


# Comparing half time home goals scored and half time away goals scored

half_team_home=pd.DataFrame(data1[['Home Team Name','Half-time Home Goals']])
half_team_away=pd.DataFrame(data1[['Away Team Name','Half-time Away Goals']])


# In[35]:


half_team_home = half_team_home.groupby('Home Team Name').sum()
half_team_home = half_team_home.sort_values(by='Half-time Home Goals',ascending=False)
half_team_home


# In[36]:


half_team_away = half_team_away.groupby('Away Team Name').sum()
half_team_away = half_team_away.sort_values(by='Half-time Away Goals',ascending=False)
half_team_away


# In[37]:


# Concatinating both the tables on team name
total = pd.concat([half_team_home, half_team_away], axis = 1)
total


# In[38]:


# Creating total goals columns to order the table based on total number of goals scored by a team
total['total_goals'] = total['Half-time Home Goals'] + total['Half-time Away Goals']
total = total.sort_values(by= 'total_goals',ascending=False)
total=total[:10]
total


# In[39]:


# We don't require total_goals anymore, so...
total.pop('total_goals')
total


# In[41]:


plt.figure(figsize=(10, 6))
total.plot(kind='bar', color='skyblue')
plt.title('Country wise analysis')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# In[42]:


data1.head(10)


# In[43]:


# We didn't considered draw matches here because in many cells we had NaN values given which corresponded to 0 values and could
# had made our pie chart biased.

def winner(data1):
    if data1['Home Team Goals'] > data1['Away Team Goals']:
        return 'Home team won'
    elif data1['Home Team Goals'] < data1['Away Team Goals']:
        return 'Away Team won'
    


# In[44]:


data1['winner']=data1.apply(lambda x:winner(x),axis=1)


# In[45]:


data1['winner'].value_counts()


# In[46]:


labels=['Home team won','Away Team won']
sizes=[486,174]


# In[47]:


fig, ax = plt.subplots(figsize= (4, 4), dpi = 100)
explode = (0.1, 0, 0)
ax.pie(sizes, labels = labels, autopct = '%1.1f%%', shadow = True,
      startangle = 90)

plt.show()


# In[48]:


data2.head()


# In[49]:


# Team Initials and Number Of Players Played Analysis
data2['Team Initials'].unique()


# In[50]:


data_nat = pd.DataFrame(data2[['Team Initials','Player Name']])
data_nat.head()


# In[51]:


d2 = pd.DataFrame(data_nat['Team Initials'].value_counts())
d2


# In[ ]:





# In[54]:


# BUILDING BEE SWARM PLOT FOR NUMBER OF PLAYERS AND FINDING MINIMUM AND MAXIMUM RANGE
plt.rcParams['figure.facecolor'] = "#ffffe6"
plt.rcParams['axes.facecolor'] = "#ffffe6"
p2 = sns.swarmplot( x = 'Team Initials', data = d2 , palette='inferno')
plt.title('Finding the range of players played from Minimum To Maximum')
plt.xlabel('Number Of Players')
plt.ylabel('Range of Players')
plt.show()


# In[58]:


plt.figure(figsize=(10, 6))
d2.plot(kind='bar', color='skyblue')
plt.title('Country code vs number of players played')
plt.xlabel('Country code')
plt.ylabel('No of players')
plt.xticks(rotation=90)
plt.show()


# In[ ]:





# In[ ]:




