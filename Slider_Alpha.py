


###############test run 4 now add the values as compared to Male, Female, Non Gender, age and student status



import streamlit as st
import pandas as pd
import altair as alt
import datetime as dt
import matplotlib.pyplot as plt


ALL_DATA_URL = "./slider_bar_alpha.csv"

def load_all_data(nrows):
    data = pd.read_csv(ALL_DATA_URL, nrows=nrows)
    return data

all_data = load_all_data(100000)
st.markdown(
    f'<div style="text-align:center"><h1>GREENWOOD PROJECT</h1></div>',
    unsafe_allow_html=True)

st.markdown(
    f'<div style="text-align:center"><h1></h1></div>',
    unsafe_allow_html=True)
# Convert the date of birth to a datetime object
all_data["Date_of_Birth"] = pd.to_datetime(all_data["Date_of_Birth"], errors="coerce")

# Calculate the age based on the date of birth
all_data["Age"] = (dt.datetime.now() - all_data["Date_of_Birth"]) // dt.timedelta(days=365.2425)

# Create a slider for selecting the age range



# Filter the data based on the selected age range
min_age = int(all_data["Age"].min())
max_age = int(all_data["Age"].max())
age_range = st.slider("Select an age range", min_age, max_age, (min_age, max_age),key=f"first_slider")
filtered_data = all_data[all_data["Age"].between(age_range[0], age_range[1])]

# Filter data based on selected gender and age range
gender = st.selectbox("Select a gender", ["Male", "Female", "Gender non-conforming"])
filtered_data = filtered_data[filtered_data["To_which_gender_do_you_identify?"] == gender]


filtered_data = filtered_data[
    (filtered_data["Age"] >= age_range[0]) & (filtered_data["Age"] <= age_range[1])
]

# Compute value counts of "Are you currently a student?" for the filtered data
status_counts = filtered_data["Are_you_currently_a_student?"].value_counts().reset_index()
status_counts.columns = ["status", "count"]

# Create a pie chart of the filtered data
chart = alt.Chart(status_counts).mark_bar().encode(
    x="status",
    y="count",
    color="status"
)
st.write(f"Student Status Counts (age {age_range[0]}-{age_range[1]})")
st.altair_chart(chart, use_container_width=True)

# define the ordinal values you want to analyze

def load_all_data(nrows):
    data = pd.read_csv(ALL_DATA_URL, nrows=nrows)

    def load_all_data(nrows):
        data = pd.read_csv(ALL_DATA_URL, nrows=nrows)
        return data

    all_data = load_all_data(100000)


ordinal_values = ['Essential', 'Very Important', 'Desirable', 'Not Important']
data = all_data.replace("Very important", "Very Important")
# define the columns you want to analyze
columns_to_analyze = ['Appearance', 'Assertiveness', 'Being_Someone_Special', 'Career', 'Control', 'Emotional_Stability', 'Family', 'Financial_Security', 'Friendships', 'Health', 'Independence', 'Intelligence', 'Love', 'Marriage', 'Personal_Recognition', 'Relationships', 'Spiritual_Life', 'Status', 'Success', 'Able_to_Make_a_Difference', 'Able_to_See_Results', 'Be_Own_Boss', 'Business_Location', 'Challenge', 'Competition_on_the_Job', 'Contribute_to_Society', 'Creativity', 'Excitement', 'Fast_Paced', 'Flexibility', 'Good_Benefits', 'Intellectual_Growth', 'Job_Security', 'Leadership', 'Manage_People', 'Outdoors', 'Personal_Leisure_Time', 'Power', 'Prestige', 'Promotion', 'Regular_Hours', 'Respect', 'Teamwork', 'Time_Alone', 'Time_for_Family', 'To_Be_Known', 'Travel', 'Variety', 'Wealth', 'Helping_People']
# all_data_no_missing = all_data.dropna(subset=['Appearance'])
# st.write(all_data_no_missing)
# iterate over the columns and ordinal values, and calculate the percentages
percentages = {}
for column in columns_to_analyze:
    column_name = column.replace("_"," ")
    st.markdown(f'<div style="text-align:center"><h1>{column_name}</h1></div>', unsafe_allow_html=True)
    percentages[column] = {}
    gender = st.selectbox("Select a gender", ["Male", "Female", "Gender non-conforming"], key=f"gender_checkbox_{column}")
    min_age = int(all_data["Age"].min())
    max_age = int(all_data["Age"].max())
    age_range = st.slider("Select an age range", min_age, max_age, (min_age, max_age),key=f"slider_age_{column}")
    for ordinal_value in ordinal_values:
        filtered_data = data[data["Age"].between(age_range[0], age_range[1])]
        filtered_data = filtered_data[filtered_data["To_which_gender_do_you_identify?"] == gender]
        value_counts = filtered_data[column].value_counts()
        ordinal_frequency = value_counts[ordinal_value] if ordinal_value in value_counts else 0
        ordinal_percentage = (ordinal_frequency / len(filtered_data)) * 100
        percentages[column][ordinal_value] = ordinal_percentage
        st.write(f"The percentage of {ordinal_value} is: {ordinal_percentage:.2f}%")
    st.bar_chart(percentages[column])






