import pandas as pd
inventory=pd.read_csv('inventory.csv')
# print(inventory.head(10))

#3 saving rows into variable
staten_island = inventory.iloc[:10]
# print(staten_island)

#4 saving a column to variable
product_request = staten_island.product_description
# print(product_request)

#5 selecting rows of certain values - no need to use lambda because no if statement or math operations or data modification
seed_request=inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
# print(seed_request)

#6 lambda function if statement on 1 column only
inventory['in_stock'] = inventory.quantity.apply(lambda x: 'True' if x > 0 else 'False')

#7 add column with margin calculation
inventory['total_value'] = inventory['price']*inventory['quantity']
# print(inventory)

#8 
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda,axis=1)

print(inventory)

