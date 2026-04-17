import streamlit as st
import qrcode
from io import BytesIO

# 1. Configuración de la página
st.set_page_config(page_title="Generador de QR - ASEG", page_icon="📱")

# 2. Inyección de CSS para los colores institucionales de ASEG
estilo_css = """
<style>
    /* Fondo de la página */
    .stApp {
        background-color: #f4f4f9; 
    }
    
    /* Color de los textos generales y títulos */
    h1, h2, h3, p, label {
        color: #00304F !important; /* Azul Marino */
    }

    /* Estilo del botón */
    .stButton > button {
        background-color: #FF5E12 !important; /* Naranja Intenso */
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    /* Efecto al pasar el mouse por el botón (Hover) */
    .stButton > button:hover {
        background-color: #57A0D4 !important; /* Azul Hover */
        color: white !important;
        border-color: #00304F !important;
    }

    /* Estilo de la caja de texto */
    .stTextInput > div > div > input {
        background-color: #D6D6D6; /* Gris Claro de fondo */
        color: #362D32; /* Gris Oscuro para texto */
        border: 2px solid #00304F;
        border-radius: 5px;
    }
</style>
"""
st.markdown(estilo_css, unsafe_allow_html=True)

# 3. Interfaz de usuario
st.title("Generador de Códigos QR Institucional")
st.write("Ingresa el enlace o texto que deseas convertir en un código QR:")

# Variable de entrada para el usuario
texto_usuario = st.text_input("Enlace o texto:")

# Botón para generar
if st.button("Generar QR"):
    if texto_usuario:
        # Lógica para crear el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto_usuario)
        qr.make(fit=True)

        # Crear la imagen usando los colores de la institución
        # El QR será Azul Marino y el fondo Gris Claro
        img = qr.make_image(fill_color="#00304F", back_color="#D6D6D6")

        # Guardar la imagen en la memoria para mostrarla en Streamlit
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Mostrar la imagen en la página
        st.image(byte_im, caption="Tu código QR generado")
        
        # Botón para descargar el QR
        st.download_button(
            label="Descargar QR",
            data=byte_im,
            file_name="codigo_qr_aseg.png",
            mime="image/png"
        )
    else:
        # Mensaje de error si el usuario no escribe nada
        st.warning("Por favor, ingresa un texto o enlace primero.")
