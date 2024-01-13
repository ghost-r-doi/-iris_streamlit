# 必要なライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

# タイトルとテキストを記入
st.title('Streamlit 基礎')
img = Image.open('iris.jpg')
st.image(img,caption = 'Iris' , use_column_width = True)

if st.checkbox('Show Image'):
    img = Image.open('iris.jpg')
    st.image(img,caption = 'Iris' , use_column_width = True)

# セレクトボックス
option = st.selectbox(
    '好きな数字を入力してください。',
    list(range(1, 11))
)

'あなたの好きな数字は' , option , 'です。'

