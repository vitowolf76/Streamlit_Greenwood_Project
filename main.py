import streamlit as st
import numpy as np
import pandas as pd
from dateutil.parser import parse
import datetime as dt
import matplotlib.pyplot as plt
import altair as alt
import plotly.graph_objs as go

# objective = Figure out how times each of the career values equals  essential , Very important , desirable and not import
# create an empty dictionary to store the percentages ( also can we creat a slider to show what age the student is and want they find important) exploration of values based on age and gender need to rework age  Y2K problem
# # # Display the dataframe as a table using Stream

DATA_URL_1 = ("/Users/vitowolf/PycharmProject/Streamlit_Greenwood_Project_2/all_data.csv")
DATA_URL_2= ("/Users/vitowolf/PycharmProject/Streamlit_Greenwood_Project_2/all_values .csv")
DATA_URL_3= ("/Users/vitowolf/PycharmProject/Streamlit_Greenwood_Project_2/little_value.csv")
#I added two csv files and I am using little_value/data3 to experiment with cleaning column names for eassier plotting

def load_data(nrows):
    data = pd.read_csv(DATA_URL_1, nrows=nrows)
    data2 = pd.read_csv(DATA_URL_2, nrows=nrows)
    data3 = pd.read_csv(DATA_URL_3, nrows=nrows)
    combined_data = pd.concat([data, data2, data3], axis=0)
    return combined_data

# this section of code was the original load to read all_data.csv
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL_1)
#     return data


st.markdown(
    f'<div style="text-align:center"><h1>GREENWOOD PROJECT</h1></div>',
    unsafe_allow_html=True
)
# The code block below is to add bar chart for all_data.csv only

# data = load_data(3000)
# print(data)
# st.write(data)
# # this section is creating the first charts using all_data.csv info
# x = data["Are_you_currently_a_student?"]
# st.write(x)
# y = data["State/Region"]
# st.write(y)
# z = data["City"]
# st.write(z)
# d = data["Date_of_Birth"]
# st.write(d)
#
# city = z.value_counts()
# st.bar_chart(city)
#
# counts = x.value_counts()
# st.bar_chart(counts)
#
# states = y.value_counts()
# st.bar_chart(states)
#
# d = pd.to_datetime(d, errors='coerce')
# age = (dt.datetime.now() - d) // dt.timedelta(days=365.2425)
# st.write(age)
#
# age = age.value_counts()
# st.bar_chart(age)
#
# data = load_data(3000)
# print(data)
# st.write(data)

age_range = st.slider('Select age range:', 10, 90, (20, 50))
gender = st.selectbox('Select gender:', ['Male', 'Female', 'Other'])

# Extract the data for the "Essential", "Very Important", "Desirable", and "Not Important" categories def load_data(nrows):


data = load_data(3000)
data3 = pd.read_csv(DATA_URL_3)



st.write(data3)



# # define the ordinal values you want to analyze
ordinal_values = ['Essential', 'Very Important', 'Desirable', 'Not Important']
data3 = data3.replace("Very important", "Very Important")
# define the columns you want to analyze
columns_to_analyze = ['Appearance', 'Assertiveness', 'Being_Someone_Special', 'Career', 'Control', 'Emotional_Stability', 'Family', 'Financial_Security', 'Friendships', 'Health', 'Independence', 'Intelligence', 'Love', 'Marriage', 'Personal_Recognition', 'Relationships', 'Spiritual_Life', 'Status', 'Success', 'Able_to_Make_a_Difference', 'Able_to_See_Results', 'Be_Own_Boss', 'Business_Location', 'Challenge', 'Competition_on_the_Job', 'Contribute_to_Society', 'Creativity', 'Excitement', 'Fast_Paced', 'Flexibility', 'Good_Benefits', 'Independence', 'Intellectual_Growth', 'Job_Security', 'Leadership', 'Manage_People', 'Outdoors', 'Personal_Leisure_Time', 'Power', 'Prestige', 'Promotion', 'Regular_Hours', 'Respect', 'Teamwork', 'Time_Alone', 'Time_for_Family', 'To_Be_Known', 'Travel', 'Variety', 'Wealth', 'Helping_People']
data3_no_missing = data3.dropna(subset=['Appearance'])
st.write(data3_no_missing)
# iterate over the columns and ordinal values, and calculate the percentages
percentages = {}
for column in columns_to_analyze:
    st.markdown(f'<div style="text-align:center"><h1>{column}</h1></div>', unsafe_allow_html=True)
    percentages[column] = {}
    for ordinal_value in ordinal_values:
        value_counts = data3_no_missing[column].value_counts()
        ordinal_frequency = value_counts[ordinal_value] if ordinal_value in value_counts else 0
        ordinal_percentage = (ordinal_frequency / len(data3_no_missing)) * 100
        percentages[column][ordinal_value] = ordinal_percentage
        st.write(f"The percentage of {ordinal_value} is: {ordinal_percentage:.2f}%")
    st.bar_chart(percentages[column])






    # Create a function to plot the pie chart
    def plot_pie_chart(percentages, column):
        fig, ax = plt.subplots()
        ax.pie(percentages, labels=percentages.keys(), colors=[colors[k] for k in percentages.keys()],
               autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title(column)
        return fig

    fig = go.Figure(data=[go.Pie(labels=ordinal_values, values=list(percentages[column].values()))])
    st.plotly_chart(fig)

#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#