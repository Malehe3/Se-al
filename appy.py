import streamlit as st
from PIL import Image, ImageDraw, ImageFont

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

voice_command = st.text_input("Diga 'foto' para tomar una foto")

if voice_command.lower() == "foto":
    img_file_buffer = st.camera_input("Toma una Foto")

    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        st.image(image, caption="Tu Señal de Identificación")
        
        image.save("señal_identificacion.jpg")
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
