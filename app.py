
import streamlit as st
import pandas as pd

# Título e descrição
st.title("Gerador de Orçamentos com Curadoria de Produtos + Imagem")
st.markdown("Faça o upload de uma imagem ou descreva o ambiente. O sistema sugerirá produtos adequados do catálogo.")

# Carregar catálogo com imagens
catalogo = pd.read_excel("catalogo_imagens_reais.xlsx")

# Upload de imagem de referência
imagem_cliente = st.file_uploader("📸 Envie uma imagem de referência do ambiente (opcional)", type=["jpg", "jpeg", "png"])

# Entrada de descrição
descricao = st.text_area("📝 Descreva o ambiente ou o que o cliente busca:")
categoria = st.selectbox("📂 Selecione uma categoria de produto:", catalogo['Categoria'].unique())
gerar = st.button("Gerar orçamento")

# Lógica de seleção e exibição
if gerar and descricao:
    st.subheader("🛋️ Produto Sugerido:")
    produto = catalogo[catalogo['Categoria'] == categoria].sample(1).iloc[0]
    
    st.image(produto['Imagem'], width=300)
    st.markdown(f"**Nome:** {produto['Nome']}")
    st.markdown(f"**Descrição:** {produto['Descrição']}")
    st.markdown(f"**Preço:** R$ {produto['Preço (R$)']:.2f}")
    st.markdown(f"**Fornecedor:** {produto['Fornecedor']}")

    st.success("✅ Orçamento gerado com sucesso!")
    
    if imagem_cliente:
        st.markdown("---")
        st.markdown("🔍 **Imagem enviada como referência:**")
        st.image(imagem_cliente, width=250)

# Rodapé
st.markdown("---")
st.caption("Protótipo por Rafael Ferrer – IA para vendas e automação inteligente")
