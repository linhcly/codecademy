import csv
smoker = []
sex = []
age = []
children = []
charges = []
region = []
bmi = []
insurance_data = []

with open('insurance.csv') as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv,delimiter=',')
    for row in insurance_reader:
        smoker.append(row['smoker'])
        sex.append(row['sex'])
        age.append(row['age'])
        children.append(row['children'])
        charges.append(row['charges'])
        region.append(row['region'])
        bmi.append(row['bmi'])
        insurance_data.append(row)

# 1. what is the average age of people in the dataset 

def average_age(age_list):
  total_age = 0
  for num in age_list:
     total_age += int(num)
  average = total_age/len(age_list)
  return "average age is: "+str(round(average,2))
# print(average_age(age))
#Conclusion: 39.21 years old


# 2. how many people are smoker?
def smoker_count(smoker_list):
    smoker_num = 0
    non_smoker_num = 0
    for n in smoker_list: 
      if n == 'yes':
        smoker_num += 1
      else:
         non_smoker_num += 1 
    return smoker_num,non_smoker_num
    
# print(smoker_count(smoker))
#  = 274 smokers out of 1338


#3.how many males and females in this dataset?
def gender_count(sex_list):
    female = 0
    male = 0 
    for n in sex_list:
      if n == "male":
         male += 1
      else:
         female += 1
    return "female count: "+str(female),"male count: "+str(male)

# print(gender_count(sex))
# Conclusion: 662 females and 676 males

#4.are males more likely to smoke than females? 
def smoker_sex(insurance_data_dict):
   female_smoker = 0
   male_smoker = 0
   for row in insurance_data_dict:
    if row['sex'] == 'male' and row['smoker'] == 'yes':
       male_smoker += 1
    elif row['sex'] == 'female' and row['smoker'] == 'yes':
       female_smoker += 1
   return "female smoker: "+str(female_smoker), "male smoker: "+str(male_smoker)

# print(smoker_sex(insurance_data))
# Conclusion: more males are smokers than females (115 female smokers, 159 male smokers despite having more females in the dataset than males)
     

#5. is the average insurance cost of single male who is non smoker higher than single females non-smoker 
#does gender play a role in cost?
def nsmoker_cost(insurance_data_dict):
   female_nsmoker_cost = []
   male_nsmoker_cost = []
   for row in insurance_data_dict:
      if row['sex'] == 'male' and row['smoker'] == 'no' and row['children'] == '0':
         male_nsmoker_cost.append(float(row['charges']))
      elif row['sex'] == 'female' and row['smoker'] == 'no' and row['children'] == '0':
         female_nsmoker_cost.append(float(row['charges']))
   return "single male non-smoker cost: "+str(round(sum(male_nsmoker_cost)/len(male_nsmoker_cost),2)),"single female non-smoker cost: :"+ str(round(sum(female_nsmoker_cost)/len(female_nsmoker_cost),2))
                      
# print(nsmoker_cost(insurance_data))        

#('single male non-smoker cost: 7530.81', 'single female non-smoker cost: :7688.32')
# this data might be biased since bmi is not considered as a factor in calculation 
#Conclusion: gender does play a role in insurance cost

# 6.what is the average age of people with 1 children?
def avg_age(insurance_data_dict):
   average_age = []
   for row in insurance_data_dict:
      if row['children'] == '1':
         average_age.append(int(row['age']))
   return "Average age of people with 1 child is: "+str(sum(average_age)/len(average_age))

# print(avg_age(insurance_data))
# Average age of people with 1 child is: 39.4537037037037

      



            