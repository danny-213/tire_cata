import pandas as pd 
import json


df = pd.read_excel('MBVCO102023_Product list.xlsx')
print(df.head())

df_dict = df.to_dict('records')
print(df_dict)

# Assuming you have your list of dictionaries in the variable 'data_list'

# Open a file in write mode
with open('products.json', 'w') as f:

    # Dump the list as JSON data
    json.dump(df_dict, f, indent=4)  # Indentation for readability

print("JSON data saved to 'products.json'")