# just testing out a new branch
# code below is not modified!

# =============================================================================
# WordCloud - April 22, 2021
# =============================================================================
'''
https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
'''

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import os

path = 'C:/Users/siewm/OneDrive/Desktop/DNN practice/WordCloud tutorial/'
os.chdir(path)

test = open('jeff_bezos_speech.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

print(len(stopwords))

wc = WordCloud(
    background_color = 'white',
    stopwords=stopwords,
    height = 600,
    width = 400)

wc.generate(test)

wc.to_file('wc_output.png')

# %%

# =============================================================================
# Automate Excel with Python tutorial - April 22, 2021
# =============================================================================

import pandas as pd
import datetime as dt
import calendar
import os
import plotly
import plotly.express as px

path = 'C:/Users/siewm/OneDrive/Desktop/DNN practice/Automate Excel with Python Tutorial/'
os.chdir(path)

filesname = ['January.xlsx','February.xlsx','March.xlsx']

combined = pd.DataFrame()

for file in filesname:
    df = pd.read_excel(file)
    df['Date'] = df['Date'].dt.date
    df['Day'] = pd.DatetimeIndex(df['Date']).day
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df['Year'] = pd.DatetimeIndex(df['Date']).year
    df['Month_name'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
    print('Length of ', file, '-', len(df))
    combined = combined.append(df, ignore_index = True)


barchart = px.bar(combined, x='Month_name', y='Sales', title='Sales Q1 2020')

# export bar chart to HTML
plotly.offline.plot(barchart, filename='Sales_Q1_2020.html')

combined.to_excel('SalesQ120.xlsx', index = False)


# %%
# =============================================================================
# DataCamp - Importing data in Python - April 29, 2021
# =============================================================================

# starting a line with ! gives you complete system shell access. 
# This means that the IPython magic command ! ls will display the contents of your current directory. 
 
# A method read() is used like file.read()

# Open a file: file
file = open('moby_dick.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file using the close() method
file.close()

# Check whether file is closed
print(file.closed)


# Import package
import numpy as np

# Assign filename to variable: file
file = 'digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits using the function type().
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

#numpy arrays have to contain elements that are all the same type


import os    #The first line of the following code imports the library os
wd = os.getcwd()    #stores the name of the current directory in a string called wd
os.listdir(wd)    #outputs the contents of the directory in a list to the shell.
 
# SQL
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
# Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6. 
# Use the >= operator and assign the results to rs.
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())


# %%
# =============================================================================
# colorama - May 12, 2021
# =============================================================================

#import colorama
from colorama import Fore, Back, Style

print('\nwith Fore.RESET and Style.BRIGHT at every line.')
print(Fore.RED + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.GREEN + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.BLUE + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.CYAN + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.YELLOW + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(Fore.WHITE + Style.BRIGHT + 'Hello World' + Fore.RESET)
print(f"{Style.BRIGHT}{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O{Fore.RESET}")
print(f"{Style.BRIGHT}{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D{Fore.RESET}")
print(f"{Style.BRIGHT}{Fore.BLACK}{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O{Fore.RESET}")
print(f"{Style.BRIGHT}{Fore.BLACK}{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}D{Fore.RESET}")
print(Style.RESET_ALL) #reset, without this line, the Back.MAGENTA setting still there

print('set Style.BRIGHT once in the first line and Style.RESET_ALL at the last line.') #to set Style.BRIGHT to all below until the RESET_ALL code.
print(Style.BRIGHT + Fore.RED + 'Hello World')
print(Fore.GREEN + 'Hello World')
print(Fore.BLUE + 'Hello World')
print(Fore.CYAN + 'Hello World')
print(Fore.YELLOW + 'Hello World')
print(Fore.WHITE + 'Hello World')
print(f"{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O")
print(f"{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D")
print(f"{Fore.BLACK}{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O")
print(f"{Fore.BLACK}{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}D")
print(Style.RESET_ALL)

#without Style.BRIGHT setting.
print('Without the Style.BRIGHT setting')
print(Fore.RED + 'Hello World')
print(Fore.GREEN + 'Hello World')
print(Fore.BLUE + 'Hello World')
print(Fore.CYAN + 'Hello World')
print(Fore.YELLOW + 'Hello World')
print(Fore.WHITE + 'Hello World')
print(f"{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O")
print(f"{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D")
print(f"{Fore.BLACK}{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O")
print(f"{Fore.BLACK}{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}D")
print(Style.RESET_ALL)
















