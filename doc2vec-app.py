import streamlit as st
from gensim.models.doc2vec import Doc2Vec
import pandas as pd
# Load the model
model = Doc2Vec.load("F:/Wiwid/Dataset/Doc2vec_model.model")
all_data = pd.read_csv('F:/Wiwid/Dataset/News Dataset Kompas.csv')
st.title('Doc2Vec Kompas 2015 News Data')

text = st.text_input('Enter Query Pencarian')
def similar_doc(text):
    inferred_vector = model.infer_vector(text.lower().split())
    similar_docs = model.dv.most_similar(positive = [inferred_vector], topn=10)
    return similar_docs
def similar_judul(similar_docs):
    idx = []
    for index, similarity in similar_docs:
        idx.append(index)
        similar_doc_judul = all_data["judul"][idx]
        similar_doc_judul = similar_doc_judul.reset_index()
        # similar_doc_judul['judul']
    return similar_doc_judul
def similar_isi(similar_docs):
    idx = []
    for index, similarity in similar_docs:
        idx.append(index)
        similar_doc_isi = all_data["isi"][idx]
        similar_doc_isi = similar_doc_isi.reset_index()
        # similar_doc_isi['isi']
    return similar_doc_isi

# Check if text input is not empty
if text:
    sim_doc = similar_doc(text)
    sim_judul = similar_judul(sim_doc)
    sim_isi = similar_isi(sim_doc)
    # st.dataframe(sim_doc)
    st.header('Judul Berita')
    st.dataframe(sim_judul)
    st.header('Isi Berita')
    st.table(sim_isi)