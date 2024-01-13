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