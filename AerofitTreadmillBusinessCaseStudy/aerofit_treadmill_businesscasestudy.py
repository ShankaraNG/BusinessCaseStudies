# -*- coding: utf-8 -*-
"""Aerofit_Treadmill_businesscasestudy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ByG7TDt9K2jPd_eeHqXQVORY7GX7duCA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

!gdown 1dKDbIRYiiohz9YCGeWJnIaVcROORupNM

areofit_df = pd.read_csv("aerofit_treadmill.csv")

areofit_df = pd.DataFrame(areofit_df)
areofit_df.head(5)

"""# Initial Analysis"""

areofit_df.shape

"""Data Set has 180 rows and 9 coloumns"""

areofit_df.describe(include='all')

"""The Given Data has the below mentioned Features
*   There are Three unique products of Aerofit
*   Max Age is 50
*   MAX income is 104581
*   Highest miles is 360
*   There are two marital status that is Partnered and Single
*   top selling produyct is KP281 and the no of it sold are 80
*   Most of the customers are Male who are 104 out of 180




"""

areofit_df.info()

"""The data types of the coloumns is as given above"""

areofit_df.isna().value_counts()

"""There is no null values present in any coloumns"""

areofit_df.duplicated().value_counts()

"""There is no duplicate data present in the given data set"""

areofit_df['Product'].unique()

"""We have mainly three types of product that are 'KP281', 'KP481' and 'KP781'"""

areofit_df['Gender'].value_counts()

"""out of the total 180 customer 104 are males and 76 are females"""

areofit_df['MaritalStatus'].value_counts()

"""out of the 180 customers 107 are Married and 73 are singles customers"""

areofit_df['Education'].value_counts()

"""unique Educations and its count"""

areofit_df['Fitness'].value_counts().sort_index()

"""We have five category of fitness and we can see that fitness of category 3 is highest

Converting the Fitness to a given category based on the fitness index

*   1=>Very Poor Fitness
*   2=>Poor Fitness
*   3=>Average Fitness
*   4=>Good Fitness
*   5=>Very Good Fitness
"""

aerofittm_df=areofit_df
def fitnesscategorydriver(data):
  if(data==1):
    return "Very Poor"
  elif(data==2):
    return "Poor"
  elif(data==3):
    return "Average"
  elif(data==4):
    return "Good"
  elif(data==5):
    return "Very Good"

aerofittm_df['Fitness_category']=aerofittm_df['Fitness'].apply(fitnesscategorydriver)
aerofittm_df=pd.DataFrame(aerofittm_df)
aerofittm_df['Fitness_category'].value_counts()

"""# **Univariate Analysis**

Product sold analysis of Aerofit
"""

def productssoldcount(data):
  print("The count of unique product sold are as listed below")
  print(data['Product'].value_counts())
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Product', hue='Product', palette='Set1', legend=False)
  plt.title("Product Sold count")
  plt.xlabel("Product")
  plt.ylabel("count")
  plt.show()

productssoldcount(aerofittm_df)

"""we can say that the highest no of products sold is KP281

Gender based analysis on the treadmills purchased
"""

def genderspurchcount(data):
  print("Gender count of the customer who brought the product")
  print(data['Gender'].value_counts())
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Gender', hue='Gender', palette='Set1', legend=False)
  plt.title("Gender count")
  plt.xlabel("Gender")
  plt.ylabel("count")
  plt.show()

genderspurchcount(aerofittm_df)

"""We have more male customer which accounts to about 104

Marital status based analysis on the treadmills purchased
"""

def maritialbasedcount(data):
  print("Maritial count")
  print(data['MaritalStatus'].value_counts())
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='MaritalStatus', hue='MaritalStatus', palette='Set1', legend=False)
  plt.title("Maritial count")
  plt.xlabel("Marital Status")
  plt.ylabel("count")
  plt.show()

maritialbasedcount(aerofittm_df)

