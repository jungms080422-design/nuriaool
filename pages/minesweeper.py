# minesweeper_app.py
import streamlit as st
import random
from collections import deque
import time

st.set_page_config("지뢰찾기 — 민서용", layout="centered")

# --- CSS (심플 & 감각적) ---
st.markdown("""
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
.stApp { font-family: 'Pretendard', sans-serif; background: linear-gradient(120deg,#f8fbff,#eef2ff); }
.game-card {
  background: rgba(255,255,255,0.7); backdrop-filter: blur(8px);
  border-radius:14px; padding:18px; box-shadow:0 10px 30px rgba(15,23,42,0.06);
}
.cell-btn {
  height:36px; width:36px; margin:2px; border-radius:6px;
  border: none; font-weight:700;
}
.cell-closed { background:#eef2ff; }
.cell-open { background: rgba(255,255,255,0.85); }
.cell-mine { background: #ffecec; color:#d32f2f; }
.info-row { display:flex; gap:12px; align-items:center; margin-bottom:8px; }
.small { font-size:0.9rem; color:#334155; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="game-card">', unsafe_allow_html=True)
st.title("💣 지뢰찾기 — 한 판 할래?")
st.write("크기랑 지뢰 수 조절해서 즐겨. 좌클릭: 공개, 우클릭(혹은 플래그 모드): 깃발 표시/해제")
st.markdown('---')

# --- 설정 옵션 ---
col1, col2, col3 = st.columns([1,1,1])
with col1:
    rows = st.selectbox("행 수", [8, 9, 10, 12, 14], index=0)
with col2:
    cols = st.selectbox("열 수", [8, 9, 10, 12, 14], index=0)
with col3:
    mines = st.selectbox("지뢰 개수", [5, 8, 10, 12, 15, 20], index=2)

# 플래그 모드 토글 (streamlit에서는 우클릭 이벤트 잡기 복잡하니 모드로 처리)
flag_mode = st.checkbox("🚩 플래그 모드 (깃발 꽂기/해제)", value=False)

# 초기화 버튼
if 'config' not in st.session_state or st.session_state.get('config') != (rows, cols, mines):
    st.session_state.clear()  # 새 설정이면 완전 초기화
    st.session_state['config'] = (rows, cols, mines)

if st.button("새 게임 ▶️"):
    st.session_state.clear()
    st.session_state['config'] = (rows, cols, mines)

# --- 초기화 함수 ---
def init_board(r, c, m):
    total = r * c
    # place mines
    mine_positions = set(random.sample(range(total), m))
    board = [[0 for _ in range(c)] for _ in range(r)]
    for idx in mine_positions:
        rr = idx // c
        cc = idx % c
        board[rr][cc] = -1  # mine
    # fill numbers
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1: continue
            cnt = 0
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    ni, nj = i+di, j+dj
                    if 0<=ni<r and 0<=nj<c and board[ni][nj] == -1:
                        cnt += 1
            board[i][j] = cnt
    return board

# create board if not exists
if 'board' not in st.session_state:
    r,c,m = rows, cols, mines
    st.session_state['board'] = init_board(r,c,m)
    st.session_state['revealed'] = [[False]*c for _ in range(r)]
    st.session_state['flags'] = [[False]*c for _ in range(r)]
    st.session_state['state'] = 'playing'  # playing / lost / won
    st.session_state['start_time'] = time.time()
    st.session_state['elapsed'] = 0

# helpers
def in_bounds(i,j):
    r,c = len(st.session_state['board']), len(st.session_state['board'][0])
    return 0 <= i < r and 0 <= j < c

def reveal_cell(i,j):
    if st.session_state['state'] != 'playing': return
    if st.session_state['flags'][i][j]: return
    if st.session_state['revealed'][i][j]: return
    board = st.session_state['board']
    # if mine -> game over
    if board[i][j] == -1:
        st.session_state['revealed'][i][j] = True
        st.session_state['state'] = 'lost'
        st.session_state['elapsed'] = int(time.time() - st.session_state['start_time'])
        return
    # BFS reveal for 0s
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        if st.session_state['revealed'][x][y]: continue
        st.session_state['revealed'][x][y] = True
        if st.session_state['board'][x][y] == 0:
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    nx, ny = x+di, y+dj
                    if in_bounds(nx,ny) and not st.session_state['revealed'][nx][ny] and not st.session_state['flags'][nx][ny]:

# --- 이어서 (minesweeper_app.py 완성본) ---
                        q.append((nx, ny))

def toggle_flag(i, j):
    if st.session_state['state'] != 'playing': return
    if st.session_state['revealed'][i][j]: return
    st.session_state['flags'][i][j] = not st.session_state['flags'][i][j]

def check_win():
    r, c = len(st.session_state['board']), len(st.session_state['board'][0])
    for i in range(r):
        for j in range(c):
            if st.session_state['board'][i][j] != -1 and not st.session_state['revealed'][i][j]:
                return False
    st.session_state['state'] = 'won'
    st.session_state['elapsed'] = int(time.time() - st.session_state['start_time'])
    return True

# --- 게임판 표시 ---
st.markdown('<div class="info-row">', unsafe_allow_html=True)
if st.session_state['state'] == 'playing':
    st.markdown(f'<span class="small">⌛ 경과 시간: {int(time.time() - st.session_state["start_time"])}초</span>', unsafe_allow_html=True)
elif st.session_state['state'] == 'lost':
    st.error(f"💥 지뢰 밟음! ({st.session_state['elapsed']}초)")
elif st.session_state['state'] == 'won':
    st.success(f"🎉 클리어! ({st.session_state['elapsed']}초)")
st.markdown('</div>', unsafe_allow_html=True)

r, c = len(st.session_state['board']), len(st.session_state['board'][0])
for i in range(r):
    cols = st.columns(c)
    for j in range(c):
        cell_style = "cell-btn "
        content = ""
        disabled = False

        if st.session_state['revealed'][i][j]:
            val = st.session_state['board'][i][j]
            cell_style += "cell-open "
            if val == -1:
                content = "💣"
                cell_style += "cell-mine"
            elif val > 0:
                content = str(val)
        else:
            cell_style += "cell-closed "
            if st.session_state['flags'][i][j]:
                content = "🚩"

        if st.session_state['state'] != 'playing':
            disabled = True

        # 버튼 클릭 처리
        if cols[j].button(content or " ", key=f"{i}-{j}", use_container_width=True, disabled=disabled):
            if flag_mode:
                toggle_flag(i, j)
            else:
                reveal_cell(i, j)
                check_win()

# --- 하단 문구 ---
st.markdown("---")
st.caption("💣 Made with ❤️ by 민서 | 감각적인 Streamlit 지뢰찾기")

st.markdown("</div>", unsafe_allow_html=True)
