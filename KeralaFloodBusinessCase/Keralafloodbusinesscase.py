import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


data = pd.read_csv('C:/Users/Lenovo/Desktop/data/kerala.csv')
output_directory = ('C:/Users/Lenovo/Desktop/KeralaFloodBusinesscase/figuresfromcode/')


#1) what is the Average of the Rainfall in Kerala Across Every month

def averagecalculator(data,x):
    sumofflood=data[x].sum()
    l=len(data[x])
    avg=sumofflood/l
    return float(avg)

def averagedriver(data):
    x=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    y=[]
    for i in  x:
        avg = round(averagecalculator(data,i),2)
        y.append(avg)
        
    df_avg = pd.DataFrame({
        'Month': x,
        'Average': y
    })
    
    print(df_avg)
    
    plt.figure(figsize=(15, 6))
    sns.barplot(data=df_avg, x='Month', y='Average') 
    plt.xlabel('Month')
    plt.ylabel('Average Count')
    plt.title('Average Rain Fall in Kerala')
    filename="Average_Rain_Fall_in_Kerala.png"
    full_path = os.path.join(output_directory, filename)
    plt.savefig(full_path)
    plt.show()
    plt.close()
        
# averagedriver(data)

#From this we can get to know that the highest rainfall occurs in the month of July which is about 698.22 and least rain fall occurs in the month of Jan which is 12.22
#on an average across the years from 1901 to 2018

#2) what is the The Rainfall in Kerala Across Every month for the last 10 years

df_last10=data.loc[data['YEAR']>=2008]

def a10yeardriver(data):
    x=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    for i in x:
        plt.figure(figsize=(15, 6))
        sns.barplot(data=data, x='YEAR', y=i) 
        plt.xlabel('YEAR')
        plt.ylabel('Count')
        title_name = f"Rain fall for the Month {i}"
        plt.title(title_name)
        filename= f"Rainfallforthemonth{i}.png"
        full_path = os.path.join(output_directory, filename)
        plt.savefig(full_path)
        plt.show()
        plt.close()
        
# a10yeardriver(df_last10)

#3) What is the Annual Rainfall in Kerala for the last 10 Years

def AnnualRainfallfor10years(df_last10):
        plt.figure(figsize=(15, 6))
        sns.barplot(data=df_last10, x='YEAR', y=' ANNUAL RAINFALL') 
        plt.xlabel('YEAR')
        plt.ylabel('Rainfall')
        plt.title("Annual Rainfall in last 10 years")
        filename= "AnnualRainfallforlast10years.png"
        full_path = os.path.join(output_directory, filename)
        plt.savefig(full_path)
        plt.show()
        plt.close()
        
# AnnualRainfallfor10years(df_last10)

#From this we can say that 2018 had the highest ammount of Rain Fall in the last 10 years

#4)Which all years had flood in the last 10 years

def Floodinlast10years(df_last10):
        plt.figure(figsize=(15, 6))
        sns.countplot(data=df_last10, x='YEAR',hue='FLOODS') 
        plt.xlabel('YEAR')
        plt.ylabel('Flood')
        plt.title("Flood in last 10 years")
        filename= "Floodinlast10years.png"
        full_path = os.path.join(output_directory, filename)
        plt.savefig(full_path)
        plt.show()
        plt.close()

Floodinlast10years(df_last10)

# from this we can say that Kerala had floods in the year 2010,11,13,14 and 18.

#5) how much rainfall index is considered as a heavy ranifall?

impactful_columns = ['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', ' ANNUAL RAINFALL', 'FLOODS']
refineddata=data[impactful_columns]
months=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

def mediancalculator(data, months):
    threshold={}
    for i in months:
        threshold[i]=int(data[i].median())
    
    threshold[' ANNUAL RAINFALL']=int(data[' ANNUAL RAINFALL'].median())
    
    return threshold


def mediandriver(data, months):
    heavyrainfall=refineddata
    threshold=mediancalculator(refineddata, months)
    for key, value in threshold.items():
        heavyrainfall[key] = (heavyrainfall[key] > value).astype(int)
    valuesinmonths=[]
    for i in months:
        counts = heavyrainfall[i].value_counts()
        valuesinmonths.append(counts.rename(i))
        
    valuesinmonths_df = pd.concat(valuesinmonths, axis=1)
    print(valuesinmonths_df)
    return valuesinmonths_df,heavyrainfall

valuesinmonths_df,heavyrainfall = mediandriver(refineddata, months)

#6) Probability of flood given that rainfall in June is greater than the median june rainfall value (threshold for heavy rainfall)

heavyrainfall['FLOODS'] = data['FLOODS']

crosstabofjun= pd.crosstab(heavyrainfall['JUN'],
                  heavyrainfall['FLOODS'],
                  margins=True,
                  margins_name='Total')
print(crosstabofjun)
probabilityofjune = round(crosstabofjun.loc[1, 'YES'] / crosstabofjun.loc[1, 'Total'],2)
print(probabilityofjune)

# we can say that the Probability of having flood given that heavy rain fall has occured is 0.74

#7) Given that there is a flooding, calculate the probability that heavy rainfall has occurred in July (more than threshold value)?     

crosstabofjul= pd.crosstab(heavyrainfall['JUL'],
                  heavyrainfall['FLOODS'],
                  margins=True,
                  margins_name='Total')
print(crosstabofjul)
probabilityofjuly = round(crosstabofjul.loc[1, 'YES'] / crosstabofjul.loc['Total', 'YES'],2)
print(probabilityofjune)
    
# The probability of rain fall given there is flooding is 0.73

#8)probability of flood given that june and july rainfall was greater than their median rainfall value?

crosstabofjunjul=pd.crosstab(index = [heavyrainfall['JUN'], heavyrainfall['JUL']],
            columns = heavyrainfall['FLOODS'],
            margins=True,
            margins_name='Total')  

print(crosstabofjunjul) 

probabilityofjunejuly=crosstabofjunjul.loc[1, 1]['YES']/crosstabofjunjul.loc['Total']['YES']
print(probabilityofjunejuly)

#The Probability of flood givenb that huyne and july there is a rainfall is 0.45