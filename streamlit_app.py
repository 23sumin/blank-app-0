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
    all_rolls = []
    dice_faces = {
        1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
    }
    for _ in range(int(num_rolls)):
        raw_roll = [random.randint(1, int(num_faces)) for _ in range(int(num_dice))]
        roll = tuple(sorted(raw_roll))
        results.add(roll)
        dice_imgs = []
        for v in raw_roll:
            if v in dice_faces:
                dice_imgs.append(dice_faces[v])
            else:
                dice_imgs.append(str(v))
        all_rolls.append(dice_imgs)

    st.subheader("굴린 결과:")
    if int(num_rolls) >= 101:
        st.write("(주사위 그림은 100회까지만 표시됩니다)")
        # 각 굴림의 숫자만 추출하여 한 줄에 공백으로만 구분해 모두 출력
        result_values = []
        for dice_imgs in all_rolls:
            nums = [str(v) if v.isdigit() else ''.join([c for c in v if c.isdigit()]) for v in dice_imgs]
            result_values.extend(nums)
        st.write(" ".join(result_values))
    else:
        for i, dice_imgs in enumerate(all_rolls, 1):
            dice_html = f"<span style='font-size: 5em;'>{' '.join(dice_imgs)}</span>"
            st.markdown(f"{i}번째: {dice_html}", unsafe_allow_html=True)
    st.subheader("나온 조합 (중복 없이):")
    st.write(
        ", ".join(f"({', '.join(map(str, r))})" for r in sorted(results))
    )
