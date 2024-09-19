#use pickle rf.pkl to predict land value

import pickle
import streamlit as st
import pandas as pd

dtypes = {
    'Date mutation': 'str',
    'Valeur fonciere': 'float',
    'Code departement': 'str',
    'Type local': 'str',
    'Surface reelle bati': 'float',
    'Nombre pieces principales': 'Int64',
    'Surface terrain': 'float',
}

st.title('Land value prediction')

st.write('This app predicts the value of a land based on the following features:')
st.write('Transfer month, Department code, Type of premises, Built surface, Number of rooms, Land surface')

st.write('Please enter the following features:')

date = st.slider('Transfer month', 0, 12)
code_departement = st.selectbox('Department code', ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '971', '972', '973', '974', '976'])
type_local = st.select_slider('Type of premises', ['House', 'Apartment', 'Commercial premises'])
surface_reelle_bati = st.slider('Built surface', 0, 1000)
nombre_pieces_principales = st.slider('Number of rooms', 0, 10)
surface_terrain = st.slider('Land surface', 0, 1000)

features = [date, surface_reelle_bati, nombre_pieces_principales, surface_terrain, code_departement, type_local]
#to dataframe
df = pd.DataFrame([features], columns=['Date mutation', 'Surface reelle bati', 'Nombre pieces principales', 'Surface terrain', 'Code departement', 'Type local'])

#encode code_departement and type_local in one hot avec ces colonnes : ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '971', '972', '973', '974', '976']
#['House', 'Apartment', 'Commercial premises']

st.write(df.head())

model = pickle.load(open('rf.pkl', 'rb'))

prediction = model.predict(features)

st.write(f'The estimated value of the land is {prediction[0]} €')