"""Most of the customers who have purchased the treadmill are married and account of 107 in total

Fitness category analysis
"""

def fitnesscategorybasedcount(data):
  print("Count of Fitness category they belong to")
  print(data['Fitness_category'].value_counts())
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Fitness_category', hue='Fitness_category', palette='Set1', legend=False)
  plt.title("Fitness Category count")
  plt.xlabel("Fitness Category")
  plt.ylabel("count")
  plt.show()

fitnesscategorybasedcount(aerofittm_df)

"""Most of the customer who bought the treadmill are of average fitness

Analysis on the Income
"""

def fitnessincomecount(data):
  print("Income based distribution")
  print(data['Income'].value_counts())
  plt.figure(figsize=(12,6))
  sns.histplot(data=data, x='Income', kde=True)
  plt.title("Income base distribution")
  plt.xlabel("Income Category")
  plt.ylabel("count")
  plt.show()

fitnessincomecount(aerofittm_df)

"""we can see that most of them have an income in the range of 45k to 50k."""

aerofittm_df.head(4)

"""Analysis on Miles"""

def fitnessMilescount(data):
  print("Miles based distribution")
  print(data['Miles'].value_counts())
  plt.figure(figsize=(12,6))
  sns.histplot(data=data, x='Miles', kde=True)
  plt.title("Miles distribution")
  plt.xlabel("Miles Category")
  plt.ylabel("count")
  plt.show()

fitnessMilescount(aerofittm_df)

"""This is the miles ran distribution by the customers

Usage Analysis
"""

def fitnessUsagecount(data):
  print("Usage based distribution")
  print(data['Usage'].value_counts())
  plt.figure(figsize=(12,6))
  sns.histplot(data=data, x='Usage', kde=True)
  plt.title("Usage distribution")
  plt.xlabel("Usage Category")
  plt.ylabel("count")
  plt.show()

fitnessUsagecount(aerofittm_df)

"""Education Analysis"""

def fitnessEducationcount(data):
  print("Education based distribution")
  print(data['Education'].value_counts())
  plt.figure(figsize=(12,6))
  sns.histplot(data=data, x='Education', kde=True)
  plt.title("Education distribution")
  plt.xlabel("Education Category")
  plt.ylabel("count")
  plt.show()

fitnessEducationcount(aerofittm_df)

"""Age Analysis"""

aerofittm_df['Age'].unique()

"""Based ont he above result let us categorize

*Age Categories*
*   Adolescent => 18-22
*   Young Adult => 22-25
*   Adult => 25-35
*   Middle-Aged => 35-59
*   Senior=> 60-100                                             
"""

bins = [18, 22, 25, 35, 59, 100]
labels = ['Adolescent', 'Young Adult', 'Adult', 'Middle-Aged', 'Senior']

aerofittm_df['Age_Category'] = pd.cut(aerofittm_df['Age'], bins=bins, labels=labels, right=False)
print(aerofittm_df.head(10))

def fitnessagecount(data):
  print("Age distribution")
  print(data['Age'].value_counts())
  plt.figure(figsize=(12,6))
  sns.histplot(data=data, x='Age', kde=True)
  plt.title("Age distribution")
  plt.xlabel("Age Category")
  plt.ylabel("count")
  plt.show()

  print("Age Category distribution")
  print(data['Age_Category'].value_counts())
  plt.figure(figsize=(12,6))
  sns.histplot(data=data, x='Age_Category', kde=True)
  plt.title("Age Category distribution")
  plt.xlabel("Age Category ")
  plt.ylabel("count")
  plt.show()


fitnessagecount(aerofittm_df)

"""We can see from above most of them are of age 25 and belong to adult category

# **Outliers identification**
"""

def fitnessagecount(data,coloumn):
  for i in coloumn:
    plt.figure(figsize=(12,6))
    sns.boxplot(data=data, x=i)
    title=i+" outliers"
    plt.title(title)
    plt.xlabel(i)
    plt.show()

