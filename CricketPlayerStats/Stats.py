import pandas as pd

df_player = pd.read_csv('C:/Users/Lenovo/Desktop/data/cricketPlayer_ODI.csv')


# 1. A match is randomly choosen, what is the probability that india have won that match?

def randomlywon(df_player):
    total_no = len(df_player)
    win_no = len(df_player.loc[df_player['Won'] == True].value_counts())
    probability_of_winning=round((win_no/total_no),2)
    print("Probability of winning is ",probability_of_winning)   
    
randomlywon(df_player)

#2. A match is choosen at a random, what is the probability that Player has scored a century in that match?

def century(df_player):
    total_no = len(df_player)
    century_no = len(df_player.loc[df_player['century'] == True].value_counts())
    probability_of_century=round((century_no/total_no),2)
    print("Probability of scoring a century is ",probability_of_century)   
    
century(df_player)


#3 Find how many matches india have won when Player score a  century
#4 Find how many matches india have won when Player didn't score a century

def century_won(df_player):
    total_no = len(df_player)
    century_no = len(df_player.loc[(df_player['century'] == True) & (df_player['Won'] == True)].value_counts())
    probability_of_century=round((century_no/total_no),2)
    print("Probability of winnign when the century is scored ",probability_of_century)   
    
century_won(df_player)


def century_false(df_player):
    total_no = len(df_player)
    century_no = len(df_player.loc[(df_player['century'] == False) & (df_player['Won'] == True)].value_counts())
    probability_of_century=round((century_no/total_no),2)
    print("Probability of when century was not scored ",probability_of_century)   
    
century_false(df_player)

