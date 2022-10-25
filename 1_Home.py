from re import L
from unicodedata import is_normalized
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import webbrowser

st.header('OUSC Season Offences Counter')

st.markdown("""Please enter the following information below:
### Offender Name
- Declan
- Owen
- Jackson
- Andrew
- Matty
- Felix
- Miles
- Max
- David
- Nick

### Offence
- Offside
- Yellow
- Red
""")

df = pd.read_csv('offence_log.csv')

name = st.text_input('Name of offender')
offence = st.text_input('Offence')
description = st.text_input('Please give detail as to the offence in question')

counter = 0

if st.button("Add Offence"):
    df = df.append({'Name':name,"Offence":offence,"Description":description},ignore_index=True)
    df.to_csv('offence_log.csv',index=False)



dec_off = 0
owen_off = 0
jackson_off = 0
andrew_off = 0
matty_off = 0
felix_off = 0
miles_off = 0
max_off = 0
david_off = 0
nick_off = 0

dec_yel = 0
owen_yel = 0
jackson_yel = 0
andrew_yel = 0
matty_yel = 0
felix_yel = 0
miles_yel = 0
max_yel = 0
david_yel = 0
nick_yel = 0

dec_red = 0
owen_red = 0
jackson_red = 0
andrew_red = 0
matty_red = 0
felix_red = 0
miles_red = 0
max_red = 0
david_red = 0
nick_red = 0

is_dec = df['Name'] =='Declan'
is_owen = df['Name'] == 'Owen'
is_jackson = df['Name'] == 'Jackson'
is_andrew = df['Name'] == 'Andrew'
is_matty = df['Name'] == 'Matty'
is_felix = df['Name'] == 'Felix'
is_miles = df['Name'] == 'Miles'
is_max = df['Name'] == 'Max'
is_david = df['Name'] == 'David'
is_nick = df['Name'] == 'Nick'


dec_offences = df[is_dec]
owen_offences = df[is_owen]
jackson_offences = df[is_jackson]
andrew_offences = df[is_andrew]
matty_offences = df[is_matty]
felix_offences = df[is_felix]
miles_offences = df[is_miles]
max_offences = df[is_max]
david_offences = df[is_david]
nick_offences = df[is_nick]



for offence in dec_offences['Offence'].tolist():
    if offence == 'Offside':
        dec_off += 1
    elif offence == 'Yellow':
        dec_yel += 1
    elif offence == 'Red':
        dec_red += 1

for offence in owen_offences['Offence'].tolist():
    if offence == 'Offside':
        owen_off += 1
    elif offence == 'Yellow':
        owen_yel += 1
    elif offence == 'Red':
        owen_red += 1

for offence in jackson_offences['Offence'].tolist():
    if offence == 'Offside':
        jackson_off += 1
    elif offence == 'Yellow':
        jackson_yel += 1
    elif offence == 'Red':
        jackson_red += 1

for offence in andrew_offences['Offence'].tolist():
    if offence == 'Offside':
        andrew_off += 1
    elif offence == 'Yellow':
        andrew_yel += 1
    elif offence == 'Red':
        andrew_red += 1

for offence in matty_offences['Offence'].tolist():
    if offence == 'Offside':
        matty_off += 1
    elif offence == 'Yellow':
        matty_yel += 1
    elif offence == 'Red':
        matty_red += 1

for offence in felix_offences['Offence'].tolist():
    if offence == 'Offside':
        felix_off += 1
    elif offence == 'Yellow':
        felix_yel += 1
    elif offence == 'Red':
        felix_red += 1

for offence in miles_offences['Offence'].tolist():
    if offence == 'Offside':
        miles_off += 1
    elif offence == 'Yellow':
        miles_yel += 1
    elif offence == 'Red':
        miles_red += 1

for offence in max_offences['Offence'].tolist():
    if offence == 'Offside':
        max_off += 1
    elif offence == 'Yellow':
        max_yel += 1
    elif offence == 'Red':
        max_red += 1

for offence in david_offences['Offence'].tolist():
    if offence == 'Offside':
        david_off += 1
    elif offence == 'Yellow':
        david_yel += 1
    elif offence == 'Red':
        david_red += 1

for offence in nick_offences['Offence'].tolist():
    if offence == 'Offside':
        nick_off += 1
    elif offence == 'Yellow':
        nick_yel += 1
    elif offence == 'Red':
        nick_red += 1


offences_data = pd.DataFrame({
    'Offsides':[dec_off,owen_off,jackson_off,andrew_off,matty_off,felix_off,miles_off,max_off,david_off,nick_off],
    'Yellow_Cards':[dec_yel,owen_yel,jackson_yel,andrew_yel,matty_yel,felix_yel,miles_yel,max_yel,david_yel,nick_yel],
    'Red_Cards':[dec_red,owen_red,jackson_red,andrew_red,matty_red,felix_red,miles_red,max_red,david_red,nick_red]},
    index=['Declan','Owen','Jackson','Andrew','Matty','Felix','Miles','Max U','David','Nick L'])

offences_data.sort_values(by=['Red_Cards','Yellow_Cards','Offsides'], inplace=True, ascending=False)


st.subheader('Offence Table')
st.write(offences_data)



st.subheader('Offence Log')
st.write(df)

def plot_bar(title,col,y_label):
    fig = go.Figure([go.Bar(x=offences_data['Name'], y=offences_data[col])])
    fig.update_layout(
    title={
    'text': title,
    'y':0.9,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'},
    xaxis_title= 'Member',
    yaxis_title= y_label,
    template='simple_white')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Show offsides'):
    try:
        plot_bar('Offsides','Offsides','Offsides')
    except:
        st.text('Error or no offside data to display')

  
if st.checkbox('Show yellow cards'):
    try:
        plot_bar('Yellow Cards','Yellow_Cards','Yellow Cards')
    except:
        st.text('Error or no yellow cards to display')

if st.checkbox('Show red cards'):
    try:
        plot_bar('Red Cards','Red_Cards','Red Cards')
    except:
        st.text('Error or no red cards to display')