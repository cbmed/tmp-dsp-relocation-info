import streamlit as st
from PIL import Image

im = Image.open('images/favicon.png')
st.set_page_config(page_title="CBmed Drug Screening - sample submission system", page_icon=im)  # layout="wide"

st.title("This page has moved! :truck:")
st.markdown("This page has moved to CBmed servers on 2023-05-15. You can now access it at https://photon.cbmed.at/drug-screening-sample-submission/ (all access credentials remain the same).")
st.markdown("You will also be notified of this change via email soon.")
st.markdown("If you have questions, please contact us at :email: samples@cbmed.at or it-support@cbmed.at or by calling us at :telephone_receiver: +43 316 385 288-04")
st.markdown("Best, your CBmed IT-Team!")
st.image('./images/cbmed_logo_2022.png', width=100)
