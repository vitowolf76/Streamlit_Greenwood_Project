# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import datetime as dt



# ALL_DATA_URL = (
#     "/Users/vitowolf/PycharmProject/Streamlit_Greenwood_Project_2/slider_bar_alpha.csv"
# )
#
#
#
# def load_all_data(nrows):
#     data = pd.read_csv(ALL_DATA_URL)
#     return data
#
# # data = load_data(100000)
#
# all_data = load_all_data(100000)
# st.write(all_data)
#
# # Sample data
# x = all_data["Are_you_currently_a_student?"]
# state = all_data["State/Region"]
# st.write(x)
#
# counts = x.value_counts()
# st.bar_chart(counts)
#
# state_count = state.value_counts()
# st.bar_chart(state_count)
#
# # data['Date_of_Birth'] = pd.to_datetime(data['Date_of_Birth'])
# dob = all_data['Date_of_Birth']
#
# dob = pd.to_datetime(dob, errors='coerce')
# st.write(dob)
#
# all_data['Age'] = (dt.datetime.now() - pd.to_datetime(all_data['Date_of_Birth'], errors='coerce')) // dt.timedelta(days=365.2425)
# st.write(all_data)
#
# # age = age.value_counts()
# # st.bar_chart(age)
#
# # Create slider for filtering
# min_age = int(all_data['Age'].min())
# max_age = int(all_data['Age'].max())
# age_range = st.slider('Select a year', min_age, max_age, (min_age, max_age))
#
# # Filter data based on selected year
# filtered_df = all_data[all_data['Age'].between(age_range[0], age_range[1])]
#
#
# # Display filtered data
# st.write(filtered_df)
#
#
# if st.checkbox("Show Raw Data", False):
#     st.subheader('Raw Data')
#     st.write(data)


################### test run1 trying pie chart

# import streamlit as st
# import pandas as pd
# import altair as alt
# import datetime as dt
#
# ALL_DATA_URL = "/Users/vitowolf/PycharmProject/Streamlit_Greenwood_Project_2/slider_bar_alpha.csv"
#
# def load_all_data(nrows):
#     data = pd.read_csv(ALL_DATA_URL)
#     return data
#
# all_data = load_all_data(100000)
#
# # Display the data
# st.write(all_data)
#
# # Convert the date of birth to a datetime object
# all_data["Date_of_Birth"] = pd.to_datetime(all_data["Date_of_Birth"], errors="coerce")
#
# # Calculate the age based on the date of birth
# all_data["Age"] = (dt.datetime.now() - all_data["Date_of_Birth"]) // dt.timedelta(days=365.2425)
#
# # Create a slider for selecting the age range
# min_age = int(all_data["Age"].min())
# max_age = int(all_data["Age"].max())
# age_range = st.slider("Select an age range", min_age, max_age, (min_age, max_age))
#
# # Filter the data based on the selected age range
# filtered_data = all_data[all_data["Age"].between(age_range[0], age_range[1])]
#
# # Create a pie chart of the filtered data
# status_counts = filtered_data["Are_you_currently_a_student?"].value_counts().reset_index()
# status_counts.columns = ["status", "count"]
# chart = alt.Chart(status_counts).mark_bar().encode(
#     x="status",
#     y="count",
#     color="status"
# )
# st.write(f"Student Status Counts (age {age_range[0]}-{age_range[1]})")
# st.altair_chart(chart, use_container_width=True)



#################### test run 2 with gender added

# import streamlit as st
# import pandas as pd
# import altair as alt
# import datetime as dt
#
# ALL_DATA_URL = "/Users/vitowolf/PycharmProject/Streamlit_Greenwood_Project_2/slider_bar_alpha.csv"
#
# def load_all_data(nrows):
#     data = pd.read_csv(ALL_DATA_URL)
#     return data
# #
#
# def load_all_data(nrows):
#     data = pd.read_csv(ALL_DATA_URL, nrows=nrows)
#     return data
#
# all_data = load_all_data(100000)
#
# # Display the data
# st.write(all_data)
#
# # Convert the date of birth to a datetime object
# all_data["Date_of_Birth"] = pd.to_datetime(all_data["Date_of_Birth"], errors="coerce")
#
# # Calculate the age based on the date of birth
# all_data["Age"] = (dt.datetime.now() - all_data["Date_of_Birth"]) // dt.timedelta(days=365.2425)
#
# # Create a slider for selecting the age range
# min_age = int(all_data["Age"].min())
# max_age = int(all_data["Age"].max())
# age_range = st.slider("Select an age range", min_age, max_age, (min_age, max_age))
#
# # Filter the data based on the selected age range
# filtered_data = all_data[all_data["Age"].between(age_range[0], age_range[1])]
#
# # Create a pie chart of the filtered data
# status_counts = filtered_data["Are_you_currently_a_student?"].value_counts().reset_index()
# status_counts.columns = ["status", "count"]
# chart = alt.Chart(status_counts).mark_bar().encode(
#     x="status",
#     y="count",
#     color="status"
# )
# st.write(f"Student Status Counts (age {age_range[0]}-{age_range[1]})")
# st.altair_chart(chart, use_container_width=True)
#
#
# # Filter data based on selected gender
# gender = st.selectbox("Select a gender", ["Male", "Female", "Gender non-conforming"])
# filtered_data = all_data[all_data["To_which_gender_do_you_identify?"] == gender]
#
#
# # Display charts for each gender
# if gender == "Male":
#     gender_counts = filtered_data["To_which_gender_do_you_identify?"].value_counts()
#     st.bar_chart(gender_counts)
#
# elif gender == "Female":
#     gender_counts = filtered_data["To_which_gender_do_you_identify?"].value_counts()
#     st.bar_chart(gender_counts)
#
# else:
#     gender_counts = filtered_data["To_which_gender_do_you_identify?"].value_counts()
#     st.bar_chart(gender_counts)
#
# # Display filtered data
# if st.checkbox("Show filtered data", False):
#     st.subheader("Filtered data")
#     st.write(filtered_data)





