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

st.success(f'안녕하세요 {name}님')  #초록
st.warning('꾸이꾸이')   #노랑
st.error('만나서 반가워요')    #빨강
st.info('당근 후원해주실래요?')    #파랑

if st.button('당근 후원하기'):
    st.balloons()
    st.write(f'{name}님 감사해요!')
    st.video('https://www.youtube.com/watch?v=1TovhBXTAQE')