coloumn=['Age', 'Education', 'Usage', 'Fitness', 'Income', 'Miles']
fitnessagecount(aerofittm_df,coloumn)

"""we do have outliers present in the given data mainly in the miles and income category where anything more  than 200 miles is considered as an outlier.
Where for the income anything more 80K is considered as an outlier

Age,Education and Usuage have very few outliers. Age anything above 45 is considered as an outlier and for Education anything above 20 is an outlier and usuage of 6 or above is considered as an outlier

# **HeatMaps for Correlation**
"""

plt.figure(figsize=(20,6))
aerofittmf_df=aerofittm_df[['Age', 'Education', 'Usage', 'Fitness', 'Income', 'Miles']]
sns.heatmap(aerofittmf_df.corr(),annot=True,fmt='.4f',linewidths=.5,cmap='coolwarm')
plt.yticks(rotation=0)
plt.show()

"""In the above heatmap
Correlation between Age and Miles is 0.0366
Correlation between Education and Income is 0.6258
Correlation between Usage and Fitness is 0.6686
Correlation between Fitness and Age is 0.0611
Correlation between Income and Usage is 0.5195
Correlation between Miles and Age is 0.0366
"""

coloumn=['Product', 'Gender', 'MaritalStatus']
for i in coloumn:
  plt.figure(figsize=(20,6))
  sns.pairplot(aerofittm_df,hue=i ,kind='reg')
  plt.show()

"""# **Bivarent Analysis**

Analysis with respect to product and Age,Education.usage,Fitness and Miles
"""

coloumns = ['Age', 'Education', 'Usage', 'Fitness', 'Miles']
for i in coloumns:
  print("Analysis on "+i)
  print("")
  print(aerofittm_df.groupby('Product')[i].mean())
  print("")

"""Observation

Product and Age
*   Mean Age of the customer who purchased product KP281 is 28.55
*   Mean Age of the customer who purchased product KP481 is 28.90
*   Mean Age of the customer who purchased product KP781 is 29.10

Product and Education
*   Mean Education qualification of the customer who purchased product KP281 is 15.03
*   Mean Education qualification of the customer who purchased product KP481 is 15.11
*   Mean Education qualification of the customer who purchased product KP781 is 17.32

Product and Usage
*   Customer usage mean for product KP281 is 3.08
*   Customer usage mean for product KP481 is 3.06
*   Customer usage mean for product KP781 is 4.77

Product and Fitness

*   Customer fitness mean for product KP281 is 2.96
*   Customer fitness mean for product KP481 is 2.90
*   Customer fitness mean for product KP781 is 4.62

Product and Miles

*   Customer miles mean for product KP281 is 82.78
*   Customer miles mean for product KP481 is 87.93
*   Customer miles mean for product KP781 is 166.90

We will further analyze on product vs rest of the coloumns as  mentioned below
*   Product vs Age
*   Product vs Gender
*   Product vs Education
*   Product vs Marital Status
*   Product vs Usage
*   Product vs Fitness
*   Product vs Income
*   Product vs Miles

Product Vs Age
"""

def productvsage(data):
  plt.figure(figsize=(12,6))
  sns.boxplot(data=data, x='Age', hue='Product')
  title="Product vs Age"
  plt.title(title)
  plt.xlabel("Age")
  plt.show()

productvsage(aerofittm_df)

"""Most of the people who brought KP281 are within the age of 20 to 48 and average age of 26
Most of the people who brought KP481 are within the age of 20 to 45 and average age of 26
Most of the people who brought KP481 are within the age of 22 to 38 and average age of 28

Product vs Gender
"""

def productvsgender(data):
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Product', hue='Gender')
  title="Product vs Gender"
  plt.title(title)
  plt.xlabel("Product")
  plt.show()

productvsgender(aerofittm_df)

