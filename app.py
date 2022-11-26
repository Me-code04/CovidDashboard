from library import *
from add_bg_from_local import *
import streamlit as st

countries = ["India","USA","China","Sri Lanka","Japan"]
countries_code = ["in","us","cn","lk","jp"]
country = st.sidebar.selectbox("Select your country", countries)

index = 0
while country != countries[index]:
    index += 1
country_code = countries_code[index]

statistics = ["cases","deaths","recovered"]

#st.write("Your country is", country)
st.image(f"https://flagcdn.com/w160/{country_code}.png")
days = st.sidebar.slider("Pick the number of days", min_value = 1, max_value = 100)
s_stats = st.sidebar.multiselect("Select statistics", statistics)

hist_cases = get_historic_cases(country, days)
hist_deaths = get_historic_deaths(country, days)
hist_recoveries = get_historic_recoveries(country, days)

cases_df = pd.concat([hist_cases,hist_deaths,hist_recoveries], axis = 1).astype(int)

daily_cases = get_daily_cases(country, days)
daily_deaths = get_daily_deaths(country, days)
daily_recoveries = get_daily_recoveries(country, days)

daily_cases_df = pd.concat([daily_cases,daily_deaths,daily_recoveries], axis = 1).astype(int)

yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)

add_bg_from_local('covid19Virus.jpg')

st.metric("Country", country)

col1, col2, col3 = st.columns(3)

with col1:
   st.metric("Yesterday Cases", yesterday_cases)

with col2:
   st.metric("Yesterday Deaths", yesterday_deaths)

with col3:
   st.metric("Yesterday Recoveries", yesterday_recoveries)

st.header("Trends")

col4, col5 = st.columns(2)

with col4:
    st.line_chart(cases_df[s_stats])

with col5:
    st.line_chart(daily_cases_df[s_stats])

col6, col7 = st.columns(2)

with col6:
    st.write(cases_df)

with col7:
    st.write(daily_cases_df)

st.header("Here's a wonderful video to learn more about COVID-19!")
st.video("https://www.youtube.com/watch?v=BtN-goy9VOY")


