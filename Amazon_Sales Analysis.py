#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd


# In[69]:


data=pd.read_csv('global7.csv')
data


# # Data Cleaning

# In[70]:


data.info()


# In[71]:


data.drop(['Column1','Unnamed: 0','sales in rupees','into qua','last sale'],axis=1,inplace=True)


# In[72]:


data.drop(['Discount'],axis=1,inplace=True)


# In[73]:


data.dtypes


# In[74]:


data['Order Date'] = pd.to_datetime(data['Order Date'], format='%d-%m-%Y', errors='coerce')


# In[75]:


data['Ship Date']=pd.to_datetime(data['Ship Date'],format='%d-%m-%Y',errors='coerce')


# In[76]:


data.rename(columns={' Profit ': 'Profit'}, inplace=True)


# In[77]:


data['Profit']=pd.to_numeric(data['Profit'],errors='coerce')


# In[78]:


data.isnull().sum()


# In[79]:


ship_mode=data['Ship Mode'].mode()[0]
data['Ship Mode'].fillna(value=ship_mode,inplace=True)


# In[80]:


ship_mode=data['Ship Date'].mode()[0]
data['Ship Date'].fillna(value=ship_mode,inplace=True)


# In[81]:


ship_mode=data['Order Date'].mode()[0]
data['Order Date'].fillna(value=ship_mode,inplace=True)


# In[82]:


postal_code_mean=data['Postal Code'].mean()
data['Postal Code'].fillna(value=postal_code_mean,inplace=True)


# In[83]:


profit_mean=data['Profit'].mean()
data['Profit'].fillna(value=profit_mean,inplace=True)


# # Summary Statistics

# In[84]:


print("Summary statistics for numerical columns:")
data.describe()


# # Count of unique values in categorical columns

# In[85]:


print("Count of unique values in categorical columns:")
for column in data.select_dtypes(include=['object']).columns:
    print(f"{column}: {data[column].nunique()} unique values")


# # Total Profit and Quantity by Category

# In[86]:


print("Total Profit and Quantity by Category:")
category_group = data.groupby('Category')[['Profit', 'Quantity']].sum()
category_group


# # Top 10 orders by Quantity

# In[87]:


print("Top 10 orders by Quantity:")
top_quantity_orders = data.sort_values(by='Quantity', ascending=False).head(10)
top_quantity_orders


# # Top 10 orders by Category

# In[88]:


top_profit=data.sort_values(by='Category',ascending=False).head(10)
top_profit


# # Average Shipping Cost by Market and Region

# In[89]:


avg_shipping_cost = data.groupby(['Market', 'Region'])['Shipping Cost'].mean()
print("Average Shipping Cost by Market and Region:")
avg_shipping_cost


# # Total Profit

# In[90]:


total_profit = data['Profit'].sum()
print("Total Profit:", total_profit)


# # Average Shipping Cost

# In[91]:


avg_shipping_cost = data['Shipping Cost'].mean()
print("Average Shipping Cost:", avg_shipping_cost)


# # Most Common Product Category

# In[92]:


most_common_category = data['Category'].value_counts().idxmax()
print("Most Common Product Category:", most_common_category)


# # Total Quantity Sold

# In[93]:


total_quantity_sold = data['Quantity'].sum()
print("Total Quantity Sold:", total_quantity_sold)


# # Average Profit per Category

# In[94]:


avg_profit_per_category = data.groupby('Category')['Profit'].mean()
print("Average Profit per Category:\n", avg_profit_per_category)


# # highest_profit_orders

# In[95]:


highest_profit_orders=data[data['Profit']==data['Profit'].max()]
highest_profit_orders


# # Selected Columns

# In[96]:


selected_columns = data[['Order ID', 'Order Date', 'Customer Name', 'Product Name', 'Quantity']]
selected_columns


# # Number of Orders per Region

# In[97]:


orders_per_region = data['Region'].value_counts()
print("Number of Orders per Region:\n", orders_per_region)


# # New Csv

# In[98]:


new_csv='new.csv'


# In[99]:


data.to_csv(new_csv, index=False)


# In[100]:


import matplotlib.pyplot as plt


# In[101]:


category_profit = data.groupby('Category')['Profit'].sum().reset_index()

plt.figure(figsize=(5, 6))
plt.bar(category_profit['Category'], category_profit['Profit'])
plt.xlabel('Category')
plt.ylabel('Total Profit')
plt.title('Total Profit by Category')
plt.show()


# In[102]:


profit_by_ship_mode = data.groupby('Ship Mode')['Profit'].sum().reset_index()
plt.figure(figsize=(6, 5))
plt.bar(profit_by_ship_mode['Ship Mode'], profit_by_ship_mode['Profit'], color='purple')
plt.xlabel('Ship Mode')
plt.ylabel('Total Profit')
plt.title('Total Profit by Ship Mode')
plt.show()


# In[103]:


profit_by_segment = data.groupby('Segment')['Profit'].sum().reset_index()
plt.figure(figsize=(5, 6))
plt.pie(profit_by_segment['Profit'], labels=profit_by_segment['Segment'], autopct='%1.1f%%')
plt.title('Profit Distribution by Segment')
plt.tight_layout()
plt.show()


# In[104]:


sub_category_shipping_cost = data.groupby('Sub-Category')['Shipping Cost'].sum()
plt.figure(figsize=(8, 8))
plt.pie(sub_category_shipping_cost, labels=sub_category_shipping_cost.index, autopct='%1.1f%%', startangle=140)
plt.title('Shipping Cost Distribution by Sub-Category')
plt.show()


# In[105]:


order_priority_shipping_cost = data.groupby('Order Priority')['Shipping Cost'].sum().reset_index()
plt.figure(figsize=(8, 6))
plt.bar(order_priority_shipping_cost['Order Priority'], order_priority_shipping_cost['Shipping Cost'], color='green')
plt.xlabel('Order Priority')
plt.ylabel('Total Shipping Cost')
plt.title('Total Shipping Cost by Order Priority')
plt.show()


# In[ ]:





# In[ ]:





# # Summary 

# 
# 
# **Number of Orders per Region:**
# - The data includes the number of orders in various regions, with Western Europe having the highest number of orders (5883), followed by Central America (5616), and Oceania (3487).
# 
# **Average Profit per Category:**
# - The data shows the average profit per category, with Technology having the highest average profit (57.31), followed by Furniture (29.59), and Office Supplies (15.74).
# 
# **Total Quantity Sold:**
# - The total quantity of products sold across all categories is 178312.
# 
# **Most Common Product Category:**
# - The most common product category is Office Supplies.
# 
# **Average Shipping Cost:**
# - The average shipping cost for all orders is approximately 26.48.
# 
# **Total Profit:**
# - The total profit from all orders is 1365289.06.
# 
# **Average Shipping Cost by Market and Region:**
# - The data provides the average shipping cost based on different markets and regions. For example, in the Africa market, the Central Africa region has an average shipping cost of 25.49, while in the Asia Pacific market, Eastern Asia has an average shipping cost of 40.37.
# 
# **Total Profit and Quantity by Category:**
# - The total profit and quantity of products sold are provided for each category. Technology has the highest total profit and Furniture has the highest total quantity sold.
# 
# **Count of Unique Values in Categorical Columns:**
# - The data includes the count of unique values for various categorical columns, such as Order ID, Day, Ship Mode, Customer ID, etc.
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




