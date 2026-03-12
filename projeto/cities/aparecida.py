import streamlit as st

@st.cache_data  
# Após a execução uma vez, ele guarda um cache da função escrita abaixo dele, para que se a página for recarregada novamente, abra de forma mais rápida.
def pagina_aparecida():     # Definição daquilo que irá aparecer na página
     
     # Título principal (Apenas da página. Não a ligação com a aba do navegador )
    st.title("Aparecida")  
     
     # Estará escrito isso abaixo do título
    st.write("Esse é o Hub Aparecida, o qual você pode encontrar os melhores pontos da cidade de Aparecida de Goiânia") 
pagina_aparecida()