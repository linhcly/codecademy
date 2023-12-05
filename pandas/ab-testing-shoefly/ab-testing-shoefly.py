import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# print(ad_clicks.head(5))

#2.How many views (i.e., rows of the table) came from each utm_source
ad_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
# print(ad_views)

#3 If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.
# Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#4 We want to know the percent of people who clicked on ads from each utm_source.
# Group utm_source and is_click and counting the number of user_id‘s in each of those groups. 
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
# print(clicks_by_source)

#5 pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
# print(clicks_pivot)

#6 Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.
# Was there a difference in click rates for each source?

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
# print(clicks_pivot)

#Analyzing A/B test

#7 The column experimental_group tells us whether the user was shown Ad A or Ad B.
# Were approximately the same number of people shown both ads?
AB_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
# print(AB_count)

#8 Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B
percentAB = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

#put results into pivot 
ABpivot = percentAB.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()

#add percentage column into pivot 
ABpivot['percent_clicked'] = ABpivot[True] / (ABpivot[True] + ABpivot[False])
# print(ABpivot)

#9 The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.
# Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

#10 determine which ad (A/B) gets more click throughout the days
percenta= a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
percentb= b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
apivot=percenta.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
bpivot=percentb.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
apivot['percent_clicked']=apivot[True]/(apivot[True]+apivot[False])
print(apivot)
bpivot['percent_clicked']=bpivot[True]/(bpivot[True]+bpivot[False])
print(bpivot)