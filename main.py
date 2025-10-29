import streamlit as st

st.title("정민서의 첫 번째 프로젝트")
st.subheader("할래말래")
st.write('애매하긴 해')
st.write('https://www.naver.com/')
st.link_button("네이버 바로가기",'https://www.naver.com/')

name= st.text_input("이름을 입력해주세요:")
if st.button('환영인사'):
    st.write(f'{name}님 안녕하세요')
    st.balloons()
    st.image('https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/4arX/image/kHEyaIBkalJXnxwx46z7kY5Kwoc.jpg')

st.success('성공!')  #초록
st.warning('하하')   #노랑
st.error('호호')    #빨강
st.info('파랑')    #파랑