########## test run 3 with gender and age on slider to change bar chart

# import streamlit as st
# import pandas as pd
# import altair as alt
# import datetime as dt
#
# ALL_DATA_URL = "/Users/vitowolf/PycharmProject/Streamlit_Greenwood_Project_2/slider_bar_alpha.csv"
#
# def load_all_data(nrows):
#     data = pd.read_csv(ALL_DATA_URL)
#     return data
# #
#
# def load_all_data(nrows):
#     data = pd.read_csv(ALL_DATA_URL, nrows=nrows)
#     return data
#
# all_data = load_all_data(100000)
#
# # Display the data
# st.write(all_data)
#
# # Convert the date of birth to a datetime object
# all_data["Date_of_Birth"] = pd.to_datetime(all_data["Date_of_Birth"], errors="coerce")
#
# # Calculate the age based on the date of birth
# all_data["Age"] = (dt.datetime.now() - all_data["Date_of_Birth"]) // dt.timedelta(days=365.2425)
#
# # Create a slider for selecting the age range
# min_age = int(all_data["Age"].min())
# max_age = int(all_data["Age"].max())
# age_range = st.slider("Select an age range", min_age, max_age, (min_age, max_age))
#
# # Filter the data based on the selected age range
# filtered_data = all_data[all_data["Age"].between(age_range[0], age_range[1])]
#
# # Create a pie chart of the filtered data
# status_counts = filtered_data["Are_you_currently_a_student?"].value_counts().reset_index()
# status_counts.columns = ["status", "count"]
# chart = alt.Chart(status_counts).mark_bar().encode(
#     x="status",
#     y="count",
#     color="status"
# )
# st.write(f"Student Status Counts (age {age_range[0]}-{age_range[1]})")
# st.altair_chart(chart, use_container_width=True)
#
#
# # Filter data based on selected gender and age range
# gender = st.selectbox("Select a gender", ["Male", "Female", "Gender non-conforming"])
# filtered_data = all_data[all_data["To_which_gender_do_you_identify?"] == gender]
#
# min_age = int(filtered_data["Age"].min())
# max_age = int(filtered_data["Age"].max())
# age_range = st.slider("Select an age range", min_age, max_age, (min_age, max_age))
#
# filtered_data = filtered_data[
#     (filtered_data["Age"] >= age_range[0]) & (filtered_data["Age"] <= age_range[1])
# ]
#
# # Compute value counts of "Are you currently a student?" for the filtered data
# status_counts = filtered_data["Are_you_currently_a_student?"].value_counts()
#
# # Display charts for each gender
# if gender == "Male":
#     st.subheader("Male")
#     st.bar_chart(status_counts)
#
# elif gender == "Female":
#     st.subheader("Female")
#     st.bar_chart(status_counts)
#
# else:
#     st.subheader("Gender non-conforming")
#     st.bar_chart(status_counts)
#
# # Display filtered data
# if st.checkbox("Show filtered data", False):
#     st.subheader("Filtered data")
#     st.write(filtered_data)

# filtered_data = filtered_data.replace("Very important", "Very Important")
# status_counts = filtered_data["Appearance"].value_counts().reset_index()
# status_counts.columns = ["status", "count"]
# new_names = ["Essential", "Very Important", "Desirable", "Not Important"]
# status_counts["status"] = pd.Categorical(status_counts["status"], categories=new_names, ordered=True)
# status_counts = status_counts.sort_values("status")
# chart = alt.Chart(status_counts).mark_bar().encode(
#     x=alt.X("status", title=None),
#     y=alt.Y("count", title="Count"),
#     color=alt.Color("status", title="Appearance")
# ).properties(
#     width=alt.Step(80)
# )
# min_age = int(all_data["Age"].min())
# max_age = int(all_data["Age"].max())
# age_range = st.slider("Select an age range", min_age, max_age, (min_age, max_age))
# # Filter the data based on the selected age range
# filtered_data = all_data[all_data["Age"].between(age_range[0], age_range[1])]
# st.altair_chart(chart, use_container_width=True)


# # Create a function to plot the pie chart
# def plot_pie_chart(percentages, column):
#     fig, ax = plt.subplots()
#     ax.pie(percentages, labels=percentages.keys(), colors=[colors[k] for k in percentages.keys()],
#            autopct='%1.1f%%', startangle=90)
#     ax.axis('equal')
#     ax.set_title(column)
#     return fig