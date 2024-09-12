import streamlit as st
import qrcode
from PIL import Image

st.title('QR 코드 생성기')

url = st.text_input('QR 코드로 변환할 URL을 입력하세요:')

if st.button('QR 코드 생성'):
    if url:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        st.image(img, caption='생성된 QR 코드', use_column_width=True)
    else:
        st.error('URL을 입력해 주세요.')
