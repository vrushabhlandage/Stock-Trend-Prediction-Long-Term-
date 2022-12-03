#import essential librries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import streamlit as st
from datetime import date

# defining dates

start = '2010-01-12'
end = date.today()

startstr = str(start)
endstr = str(end)

st.title('stock trend prediction')

# taking user input

userinput = st.text_input('enter Stock ticker')

# assingning data to dataframe

df = data.DataReader(userinput, 'yahoo', start, end)

#reset index coloumn

df = df.reset_index()

# droping unnecessary coloumn i.e Adj Close

df = df.drop(['Adj Close'], axis=1)

# save data in  csv file format for further use

df.to_csv(userinput + ' From 2010-01-12 till today.csv')

# printing last five day's data
dftail = df.tail()
st.write(dftail)

# Graphical visualization of closing price

st.subheader('closing price')
fig = plt.figure(figsize=(20, 7))
plt.plot(df.Close, 'g')
st.pyplot(fig)

# Graphical visualization of volume

st.subheader('volume')
fig = plt.figure(figsize=(20, 7))
# plt.plot(df.Close, 'g')
plt.plot(df.Volume, 'y')
st.pyplot(fig)


# Graphical visualizatin of closing price with ma100

st.subheader('closing price with ma100')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(20, 7))
plt.plot(ma100, 'b')
plt.plot(df.Close, 'g')
st.pyplot(fig)

# Graphical visualization of closing price with ma200

st.subheader('closing price with ma200')
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(20, 7))
plt.plot(ma200, 'r')
plt.plot(df.Close, 'g')
st.pyplot(fig)

# Graphical visualization of closing price with ma100 and ma200

st.subheader('closing price with ma100 and ma200')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(20, 7))
plt.plot(ma100, 'b')
plt.plot(ma200, 'r')
plt.plot(df.Close, 'g')
st.pyplot(fig)






