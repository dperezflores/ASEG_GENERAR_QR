import streamlit as st
import qrcode
from io import BytesIO

# 1. Configuración de la página
st.set_page_config(page_title="Generador de QR - ASEG", page_icon="📱")

# 2. Inyección de CSS para centrado total y colores ASEG
estilo_css = """
<style>
    /* Fondo de la página */
    .stApp {
        background-color: #f4f4f9; 
    }
    
    /* Centrar textos generales y aplicar color Azul Marino */
    h1, h2, h3, p, label {
        color: #00304F !important; 
        text-align: center !important; 
    }

    /* --- AJUSTE DE CENTRADO PARA QR, CAPTION Y BOTÓN --- */
    /* Centra la imagen y el botón de descarga */
    [data-testid="stImage"], [data-testid="stDownloadButton"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* Centra específicamente el texto de la leyenda (caption) de la imagen */
    [data-testid="stImageCaption"] {
        text-align: center !important;
        width: 100%;
        display: block;
    }

    /* Estilo general de los botones */
    .stButton > button, .stDownloadButton > button {
        background-color: #FF5E12 !important; /* Naranja Intenso */
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
        display: block;
        margin: 0 auto; /* Centrado extra para el botón */
    }

    /* Forzar color BLANCO en el texto de los botones */
    .stButton > button p, .stDownloadButton > button p {
        color: white !important;
    }
    
    /* Efecto al pasar el mouse por el botón (Hover) */
    .stButton > button:hover, .stDownloadButton > button:hover {
        background-color: #57A0D4 !important; /* Azul Hover */
        color: white !important;
    }

    /* Estilo de la caja de texto */
    .stTextInput > div > div > input {
        background-color: #D6D6D6; 
        color: #362D32; 
        border: 2px solid #00304F;
        border-radius: 5px;
        text-align: center;
    }
</style>
"""
st.markdown(estilo_css, unsafe_allow_html=True)

# 3. Interfaz de usuario
st.title("Generador de Códigos QR Institucional")
st.write("Ingresa el enlace o texto que deseas convertir en un código QR:")

# Variable de entrada
texto_usuario = st.text_input("Enlace o texto:")

# 4. Centrado del botón de generar usando columnas
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    boton_generar = st.button("Generar QR", use_container_width=True)

# Lógica de generación
if boton_generar:
    if texto_usuario:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto_usuario)
        qr.make(fit=True)

        # QR Negro con fondo blanco
        img = qr.make_image(fill_color="black", back_color="white")

        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Mostrar imagen centrada con leyenda centrada
        st.image(byte_im, caption="Tu código QR generado")
        
        # Botón de descarga centrado
        st.download_button(
            label="Descargar QR",
            data=byte_im,
            file_name="codigo_qr_aseg.png",
            mime="image/png"
        )
    else:
        st.warning("Por favor, ingresa un texto o enlace primero.")
