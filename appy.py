import streamlit as st
from PIL import Image
import speech_recognition as sr
import threading
import time
import io

st.title("¡Aprende Lenguaje de Señas Colombiano!")

st.write("""
### Básico: Tu Señal de Identificación

En esta sección, puedes crear tu propia señal de identificación personalizada. 
En la comunidad de personas sordas, la presentación de los nombres se realiza de manera única y significativa a través del lenguaje de señas. 
Este proceso no solo implica deletrear el nombre con el alfabeto manual, sino también, en muchas ocasiones, incluir un "nombre en señas". 
Este nombre en señas, va más allá de la mera identificación, es en un reflejo de la identidad y la conexión social dentro de la comunidad.
""")

# Video explicativo
st.write("""
Mira este video para conocer más detalles sobre la señal de identificación.
""")
video_url = "https://www.youtube.com/watch?v=sGg6p03wADw" 
st.video(video_url)

st.write("""
## ¡Ponlo en Práctica!
Captura una característica distintiva, ya sea física, de personalidad o relacionada con una experiencia memorable y crea tu propia seña:
""")

# Inicialización de variables para la foto y el reconocimiento de voz
img_file_buffer = None
recognizer = sr.Recognizer()
captured_image = None

# Función para escuchar la palabra "Foto" y tomar la foto
def listen_for_photo():
    global img_file_buffer, captured_image
    with sr.Microphone() as source:
        while True:
            print("Di 'Foto' para tomar la foto.")  # Cambiado a print para evitar la sobrecarga de la interfaz de Streamlit
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language="es-ES")
                if "foto" in command.lower():
                    print("Tomando foto en 1 segundo...")
                    time.sleep(1)
                    st.session_state["take_photo"] = True
            except sr.UnknownValueError:
                print("No se entendió la palabra. Intenta nuevamente.")  # Cambiado a print
            except sr.RequestError as e:
                print(f"No se pudo completar la solicitud de reconocimiento de voz; {e}")  # Cambiado a print

# Iniciar el reconocimiento de voz en un hilo separado para no bloquear la interfaz de Streamlit
if 'take_photo' not in st.session_state:
    st.session_state["take_photo"] = False

thread = threading.Thread(target=listen_for_photo)
thread.daemon = True
thread.start()

# Botón para tomar foto manualmente
if st.button("Toma una Foto manualmente"):
    st.session_state["take_photo"] = True

if st.session_state["take_photo"]:
    img_file_buffer = st.camera_input("Toma una Foto")

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    st.image(image, caption="Tu Señal de Identificación")
    
    # Guardar la imagen en un buffer en memoria
    buf = io.BytesIO()
    image.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Descargar",
        data=byte_im,
        file_name="señal_identificacion.jpg",
        mime="image/jpeg"
    )
    
    # Reset the state to avoid continuous capturing
    st.session_state["take_photo"] = False

st.write("""
### ¡Comparte tu Señal!
Una vez que hayas creado tu señal de identificación, compártela con tus amigos y familiares para que puedan reconocerte fácilmente en la comunidad.
""")
