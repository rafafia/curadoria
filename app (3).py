
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Título e descrição
st.title("Gerador de Orçamentos com Curadoria Multicategoria (Top 3 Resultados)")
st.markdown("Descreva o ambiente ou estilo desejado e selecione múltiplas categorias. O sistema retornará os produtos mais compatíveis com base nas descrições visuais.")

# Carregar o catálogo aprimorado
catalogo = pd.read_excel("catalogo_detalhado_aprimorado.xlsx")

# Upload da imagem (opcional)
imagem_cliente = st.file_uploader("📸 Envie uma imagem de referência do ambiente (opcional)", type=["jpg", "jpeg", "png"])

# Entrada do usuário
descricao_cliente = st.text_area("📝 Descreva o ambiente, estilo ou o que o cliente busca:")

# Seleção de múltiplas categorias
categorias = st.multiselect("📂 Selecione as categorias desejadas:", catalogo['Categoria'].unique())
gerar = st.button("Gerar orçamento")

# Lógica de curadoria com múltiplas categorias e retorno dos top 3 produtos
if gerar and descricao_cliente and categorias:
    st.subheader("🛋️ Produtos Sugeridos (Top 3 mais compatíveis)")
    
    produtos_selecionados = catalogo[catalogo['Categoria'].isin(categorias)].reset_index(drop=True)
    corpus = [descricao_cliente] + produtos_selecionados['Descrição Visual'].tolist()
    tfidf = TfidfVectorizer().fit_transform(corpus)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    # Obter os índices dos top 3 produtos mais similares
    top_indices = similarity.argsort()[-3:][::-1]

    for idx in top_indices:
        produto = produtos_selecionados.iloc[idx]
        st.image(produto['Imagem'], width=300)
        st.markdown(f"**Nome:** {produto['Nome']}")
        st.markdown(f"**Categoria:** {produto['Categoria']}")
        st.markdown(f"**Descrição Técnica:** {produto['Descrição Técnica']}")
        st.markdown(f"**Descrição Visual:** {produto['Descrição Visual']}")
        st.markdown(f"**Preço:** R$ {produto['Preço (R$)']:.2f}")
        st.markdown(f"**Fornecedor:** {produto['Fornecedor']}")
        st.markdown("---")

    st.success("✅ Orçamento com múltiplos produtos sugeridos com base na sua descrição.")

    if imagem_cliente:
        st.markdown("🔍 **Imagem enviada como referência:**")
        st.image(imagem_cliente, width=250)

# Rodapé
st.markdown("---")
st.caption("Protótipo por Rafael Ferrer – Curadoria IA Multicategoria para Vendas Consultivas")
