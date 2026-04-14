import streamlit as st
from PIL import Image
import os
from detector import detect_people
from rules import evaluate_safety

st.set_page_config(page_title="AI Construction Safety Monitor", layout="wide")

st.title("🏗️ AI Construction Safety Monitor")
st.write("Şantiye güvenliği için yapay zeka destekli izleme paneli")

uploaded_file = st.file_uploader("Bir şantiye görseli yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    os.makedirs("sample_data", exist_ok=True)
    image_path = os.path.join("sample_data", uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    st.subheader("Yüklenen Görsel")
    st.image(image_path, caption="Orijinal Görsel", use_container_width=True)

    with st.spinner("Analiz yapılıyor..."):
        detection_result = detect_people(image_path)
        safety_result = evaluate_safety(detection_result["person_count"])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tespit Sonucu")
        st.image(detection_result["output_image"], caption="Algılama Çıktısı", use_container_width=True)

    with col2:
        st.subheader("Analiz Özeti")
        st.metric("Tespit Edilen Çalışan Sayısı", detection_result["person_count"])
        st.metric("Risk Seviyesi", safety_result["risk_level"])

        st.subheader("Uyarılar")
        for alert in safety_result["alerts"]:
            st.warning(alert)

    st.success("Analiz tamamlandı.")
else:
    st.info("Başlamak için bir görsel yükleyin.")