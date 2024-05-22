import streamlit as st
from PIL import Image
import speech_recognition as sr
import threading
import time

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

# Función para escuchar la palabra "Foto" y tomar la foto
def listen_for_photo():
    global img_file_buffer
    with sr.Microphone() as source:
        while True:
            st.write("Di 'Foto' para tomar la foto.")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language="es-ES")
                if "foto" in command.lower():
                    st.write("Tomando foto en 1 segundo...")
                    time.sleep(1)
                    img_file_buffer = st.camera_input("Toma una Foto")
                    if img_file_buffer is not None:
                        image = Image.open(img_file_buffer)
                        st.image(image, caption="Tu Señal de Identificación")
                        st.download_button(
                            label="Descargar",
                            data=open("señal_identificacion.jpg", "rb").read(),
                            file_name="señal_identificacion.jpg",
                            mime="image/jpeg"
                        )
            except sr.UnknownValueError:
                st.write("No se entendió la palabra. Intenta nuevamente.")
            except sr.RequestError as e:
                st.write(f"No se pudo completar la solicitud de reconocimiento de voz; {e}")

# Iniciar el reconocimiento de voz en un hilo separado para no bloquear la interfaz de Streamlit
thread = threading.Thread(target=listen_for_photo)
thread.start()

# Botón para tomar foto manualmente
img_file_buffer = st.camera_input("Toma una Foto manualmente")

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    st.image(image, caption="Tu Señal de Identificación")
    st.download_button(
        label="Descargar",
        data=open("señal_identificacion.jpg", "rb").read(),
        file_name="señal_identificacion.jpg",
        mime="image/jpeg"
    )

st.write("""
### ¡Comparte tu Señal!
Una vez que hayas creado tu señal de identificación, compártela con tus amigos y familiares para que puedan reconocerte fácilmente en la comunidad.
""")
