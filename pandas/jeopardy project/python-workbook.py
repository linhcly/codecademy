import random
import pandas as pd
pd.set_option('display.max_colwidth', None)

# Loading the data and investigating it
jeopardy_data = pd.read_csv("jeopardy.csv")
# print(jeopardy_data.columns)

# Renaming misformatted columns
jeopardy_data = jeopardy_data.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
# print(jeopardy_data.columns)
# print(jeopardy_data["Question"])

#3
def filter_data(data,words):
  # create lambda function to specify what we want to see if our words are in the "Question column" which in this case is x
  filter = lambda x: all(word in x for word in words)
  # .apply() the lambda function to the Question column and rows are either True to the condition of lambda or False 
  return data.loc[data["Question"].apply(filter)]
    # the .loc selects all rows in dataframe that returns True from the list of True and False from Questions column 

# # Testing the filter function
filtered = filter_data(jeopardy_data, ["King", "England"])
# print(filtered["Question"])

#4 
def filter_data(data,words):
  # add .lower() to make our filtering case IN-sensitive
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # .apply() the lambda function to the Question column and rows are either True to the condition of lambda or False 
  return data.loc[data["Question"].apply(filter)]
    # the .loc selects all rows in dataframe that returns True from the list of True and False from Questions column 

# Testing the filter function
filtered = filter_data(jeopardy_data, ["King", "England"])
# print(filtered["Question"])

#5 Find the mean value of questions that has the word king in it 
#Remove any string that couldn't be coverted to numerical
replacement_pairs = [('\$',''),(',',''),('None','0')]
for original,new in replacement_pairs:
  jeopardy_data['Value'] = jeopardy_data['Value'].replace(original,new,regex=True)
#Convert the dtype of 'Value' column to float and put it in a new column
jeopardy_data['New_Value'] = pd.to_numeric(jeopardy_data['Value'])

# print(jeopardy_data.New_Value.head(100))

# filter out the rows with the word king in it and create new df then calculate mean of that column
df_king = filter_data(jeopardy_data,'king')
# print(df_king.New_Value.mean())
# mean of value of 'king' questions is $777.49

#6. Write a function that returns the count of unique answers to all of the questions in a dataset

def value_counts(data):
  return data.Answer.value_counts()

#test value count function
# print(value_counts(df_king))

#7.1 Investigate how many questions in the 90s use the word "computer" vs the 2000s
#convert Air Date column using pd.to_datetime so we can use dt.year or dt.month to select certain data
jeopardy_data['Air Date']=pd.to_datetime(jeopardy_data['Air Date'])

nineties=jeopardy_data[(jeopardy_data["Air Date"].dt.year >= 1990)&(jeopardy_data["Air Date"].dt.year <= 1999)]
# print(nineties)                       
#this code above provides nineties dataframe, we need questions that has the word computer using the function we built above

computer_nineties = filter_data(nineties,["Computer"])
# print(len(computer_nineties))
#98 rows of questions with the word computer in the 90s

twothou = jeopardy_data[(jeopardy_data["Air Date"].dt.year >= 2000)&(jeopardy_data["Air Date"].dt.year <= 2999)]
computer_twothou = filter_data(twothou,["Computer"])
# print(len(computer_twothou))
#327 rows of questions with the word computer in the 2000s

#7.2 Are you more likely to find "Literature" in Single Jeopardy or Double Jeopardy

def filter_data2(data,words):
  # add .lower() to make our filtering case IN-sensitive
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # .apply() the lambda function to the Question column and rows are either True to the condition of lambda or False 
  return data.loc[data["Category"].apply(filter)]

single_jeopardy=jeopardy_data[jeopardy_data['Round']=='Jeopardy!']
double_jeopardy=jeopardy_data[jeopardy_data['Round']=='Double Jeopardy!']

# print(len(filter_data2(single_jeopardy,"Literature")))
# print(len(filter_data2(double_jeopardy,"Literature")))

# there are 4603 literature questions in double jeopardy than single jeopardy questions 

#7.3 build a system to quiz yourself, grab random questions and use the input function to get response from the user 

def get_random_question():
  random_number=random.randint(1,len(jeopardy_data))
  print(jeopardy_data['Question'][random_number])
  user_input=input('Your response: ').lower()
  if user_input == jeopardy_data['Answer'][random_number].lower():
    print("True")
    print(jeopardy_data['Answer'][random_number])
  elif user_input != jeopardy_data['Answer'][random_number].lower():
    print("False")
    print(jeopardy_data['Answer'][random_number])

get_random_question()