"""Both male and female have purchased the product KP281 the same
Male have purchased the product KP481 more
Males have purchased the product KP781 significantly more

Product Vs Education
"""

def productvsage(data):
  plt.figure(figsize=(12,6))
  sns.boxplot(data=data, x='Education', hue='Product')
  title="Product vs Education"
  plt.title(title)
  plt.xlabel("Education")
  plt.show()

productvsage(aerofittm_df)

"""People who have purchased the product KP281 and KP481 seems to have the same education trend
People who have purchased the product KP781 seem to be on the higher educated background

Product Vs Marital Status
"""

def productvsmarriage(data):
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Product', hue='MaritalStatus')
  title="Product vs Marital Status"
  plt.title(title)
  plt.xlabel("Product")
  plt.show()

productvsmarriage(aerofittm_df)

"""The product KP281 is used by Married people more than that of the single ones and are significantly large compared to KP481 and KP781 as seen above

Product vs Usage
"""

def productvsUsage(data):
  plt.figure(figsize=(12,6))
  sns.boxplot(data=data, x='Usage', hue='Product')
  title="Product vs Usage"
  plt.title(title)
  plt.xlabel("Usage")
  plt.show()

productvsUsage(aerofittm_df)

"""We have KP281 and KP781 usage as more compared to that of KP481

Product vs Fitness
"""

def productvsFitness(data):
  plt.figure(figsize=(12,6))
  sns.kdeplot(data=data, x='Fitness', hue='Product')
  title="Product vs Fitness"
  plt.title(title)
  plt.xlabel("Fitness")
  plt.show()

productvsFitness(aerofittm_df)

"""We have the fitness of the product KP281 and KP481 more due to higher spike

Product vs Income
"""

def productvsIncome(data):
  plt.figure(figsize=(12,6))
  sns.kdeplot(data=data, x='Income', hue='Product')
  title="Product vs Income"
  plt.title(title)
  plt.xlabel("Income")
  plt.show()

productvsIncome(aerofittm_df)

"""People who purchase the product KP281 and KP481 have higher spikes compared to KP781

Product vs Miles
"""

def productvsMiles(data):
  plt.figure(figsize=(12,6))
  sns.kdeplot(data=data, x='Miles', hue='Product')
  title="Product vs Miles"
  plt.title(title)
  plt.xlabel("Miles")
  plt.show()

productvsMiles(aerofittm_df)

"""People who purchase the product KP281 and KP481 have higher spikes in miles compared to KP781

Gender analysis done on the rest of the fields as mentioned below
*   Gender vs Usage
*   Gender vs Fitness
*   Gender vs Income
*   Gender vs Miles
"""

def Gendervsusage(data):
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Usage', hue='Gender')
  title="Usage vs Gender"
  plt.title(title)
  plt.xlabel("Usage")
  plt.show()

Gendervsusage(aerofittm_df)

"""Among Male and Female Males usage higher in 4 days per week
Female customers mostly use 3 days per week
Only few Male customers use 7 days per week whereas female customers maximum usage is only 6 days per week

Gender vs Fitness
"""

def GendervsFitness(data):
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Fitness', hue='Gender')
  title="Fitness vs Gender"
  plt.title(title)
  plt.xlabel("Fitness")
  plt.show()

GendervsFitness(aerofittm_df)

"""We can see that Among Males and females males have higher average fitness
Even among the Average fitness that is 3 males are having higher than females

Gender vs Income
"""

def GendervsIncome(data):
  plt.figure(figsize=(12,6))
  sns.kdeplot(data=data, x='Income', hue='Gender')
  title="Income vs Gender"
  plt.title(title)
  plt.xlabel("Income")
  plt.show()

GendervsIncome(aerofittm_df)

"""We can see that both male and female have equal higher or peak income in the range of 20K to 80K and peak of about 40K

Gender vs Miles
"""

