import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

name = st.title('Это название.')
st.header('Это заголовок.')
st.subheader('А это подзаголовок.')
st.text('Здесь можно писать текс. Например, "Привет".')
st.markdown("This is a markdown") #не поняла эту функцию

st.success('Плитка успеха (зеленая)')
st.info('Плитка информации (синяя)')
st.warning('Плитка предупреждения (желтая)')
st.error('Плитка ошибка (красная)')
st.info("пример")

st.write('Текст с командой write. С помощью нее можно писать текст в формате кода.')
st.write("Пример:", range(10))

from PIL import Image
img = Image.open("altair.jpg")
st.image(img, caption='Альтаир и Малик')

if st.checkbox("Покажи/Убери"):
    st.text("Ты нажал на галочку. Вот текст!")

status = st.radio("Выберите:", ('ДА', 'НЕТ'))
if status == 'ДА':
    st.success('ДА')
else:
    st.error('НЕТ')

character = st.selectbox("Выберите персонажа: ", 
                          ['Альтаир', 'Малик', 'Роберо'])
st.write('Твой персонаж: ', character)

characters = st.multiselect("Выберите персонажа (можно несколько): ",
                            ['Альтаир', 'Малик', 'Роберо'])
st.write(f"Вы выбрали {len(characters)} персонажей.")

if st.button("Нажми кнопку"):
    st.text("Молодец, возьми с полки пирожок)")

name = st.text_input("Введите имя", "Нажмите здесь")
if st.button('Потвердить'):
    result = name.title()
    st.info(result)