#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[19]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[21]:


total_players = len(purchase_data["SN"].value_counts())
total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[28]:


total_unique_items = len((purchase_data["Item ID"]).unique())
average_price = (purchase_data["Purchase ID"]).count()
purchases = (purchase_data["Purchase ID"]).count()
total_revenue = (purchase_data["Price"]).sum()

purchasing_analysis_df = pd.DataFrame({"Total Unique Items":[total_unique_items], "Average Price":[average_price], "Total Purchase":[purchases], "Total Revenue":[total_revenue]})
purchasing_analysis_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[36]:


gender_dem = purchase_data.groupby("Gender")
gender_count = gender_dem.nunique()["SN"]
player_percents = gender_count/total_players*100
gender_dems = pd.DataFrame({"Percent of Players": player_percents})
gender_dems


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[39]:


purchase_numbers = gender_dem["Purchase ID"].count()
average_price = gender_dem["Price"].mean()
average_total = gender_dem["Price"].sum()
player_purchase_average = average_total/gender_count

purchasing_analysis_gender = pd.DataFrame({"Purchase Count":purchase_numbers, "Average Purchase Price": average_price, "Average Purchase Value": average_total, "Average Purchase Per Person": player_purchase_average})

purchasing_analysis_gender


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[46]:


bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 100]
bin_names = ["<= 10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Group"] = pd.cut(purchase_data["Age"],bins,labels=bin_names)

age_group = purchase_data.groupby("Age Group")

players_by_age = age_group["SN"].nunique()

age_percent = (players_by_age/total_players) * 100

players_age_stats = pd.DataFrame({"Percentage of Players": age_percent, "Total": players_by_age})
players_age_stats


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[50]:


purchase_analysis_age = age_group["Purchase ID"].count()
purchase_analysis_age

purchase_amount_age_average = age_group["Price"].mean()

purchase_per_age = purchase_amount_age_average/players_by_age

purchase_analysis_age = pd.DataFrame({"Purchase Count": purchase_analysis_age ,
                                 "Average Price": purchase_amount_age_average,
                                 "Total Value": purchase_amount_age_average,
                                 "Average Purchase per Person": purchase_per_age})
purchase_analysis_age


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[66]:


stats_on_spenders = purchase_data.groupby("SN")
spender_counts = stats_on_spenders["Purchase ID"].count()
average_spender_purchase = stats_on_spenders["Price"].mean()
spender_total = stats_on_spenders["Price"].sum()

Top_Spenders = pd.DataFrame({"Purchase Count": spender_counts, "Average Purchase Price": average_spender_purchase, "Total Purchase Value": spender_total})
descending_format = Top_Spenders.sort_values(["Total Purchase Value"], ascending = False)
descending_format.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[77]:


pop_items = purchase_data[["Item ID", "Item Name", "Price"]]

items_info = pop_items.groupby(["Item ID", "Item Name"])

number_purchase = items_info["Price"].count()

purchase_price = (items_info["Price"].sum())

item_price = purchase_price/number_purchase

most_pop_items = pd.DataFrame({"Purchase Count": number_purchase, "Item Price": item_price, "Total Purchase Value": purchase_price})
ordered = most_pop_items.sort_values(["Purchase Count"], ascending=True)
ordered


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[76]:


ordered = most_pop_items.sort_values(["Total Purchase Value"], ascending= False).head()
ordered.head()


# In[ ]:




