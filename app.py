import streamlit as st
from predictor import predict_class
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.image('header.png')
placeholder = st.empty()
with placeholder.form("Input"):
    st.markdown("Parkinson's Disease Detection")
    x00 = st.number_input(label='Enter MDVP Fo(Hz):',step=1.,format='%.4f')
    x01 = st.number_input(label='Enter MDVP Fhi(Hz):',step=1.,format='%.4f')
    x02 = st.number_input(label='Enter MDVP Flo(Hz):',step=1.,format='%.4f')
    x03 = st.number_input(label='Enter MDVP Jitter(%):',step=1.,format='%.4f')
    x04 = st.number_input(label='Enter MDVP Jitter(Abs):',step=1.,format='%.4f')
    x05 = st.number_input(label='Enter MDVP RAP:',step=1.,format='%.4f')
    x06 = st.number_input(label='Enter MDVP PPQ:',step=1.,format='%.4f')
    x07 = st.number_input(label='Enter Jitter DDP:',step=1.,format='%.4f')
    x08 = st.number_input(label='Enter MDVP Shimmer:',step=1.,format='%.4f')
    x09 = st.number_input(label='Enter MDVP Shimmer(dB):',step=1.,format='%.4f')
    x10 = st.number_input(label='Enter Shimmer APQ3:',step=1.,format='%.4f')
    x11 = st.number_input(label='Enter Shimmer APQ5:',step=1.,format='%.4f')
    x12 = st.number_input(label='Enter MDVP:APQ ',step=1.,format='%.4f')
    x13 = st.number_input(label='Enter Shimmer DDA:',step=1.,format='%.4f')
    x14 = st.number_input(label='Enter NHR :',step=1.,format='%.4f')
    x15 = st.number_input(label='Enter HNR :',step=1.,format='%.4f')
    x16 = st.number_input(label='Enter RPDE :',step=1.,format='%.4f')
    x17 = st.number_input(label='Enter DFA :',step=1.,format='%.4f')
    x18 = st.number_input(label='Enter spread1 :',step=1.,format='%.4f')
    x19 = st.number_input(label='Enter spread2 :',step=1.,format='%.4f')
    x20 = st.number_input(label='Enter D2 :',step=1.,format='%.4f')
    x21 = st.number_input(label='Enter PPE :',step=1.,format='%.4f')
    values_list = [x00,x01,x02,x03,x04,x05,x06,x07,x08,x09,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21]
    submit =  st.form_submit_button("submit")

if submit and None not in values_list:
    input_data = values_list
    st.markdown(f"### {predict_class(input_data)}")
else:
    st.markdown("Test entries are empty or contain incorrect values")

st.image('footer.png')
# badhri
