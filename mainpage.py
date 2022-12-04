import streamlit as st
import pandas as pd
from PIL import Image

st.write('never gonna give you up')

col1, col2, col3 = st.columns((2,4,1))
with col1:
    st.image(Image.open('dark_logo.png'))
    # if st.theme():
    #     st.image(Image.open('logo.png'))
    # else:
    #     st.image(Image.open('dark_logo.png'))

# st.plotly_chart(fig.update_layout(theme))
with col2:
    st.header(' ')
    st.header('Knowledge Represent')
    st.markdown('Your choice, your comfort')
# with col3: 
    # st.title('Represent')
st.markdown('# 30 days of NNN is over')

with st.form("my_form"):
    option = st.multiselect(
        'Quận',
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
        'Tân Bình', 'Bình Tân', 'Tân Phú', 'Bình Thạnh', 'Gò Vấp', 'Phú Nhuận',
        'Hóc Môn', 'Bình Chánh', 'Nhà Bè', 'Củ Chi'))

    submitted = st.form_submit_button("Next")

if not option and submitted==True:
    st.warning("Hãy chọn quận!!",icon="⚠️")

if option:
    with st.form("serching_form"):
        st.write('Quận đã chọn: ', ', '.join(option))   
        with st.expander("filter"):
        # st.text("Filter")
            money = st.slider('Chọn giá tiền (triệu/m²)',0, 200, (0, 50))
        search = st.form_submit_button("Search")
        if search:
            st.write('Quận đã chọn: ', ', '.join(option))
            # st.select_slider("Displayed values:", ["Normalized", "Absolute"])