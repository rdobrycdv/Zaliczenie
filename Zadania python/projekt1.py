import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#from subprocess import check_output
#print(check_output(["ls", "/Users/radek/Desktop/Zadania python"]).decode("utf8"))

train_df = pd.read_csv('/Users/radek/Desktop/Zadania python/train.csv', header=0,index_col=0)
test_df = pd.read_csv('/Users/radek/Desktop/Zadania python/test.csv', header=0,index_col=0)
full = pd.concat([train_df , test_df], sort=True)

#full.info() #podstawowe informacje o pliku
#full.head() #pokazuje pierwsze wiersze
#full[["Age","Pclass"]][5:30] # wybieranie konkretnej kolumny
#full[:5] #5 pierwszych kolumn
#full.isnull().sum() #szukanie pustych wierszy
full['_Sex'] = pd.Categorical(full.Sex).codes
full['_Embarked'] = pd.Categorical(full.Embarked).codes #kategoryzacja
full['_CabinType'] = pd.Categorical(full['Cabin'].astype(str).str[0]).codes
cols = ['Age','_Embarked','Fare','Parch','Pclass','_Sex','SibSp','Survived','_CabinType']
full[cols].corr() #sprawdzanie korelacji  z tabeli wynika, ze najwiekszy wplyw na przezycie ma plec, nastepnie oplata za bilet oraz typ kabiny
pat = r",\s([^ .]+)\.?\s+"

full['Title'] =  full['Name'].str.extract(pat,expand=True)[0]
full.groupby('Title')['Title'].count() #posortowanie osob wg tytulu oznacza to ze najwiecej jest MR, Miss, MRs i Master
full.loc[full['Title'].isin(['Mlle','Ms','Lady']),'Title'] = 'Miss'
full.loc[full['Title'].isin(['Mme']),'Title'] = 'Mrs'
full.loc[full['Title'].isin(['Sir']),'Title'] = 'Mr'
full.loc[~full['Title'].isin(['Miss','Master','Mr','Mrs']),'Title'] = 'Other' # NOT IN
full['_Title'] = pd.Categorical(full.Title).codes

full.groupby('Title')['Title'].count() #grupowanie na glowne grupy tytlulow
full['TicketCounts'] = full.groupby(['Ticket'])['Ticket'].transform('count') # ten sam numer biletu
#full['Age'].hist(); #historgam dla wieku najwiecej ludzi w przedzaile 18 do 31 lat

#full[full['Survived']==1]['Age'].hist(bins=30) #ilosc osob ktore przezyly wg wieku

plt_all = plt.hist(full['Age'],bins = 30,  range = [0,100],label='all')
plt_survived =plt.hist(full[full['Survived']==1]['Age'], bins = 30, range = [0,100],label='Survived') #nalozenie na siebie wykresow wieku, oraz wieku osob ktore przezyly, widac ze najwiekszy procent ocalaclych to dzieci
plt.legend()
plt.show()

#full['Sex'].hist(); #ilosc kobiet i mezczyzn (prawie dwa razy wiecej mezczyzn)
#full[full['Survived']==1]['Sex'].hist(bins=30) #liczba kobiet i mezczyzn ktorzy przezyli
plt_all = plt.hist(full['Sex'],bins = 6,  range = [0,2],label='all')
plt_survived =plt.hist(full[full['Survived']==1]['Sex'], bins = 6, range = [0,2],label='Survived') #nalozenie na siebie wykresow plci, oraz plci osob ktore przezyly, widac ze przezylo dwa razy wiecej kobiet, przy o polowe mniejszym udziale w tej populacji
plt.legend()
plt.show()

plt_all = plt.hist(full['Cabin'],bins = 6,  range = [0,2],label='all')
plt_survived =plt.hist(full[full['Survived']==1][''], bins = 6, range = [0,2],label='Survived') #nalozenie na siebie wykresow plci, oraz plci osob ktore przezyly, widac ze przezylo dwa razy wiecej kobiet, przy o polowe mniejszym udziale w tej populacji
plt.legend()
plt.show()
