import streamlit as st

def education_page():
    st.title("Education")
    with st.container(border=True):
        st.write(
            """
            **EFREI Paris** | 2021-2026
            - École d'ingénieur informatique en 5 ans. Actuellement en deuxième année de cycle ingénieur (M1).
            - Cours suivis: Advanced databases, Data visualization, Machine learning, API and web services, and Maths for data scientists
            """
        )
    with st.container(border=True):
        st.write(
            """
            **APU Kuala Lumpur** | 2023
            - Semestre d’étude en Malaisie
            - Cours suivis: Advanced web programming, Java programming, Object-oriented Analysis and Design with UML
            """
        )
    with st.container(border=True):
        st.write(
            """
            **Saint-Jean Hulst** | 2006-2021
            - Bac spécialité NSI/Physique avec mention Bien
            """
        )
    

education_page()