import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# print(ad_clicks.head(5))

ad_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
# print(ad_views)
#3
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#4
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
# print(clicks_by_source)

#5
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
# print(clicks_pivot)

#6 
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
# print(clicks_pivot)

#7 
AB_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
# print(AB_count)

#8 
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

#9 
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