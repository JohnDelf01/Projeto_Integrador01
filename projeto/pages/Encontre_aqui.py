import streamlit as st
from cities.goiania import pagina_goiania
from cities.aparecida import pagina_aparecida
from cities.canedo import pagina_canedo

# Foi selecionado Ícone, Nome, e status de toda a página. O ícone e o título ficam na aba de navegação do Chrome, Microsoft Edge, entre outros.
st.set_page_config(
    page_title = "Sua Cidade",
    page_icon = ":beer:",
    initial_sidebar_state="expanded"
)
st.sidebar.title("Menu")

pgs = {
    # dicionário python. Lado esquerdo são as keys/entradas | Lado direito são os valores, que, no caso, são as funções definidas anteriormente. Serve para definir o que as entradas vão receber.
    "Goiânia": pagina_goiania,  
    "Aparecida": pagina_aparecida,
    "Senador Canedo": pagina_canedo
}

# st.sidebar --> Cria uma sidebar na página 
# No caso a função ".selectbox" vai criar uma caixa de selecionáveis. Neste caso ele cria essa caixa com base na listagem das entradas do dícionario "pgs = páginas"
# pgs.keys --> puxa quais são as entradas que o dicionário tem, apenas elas, sem seus valores
selecao = st.sidebar.selectbox("Selecione uma cidade:", list(pgs.keys()))

# pgs_selected = páginas selecionadas
#tem a função de guardar o valor que foi selecionado na selectbox e logo em seguida executá-lo, dessa forma, cria uma página nova, 
#com as informações contidas nas funções antes escritas, as quais são executadas através da seleção das keys do dicionário
pgs_selected = pgs[selecao]
pgs_selected()
