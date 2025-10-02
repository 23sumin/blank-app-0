import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 주사위 시각화 함수
import matplotlib.pyplot as plt
import numpy as np

st.header("주사위 윗면 시각화")
num_dice = st.number_input("주사위의 개수", min_value=1, max_value=10, value=1)
num_faces = st.number_input("주사위의 면 수", min_value=2, max_value=20, value=6)

if st.button("주사위 굴리기"):
    results = np.random.randint(1, num_faces+1, size=num_dice)
    st.write(f"결과: {results}")
    fig, axes = plt.subplots(1, num_dice, figsize=(2*num_dice, 2))
    if num_dice == 1:
        axes = [axes]
    for ax, value in zip(axes, results):
        # 사각형으로 주사위 윗면 그리기
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, fill=True, color='white', edgecolor='black', linewidth=2))
        ax.text(0.5, 0.5, str(value), fontsize=24, ha='center', va='center')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    plt.tight_layout()
    st.pyplot(fig)