def GendervsMiles(data):
  plt.figure(figsize=(12,6))
  sns.kdeplot(data=data, x='Miles', hue='Gender')
  title="Miles vs Gender"
  plt.title(title)
  plt.xlabel("Miles")
  plt.show()

GendervsMiles(aerofittm_df)

"""Seems like over all males have a higher Mile range than female but they both peak at the same level

Analysis is on How Marital Status affects the rest of the values

*   Marital vs Usage
*   Marital vs Fitness
*   Marital vs Income
*   Marital vs Miles
"""

def Maritalvsusage(data):
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Usage', hue='MaritalStatus')
  title="Usage vs Marital Status"
  plt.title(title)
  plt.xlabel("Usage")
  plt.show()

Maritalvsusage(aerofittm_df)

"""People who have married have an higher usuage value in 3 and people who are single tend to stop of the usage value of 6

Marital vs Fitness
"""

def MaritalvsFitness(data):
  plt.figure(figsize=(12,6))
  sns.countplot(data=data, x='Fitness', hue='MaritalStatus')
  title="Fitness vs Marital Status"
  plt.title(title)
  plt.xlabel("Fitness")
  plt.show()

MaritalvsFitness(aerofittm_df)

"""People who are single have a higher fitness in terms of average fitness that is 3

Marital vs Income
"""

def MaritalvsIncome(data):
  plt.figure(figsize=(12,6))
  sns.kdeplot(data=data, x='Income', hue='MaritalStatus')
  title="Income vs Marital Status"
  plt.title(title)
  plt.xlabel("Income")
  plt.show()

MaritalvsIncome(aerofittm_df)

"""Parterned people have higher income in the range of 20K to 80K and peak at 45K

Marital vs Miles
"""

def MaritalvsMiles(data):
  plt.figure(figsize=(12,6))
  sns.kdeplot(data=data, x='Miles', hue='MaritalStatus')
  title="Miles vs Marital Status"
  plt.title(title)
  plt.xlabel("Miles")
  plt.show()

MaritalvsMiles(aerofittm_df)

"""Partnered people have higher Miles and peak at the value close to 90

# **Outlier Detection and probability**

Inter Quartile Range
"""

def interquartilerange(data , coloumn):
  for i in coloumn:
    q1=np.percentile(data[i], 25)
    q3=np.percentile(data[i], 75)
    quartile = q3-q1
    print("The Inter Quartile Range of "+i+" is",quartile)


coloumn=['Age', 'Education', 'Usage', 'Fitness', 'Income', 'Miles']
interquartilerange(aerofittm_df,coloumn)

"""Probability of Product for given gender"""

probabilityofp=pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Gender']],margins=True)
print(probabilityofp)
np.round(((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Gender']],margins=True))/180)*100,2)

"""With the above data we can calculate the probability of each product with respect to the genders

Marginal Probability

Probability of Male Customer Purchasing product is 57.77

Probability of Female Customer Purchasing product is 42.22

Marginal Probability of any customer buying

product KP281 is : 44.44

product KP481 is : 33.33

product KP781 is : 22.22
"""

np.round((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Gender']],margins=True, normalize="columns"))*100,2)

"""Probability of Selling Product

p(KP281|Female) = 52
p(KP481|Female) = 38
p(KP781|Female) = 10
p(KP281|male) = 38
p(KP481|male) = 30
p(KP781|male) = 32

Probability of product given MaritalStatus
"""

probabilityofg=pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['MaritalStatus']],margins=True)
print(probabilityofg)
np.round(((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['MaritalStatus']],margins=True))/180)*100,2)

"""Marginal Probability

Probability of Married Customer Purchasingproduct is 59.44

Probability of Single Customer Purchasing product is 40.56

Marginal Probability of any customer buying

product KP281 is : 44.44

product KP481 is : 33.33

product KP781 is : 22.22
"""

np.round((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['MaritalStatus']],margins=True, normalize="columns"))*100,2)

