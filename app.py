import streamlit as st
import qrcode
from io import BytesIO

# 1. Configuración de la página
st.set_page_config(page_title="Generador de QR - ASEG", page_icon="📱")

# 2. Inyección de CSS para los colores institucionales
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

    /* Centrar la imagen generada y el botón de descarga en la pantalla */
    div[data-testid="stImage"], div[data-testid="stDownloadButton"] {
        display: flex;
        justify-content: center;
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
    /* --- NUEVA REGLA: Forzar color BLANCO en el texto del botón --- */
    .stButton > button p, .stButton > button div, .stButton > button span {
        color: white !important;
    }
    /* Efecto al pasar el mouse por el botón (Hover) */
    .stButton > button:hover {
        background-color: #57A0D4 !important; /* Azul Hover */
        color: white !important;
        border-color: #00304F !important;
    }

    /* Estilo de la caja de texto y centrado de su contenido */
    .stTextInput > div > div > input {
        background-color: #D6D6D6; /* Gris Claro de fondo */
        color: #362D32; /* Gris Oscuro para texto */
        border: 2px solid #00304F;
        border-radius: 5px;
        text-align: center;
    }
</style>
"""
st.markdown(estilo_css, unsafe_allow_html=True)

# 3. Interfaz de usuario
st.title("Generador de Códigos QR")
st.write("Ingresa el enlace o texto que deseas convertir en un código QR:")

# Variable de entrada para el usuario
texto_usuario = st.text_input("Enlace o texto:")

# 4. Uso de columnas para centrar exclusivamente el botón de generar
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Creamos el botón dentro de la columna central
    boton_generar = st.button("Generar QR", use_container_width=True)

# Lógica si se presiona el botón
if boton_generar:
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

        # Crear la imagen: negro con fondo blanco
        img = qr.make_image(fill_color="black", back_color="white")

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
