import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="너를 알아보는 두 가지 길", layout="centered")

# --- 스타일 (메인 CSS) ---
st.markdown(
    """
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    .stApp {
        background: linear-gradient(120deg, #f8fbff, #eef2ff);
        font-family: 'Pretendard', sans-serif;
        color: #111;
    }
    .card {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(14px);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
        transition: transform 0.2s ease-in-out;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    }
    .result {
        border: 1px solid rgba(107,141,242,0.3);
        background: rgba(255,255,255,0.5);
        backdrop-filter: blur(10px);
    }
    h1, h2, h3 {
        color: #334155;
        font-weight: 600;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6b8df2, #8ea2f8);
        color: white;
        border-radius: 12px;
        padding: 8px 20px;
        font-weight: 600;
        border: none;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #8ea2f8, #a5b4fc);
        transform: scale(1.02);
    }
    div[data-baseweb="tab-list"] {
        gap: 16px;
    }
    button[data-baseweb="tab"] {
        background-color: #eef2ff;
        border-radius: 10px !important;
        color: #334155 !important;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
    }
    button[data-baseweb="tab"]:hover {
        background-color: #e0e7ff;
        transform: scale(1.03);
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #6b8df2, #8ea2f8);
        color: white !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------
# 페이지 타이틀
# --------------------
st.title("✨ 너를 알아보는 두 가지 길")
st.caption("간단한 MBTI 테스트와 학과 탐색 — 깔끔하고 감각적인 UI")

tabs = st.tabs(["MBTI 테스트 & 추천", "학과 정보 탐색"])

# --------------------
# MBTI 섹션
# --------------------
with tabs[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🔍 간단 MBTI — 10문항")
    st.write("각 문항에서 더 맞는 쪽을 골라줘. 결과로 MBTI와 취향/추천을 알려줄게.")

    questions = [
        {"q": "파티에서 난", "a": "사람들과 활발히 얘기하며 에너지 얻음", "b": "한두 명이랑 깊게 얘기하는 걸 선호함", "trait": "EI"},
        {"q": "결정할 때", "a": "직관/감으로 즉흥적인 편", "b": "계획 세우고 체크하는 편", "trait": "JP"},
        {"q": "정보를 볼 때", "a": "사실과 세부 사항에 주목", "b": "패턴과 미래 가능성에 주목", "trait": "SN"},
        {"q": "토론할 때", "a": "논리와 근거로 말하는 편", "b": "사람 감정과 조화를 고려", "trait": "TF"},
        {"q": "여가시간엔", "a": "계획된 활동으로 효율적으로 보냄", "b": "그날 기분 따라 자유롭게 보냄", "trait": "JP"},
        {"q": "친구가 고민상담할 때", "a": "직설적으로 해결책 제시", "b": "공감과 감정 지지 먼저", "trait": "TF"},
        {"q": "일을 할 때", "a": "체계적으로 하나씩 처리", "b": "여러 가능성 열어두고 진행", "trait": "JP"},
        {"q": "학습 스타일", "a": "구체적 사례와 연습으로 익힘", "b": "개념과 원리 중심으로 이해", "trait": "SN"},
        {"q": "새로운 사람 만나면", "a": "바로 말 걸고 친해지려 함", "b": "관찰 후 천천히 다가감", "trait": "EI"},
        {"q": "결정 내릴 때", "a": "객관적 분석으로 선택", "b": "가치와 감정 고려해 선택", "trait": "TF"},
    ]

    if 'answers' not in st.session_state:
        st.session_state.answers = [None] * len(questions)

    for i, item in enumerate(questions):
        st.write(f"**{i+1}. {item['q']}**")
        st.session_state.answers[i] = st.radio("", (item['a'], item['b']), key=f"q{i}")

    if st.button("결과 보기 🎯"):
        counts = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        mapping = {
            questions[0]['a']: 'E', questions[0]['b']: 'I',
            questions[1]['a']: 'P', questions[1]['b']: 'J',
            questions[2]['a']: 'S', questions[2]['b']: 'N',
            questions[3]['a']: 'T', questions[3]['b']: 'F',
            questions[4]['a']: 'J', questions[4]['b']: 'P',
            questions[5]['a']: 'T', questions[5]['b']: 'F',
            questions[6]['a']: 'J', questions[6]['b']: 'P',
            questions[7]['a']: 'S', questions[7]['b']: 'N',
            questions[8]['a']: 'E', questions[8]['b']: 'I',
            questions[9]['a']: 'T', questions[9]['b']: 'F',
        }
        for ans in st.session_state.answers:
            if ans in mapping:
                counts[mapping[ans]] += 1

        mbti = (
            ('E' if counts['E'] >= counts['I'] else 'I') +
            ('S' if counts['S'] >= counts['N'] else 'N') +
            ('T' if counts['T'] >= counts['F'] else 'F') +
            ('J' if counts['J'] >= counts['P'] else 'P')
        )

        # 추천 데이터 (간단 샘플, 필요하면 더 확장 가능)
        recommendations = {
            'INTJ': {'hobby':'체스/전략게임','song':['Radiohead - Karma Police','BTS - Cypher Pt.3'],'book':'칼 융 - 심리학의 이해','match':['ENFP','ENTP']},
            'INTP': {'hobby':'코딩 프로젝트','song':['Grimes - Oblivion','Zion.T - 복숭아'],'book':'폴 그레이엄 - Hackers & Painters','match':['ENTJ','ENFJ']},
            'ENTJ': {'hobby':'스타트업 기획','song':['Imagine Dragons - Believer','BLACKPINK - Kill This Love'],'book':'리더십 관련 도서','match':['INFP','INTP']},
            'ENTP': {'hobby':'발명/아이디어 브레인스토밍','song':['Tame Impala - The Less I Know The Better','NewJeans - Attention'],'book':'말콤 글래드웰 - 아웃라이어','match':['INFJ','INTJ']},
            'INFJ': {'hobby':'글쓰기/시','song':['Adele - Someone Like You','IU - 밤편지'],'book':'제임스 홀리스 - The Gift of Darkness','match':['ENFP','ENTP']},
            'INFP': {'hobby':'일기/감성 사진','song':['Billie Eilish - Ocean Eyes','IU - Palette'],'book':'파울로 코엘료 - 연금술사','match':['ENFJ','ENTJ']},
            'ENFJ': {'hobby':'멘토링/봉사','song':['Coldplay - Fix You','BTS - Spring Day'],'book':'데일 카네기 - 인간관계론','match':['INFP','INTP']},
            'ENFP': {'hobby':'브이로그/창작 활동','song':['Pharrell Williams - Happy','NewJeans - Hype Boy'],'book':'엘리자베스 길버트 - Eat Pray Love','match':['INFJ','INTJ']},
            'ISTJ': {'hobby':'수집/데이터 정리','song':['The Beatles - Let It Be','IU - 마음'],'book':'체계적 사고 관련 서적','match':['ESFP','ESTP']},
            'ISFJ': {'hobby':'수공예/요리','song':['Jeremy Zucker - Comethru', '태연 - Weekend'],'book':'인간관계/심리서적','match':['ESFP','ESTP']},
            'ESTJ': {'hobby':'조직 운영/클럽 리더','song':['AC/DC - Back In Black','아이유 - Coin'],'book':'리더십/매니지먼트 서적','match':['ISFP','INFP']},
            'ESFJ': {'hobby':'이벤트 기획','song':['Icona Pop - I Love It','BLACKPINK - As If It’s Your Last'],'book':'대인관계 기술서','match':['INFP','ISFP']},
            'ISTP': {'hobby':'메이커/수리','song':['Kendrick Lamar & SZA - luther','SEVENTEEN - 아주 NICE'],'book':'기술 실용서','match':['ESFJ','ENFJ']},
            'ISFP': {'hobby':'그림/사진','song':['Frank Ocean - Pink + White','주현 - 그대 곁에'],'book':'예술 관련 에세이','match':['ESTJ','ESFJ']},
            'ESTP': {'hobby':'아웃도어 스포츠','song':['The Weeknd - Blinding Lights','ITZY - WANNABE'],'book':'실전형 자기계발서','match':['ISFJ','ISTJ']},
            'ESFP': {'hobby':'댄스/공연','song':['Dua Lipa - Levitating','TWICE - Feel Special'],'book':'셀프 표현 관련 책','match':['ISTJ','ISFJ']},
        }

        rec = recommendations.get(mbti, None)

        st.markdown('<div class="result card">', unsafe_allow_html=True)
        st.subheader(f"✨ 결과: {mbti}")
        if rec:
            st.write(f"🎨 추천 취미: {rec['hobby']}")
            st.write(f"🎧 추천 곡: {', '.join(rec['song'])}")
            st.write(f"📚 추천 책: {rec['book']}")
            st.write(f"🤝 잘 맞는 MBTI: {', '.join(rec['match'])}")
            st.write("\n✨ 한 줄 요약: 당신만의 성향을 활용해 작은 실험을 해봐. 취미 하나만 2주간 꾸준히 시도해도 큰 변화가 옴!")
        else:
            st.write("추천 데이터가 준비되지 않았어요. 다음 업데이트에서 추가할게요 🙏")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --------------------
# Major (학과) 섹션
# --------------------
with tabs[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🏫 학과 정보 탐색")
    st.write("문·이과 주요 학과를 간단하게 정리했어. 원하는 학과를 골라봐.")

    majors = {
        '컴퓨터공학':{
            'overview':'소프트웨어, 알고리즘, 컴퓨터 구조를 배우며 문제 해결 능력을 키움.',
            'courses':['프로그래밍', '자료구조', '운영체제', '알고리즘', '컴퓨터네트워크'],
            'careers':['SW개발자', '데이터 엔지니어', 'AI엔지니어', '시스템 아키텍트'],
            'pros':'취업 기회 넓음, 원격·프리랜스 가능',
            'cons':'끊임없는 학습 필요, 경쟁 치열'
        },
        '전자공학':{
            'overview':'회로, 반도체, 통신 등을 다루는 공학분야.',
            'courses':['회로이론','전자회로','신호처리','마이크로프로세서'],
            'careers':['반도체 엔지니어','통신 엔지니어','하드웨어 설계'],
            'pros':'하드웨어 산업 수요 큼',
            'cons':'물리·수학 난이도 높음'
        },
        '기계공학':{
            'overview':'기계 설계, 역학, 열역학 등을 통해 기계 시스템을 연구.',
            'courses':['역학','재료역학','열역학','제어공학'],
            'careers':['설계 엔지니어','자동차·로봇 개발'],
            'pros':'제조업과 연계성 큼',
            'cons':'현장 지식·실무 요구'
        },
        '화학공학':{
            'overview':'화학 공정 설계와 물질 변환 공학을 다룸.',
            'courses':['공정제어','유체역학','화학반응공학'],
            'careers':['공정엔지니어','에너지·소재 산업'],
            'pros':'산업 경쟁력 높음',
            'cons':'실험·현장 중심'
        },
        '물리학':{
            'overview':'자연의 기본 법칙을 수학적으로 탐구함.',
            'courses':['역학','전기·자기학','양자역학','광학'],
            'careers':['연구원','데이터 분석가','금융 모델러','기초과학자'],
            'pros':'기초 이론으로 다양한 분야 진출 가능',
            'cons':'고급 수학 요구, 연구 경쟁 심함'
        },
        '수학':{
            'overview':'순수·응용 수학을 통해 논리적 사고와 문제 해결 능력 강화.',
            'courses':['미적분','대수학','해석학','확률통계'],
            'careers':['연구·금융·데이터 사이언스'],
            'pros':'기초 역량이 넓게 적용됨',
            'cons':'추상적 개념이 많음'
        },
        '생명과학/생물학':{
            'overview':'생명체의 구조와 기능, 유전학을 연구.',
            'courses':['세포생물학','유전학','생화학','분자생물학'],
            'careers':['바이오 연구원','제약회사','의학연구'],
            'pros':'바이오 산업 성장',
            'cons':'실험·랩 업무 많음'
        },
        '경제학':{
            'overview':'자원 배분, 시장 작동 원리, 거시·미시 경제 이론을 공부.',
            'courses':['미시경제','거시경제','계량경제학','금융론'],
            'careers':['금융분야','공공정책','리서치 애널리스트'],
            'pros':'폭넓은 진로, 사회 현상 이해 도움',
            'cons':'수리적·통계적 능력 요구'
        },
        '경영학':{
            'overview':'기업 운영 전반(마케팅, 재무, 인사)을 학습.',
            'courses':['회계','마케팅','조직행동','재무관리'],
            'careers':['기업관리자','마케터','컨설턴트'],
            'pros':'실무적 스킬 습득 유리',
            'cons':'전공자 많아 차별화 필요'
        },
        '심리학':{
            'overview':'행동과 마음을 과학적으로 연구.',
            'courses':['인지심리','사회심리','발달심리','통계'],
            'careers':['상담사','HR, UX리서처','교육 분야'],
            'pros':'사람 이해력 증가',
            'cons':'전문직 진입 위해 추가 자격/대학원 필요'
        },
        '법학':{
            'overview':'법의 이론과 사례를 학습하며 논리적 사고를 키움.',
            'courses':['헌법','민법','형법','상법'],
            'careers':['변호사','공무원','기업 법무팀'],
            'pros':'사회적 지위·보수 안정적',
            'cons':'사법시험(또는 변호사 시험) 대비 필요'
        },
        '국어국문학':{
            'overview':'문학·언어·비평을 통해 국어 문화 이해.',
            'courses':['고전문학','현대문학','언어학','문학비평'],
            'careers':['출판·편집·교사·콘텐츠 창작'],
            'pros':'글쓰기·비판적 사고 향상',
            'cons':'진로 다양성은 있으나 경쟁 심함'
        },
        '미술/디자인':{
            'overview':'시각 표현과 디자인 원리를 배워 창작물을 만듦.',
            'courses':['드로잉','색채학','디자인 이론','포트폴리오 제작'],
            'careers':['그래픽 디자이너','제품디자이너','일러스트레이터'],
            'pros':'포트폴리오로 실력 직접 증명 가능',
            'cons':'프리랜스·계약직이 많음'
        }
    }

    major_list = list(majors.keys())
    choice = st.selectbox("학과 선택", ["-- 선택 --"] + major_list)

    if choice and choice != "-- 선택 --":
        info = majors[choice]
        st.markdown('<div class="result card">', unsafe_allow_html=True)
        st.subheader(f"💡 {choice}")
        st.write(f"{info['overview']}")
        st.write(f"\n⚙️ 주요 과목: {', '.join(info['courses'])}")
        st.write(f"\n🚀 진로: {', '.join(info['careers'])}")
        st.write(f"\n👍 장점: {info['pros']}")
        st.write(f"\n👎 단점: {info['cons']}")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- footer ---
st.markdown("---")
st.write("📘 `streamlit run app.py` 로 실행하세요.")
st.caption("만든 사람: 민서 ✨")
