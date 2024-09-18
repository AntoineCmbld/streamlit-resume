import streamlit as st

import streamlit.components.v1 as components


nav =st.navigation({"": [st.Page('home.py', title='Home', icon=':material/home:'),
                    st.Page('about.py', title='About', icon=':material/face:'),
                    st.Page('education.py', title='Education', icon=':material/school:')
                    ],
                    "Projects": [
                    st.Page('land_value.py', title='Land value', icon=':material/developer_board:')
                    ]})

with st.sidebar:
        components.iframe('https://lottie.host/embed/11baf9d0-2f09-4940-8fc4-8545070fae47/PlZnidWzAu.json')
        #navbar
        st.write("--------/!\\\-------Work in progress-------/!\\\--------")
nav.run()