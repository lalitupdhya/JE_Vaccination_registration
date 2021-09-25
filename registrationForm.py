import streamlit as st
import pandas as pd
import datetime as dt


st.title('JE vaccination Drive Biswanath District.')

df = pd.read_excel('BiswanathHealthFacilities.xlsx')

bphc = list(df.Health_Block.unique())
option1 = st.selectbox(
    'Enter the BPHC',
    bphc
)

insName = list(df[df.Health_Block==option1].Facility_Name.unique())
option2 = st.selectbox(
        'Enter the Health Institution Name',
        insName
    )
try:
    df_final = pd.read_excel('newEntries.xlsx')
except:
    df_final = pd.DataFrame()
with st.form(key="form1", clear_on_submit = True):
    name = st.text_input(label = "Enter name of the person")
    age = st.text_input(label = "Enter age of the person")
    sex = st.text_input(label = "Enter sex of the person")
    address = st.text_input(label = "Enter address of the person")
    mob = st.text_input(label = "Enter phone no of the person")
    submit = st.form_submit_button(label = "Submit")
    if submit:
        entry = {
            "date":[dt.datetime.now()],
            "name":[name],
            "age" : [age],
            "sex":[sex],
            "Address":[address],
            "MobileNo":[mob],
            "BPHC": option1,
            "Facility_Name": option2
        }
        temp = pd.DataFrame(entry)
        df_final = pd.concat([df_final,temp])
        df_final.to_excel('newEntries.xlsx', index=False)
        st.write(f'{name} is registered successfully !')