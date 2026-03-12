import streamlit as st

@st.cache_data
def pagina_goiania():
   st.title("Goiânia")
   st.write("Maior cidade do Estado de Goiás. Encontre aqui os melhores pontos de Goiânia")    

pagina_goiania()