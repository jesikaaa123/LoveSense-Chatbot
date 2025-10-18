import streamlit as st
import google.generativeai as genai

# Konfigurasi API Key Gemini
genai.configure(api_key="AIzaSyBboni1ytwrArXqmPt9TMIJ1lYiOq7AUEo")

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="LoveSense 💘", page_icon="💞", layout="centered")
st.title("💘 LoveSense – Chatbot Analisis Tipe Jodoh")

st.write("Hai! Aku *LoveSense*, AI yang bisa bantu kamu tahu tipe jodoh ideal 💞")
st.write("Coba tanya sesuatu seperti:")
st.write("- Aku orangnya cuek, cocoknya sama tipe apa ya?")
st.write("- Kalau aku Libra, cocoknya sama siapa?")
st.write("---")

# Input pengguna
pesan = st.text_input("Tulis pertanyaanmu di sini:")

# Proses chatbot
if pesan:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        jawaban = model.generate_content(
            f"Kamu adalah LoveSense, chatbot cinta. Jawablah dengan gaya santai dan romantis. Pertanyaan pengguna: {pesan}"
        )
        st.success(jawaban.text)
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")