"""Probability of Selling Product

p(KP281|Married) = 44.86
p(KP481|Married) = 33.64
p(KP781|Married) = 21.50
p(KP281|Single) = 43.84
p(KP481|Single) = 32.88
p(KP781|Single) = 23.29

Probability of a product given Fitness category
"""

probabilityoffg=pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Fitness_category']],margins=True)
print(probabilityoffg)
np.round(((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Fitness_category']],margins=True))/180)*100,2)

"""Marginal Probability

Probability of Fitness Customer of customer as average Purchasing product is 53.89
Probability of Fitness Customer of customer as Good Purchasing product is 13.33
Probability of Fitness Customer of customer as Poor Purchasing product is 14.44
Probability of Fitness Customer of customer as Very Good Purchasing product is 17.22
Probability of Fitness Customer of customer as Very Poor Purchasing product is 1.11

Marginal Probability of any customer buying

product KP281 is : 44.44
product KP481 is : 33.33
product KP781 is : 22.22
"""

np.round((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Fitness_category']],margins=True, normalize="columns"))*100,2)

"""Probability of Selling Product

p(KP281|Average) = 55.67
p(KP481|Average) = 40.21
p(KP781|Average) = 4.12
p(KP281|Good) = 37.50
p(KP481|Good) = 33.33
p(KP781|Good) = 29.17
p(KP281|Poor) = 53.85
p(KP481|Poor) = 46.15
p(KP781|Poor) = 0
p(KP281|Very Good) = 6.45
p(KP481|Very Good) = 0
p(KP781|Very Good) = 93.55
p(KP281|Very Poor) = 50
p(KP481|Very Poor) = 50
p(KP781|Very Poor) = 0

Probability of a product given Age category
"""

probabilityoffg=pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Age_Category']],margins=True)
print(probabilityoffg)
np.round(((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Age_Category']],margins=True))/180)*100,2)

"""Marginal Probability

Probability of Age of customer as Adolocent Purchasing product is 9.44
Probability of Age of customer as Young Adult Purchasing product is 20.56
Probability of Age of customer as Adult Purchasing product is 50
Probability of Age of customer as Middle Aged Purchasing product is 20


Marginal Probability of any customer buying

product KP281 is : 44.44
product KP481 is : 33.33
product KP781 is : 22.22
"""

np.round((pd.crosstab(index=aerofittm_df['Product'],columns=[aerofittm_df['Age_Category']],margins=True, normalize="columns"))*100,2)

"""Probability of Selling Product

p(KP281|Adolescent) = 58.82
p(KP481|Adolescent) = 41.18
p(KP781|Adolescent) = 0
p(KP281|Young Adult) = 45.95
p(KP481|Young Adult) = 27.03
p(KP781|Young Adult) = 27.03
p(KP281|Adult) = 40.00
p(KP481|Adult) = 34.44
p(KP781|Adult) = 25.56
p(KP281|Middle Aged) = 47.22
p(KP481|Middle Aged) = 33.33
p(KP781|Middle Aged) = 19.44

Recommendations


Promote Customers to upgrade from lower versions to next level versions after consistent usages as there are very less people in the usage after 5 category so improvements can be pushed.

Married people prefer product KP281 more and this can be used as our advantage to have marketing done on these products for couples as exercise together to increase the sales.

Female who prefer exercising is low here as  compared to males. we should run a marketing campaign on to encourage women to exercise more

KP281 & KP481 treadmills are preferred by the customers as this is the most used and most of the people income lies around 45K so these models need to be put on offers or sales to increase the products.

As KP781 is better and advanced (based on the data that the male use this product more and is extensively used by higher fitness people) this treadmill should be marketed for professionals and athletes.

KP781 product should be promoted using influencers and other athletes.

KP781 can be recommended for Female customers who exercises extensively as this variant is preferred less.

Market the Adolescents to use the more of KP281 and provide its health benefits.

Target the Age group above 40 years to recommend Product KP781.
"""