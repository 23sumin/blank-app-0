import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


st.header("주사위 결과 중복 없이 나열하기")

# 입력값 받기
num_dice = st.number_input("주사위의 수 (2 이상)", min_value=2, value=2, step=1)
num_faces = st.number_input("주사위의 면의 수 (2 이상)", min_value=2, value=6, step=1)
num_rolls = st.number_input("주사위를 굴리는 횟수 (1 이상)", min_value=1, value=10, step=1)

if st.button("주사위 굴리기"):
    import random
    results = set()
    for _ in range(int(num_rolls)):
        roll = tuple(sorted([random.randint(1, int(num_faces)) for _ in range(int(num_dice))]))
        results.add(roll)
    st.subheader("나온 조합 (중복 없이):")
    st.write(
        ", ".join(f"({', '.join(map(str, r))})" for r in sorted(results))
    )
