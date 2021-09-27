import streamlit as st
import pandas as pd
import datetime as dt
import pytz


IST = pytz.timezone('Asia/Kolkata')

st.title('JE vaccination Drive Biswanath District.')

if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv('BiswanathHealthFacilities.csv')

bphc = list(st.session_state.df.Health_Block.unique())
option1 = st.selectbox(
    'Enter the BPHC',
    bphc
    )
insName = list(st.session_state.df[st.session_state.df.Health_Block==option1].Facility_Name.unique())
option2 = st.selectbox(
    'Enter the Health Institution Name',
    insName
    )


if 'df_final' not in st.session_state:
    st.session_state.df_final = pd.DataFrame()

with st.form(key="form1", clear_on_submit = True):
    name = st.text_input(label = "Enter name of the person")
    # age = st.selectbox("Enter age of the person", [k for k in range(120)])
    age = st.number_input("Enter Age", min_value=0, max_value=120)
    sex = st.selectbox("Enter sex of the person", ['Female','Male','Other'])
    address = st.text_input(label = "Enter address of the person")
    mob = st.number_input("Enter phone no of the person", min_value=6000000000, max_value=9999999999)
    submit = st.form_submit_button(label = "Submit")
    if submit:
        entry = {
            "date":[dt.datetime.now(IST).strftime('%Y:%m:%d %H:%M:%S')],
            "name":[name],
            "age" : [age],
            "sex":[sex],
            "Address":[address],
            "MobileNo":[mob],
            "BPHC": option1,
            "Facility_Name": option2
        }
        temp = pd.DataFrame(entry)
        st.session_state.df_final = pd.concat([st.session_state.df_final,temp])
        st.write(f'{name} is registered successfully !')


st.download_button('Download File', data=st.session_state.df_final.to_csv(index=False), mime='text/csv')