import streamlit as st
from feedback.feedback_store import save_feedback, load_feedback


st.title('CrewAI Feedback')

new_feedback = st.text_input('Nuevo feedback:')
if st.button('Guardar'):
    if new_feedback:
        save_feedback({'feedback': new_feedback})
        st.success('Guardado')

st.subheader('Historial')
for entry in load_feedback():
    st.write(entry)
