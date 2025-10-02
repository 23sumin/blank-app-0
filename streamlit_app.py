import streamlit as st



st.header("주사위 결과 중복 없이 나열하기")



num_dice = st.number_input("주사위의 수 (1 이상)", min_value=1, value=2, step=1)
num_faces = 6  # 주사위 면의 수는 6으로 고정
num_rolls_input = st.text_input("주사위를 굴리는 횟수 (숫자 또는 '모든 경우의 수' 입력)", value="10")
multiple_of = st.text_input("합이 배수인지 판별할 수 (입력 시 배수 여부 표시)")
# 순서 상관없이(중복 제거) or 순서 상관있게(중복 허용) 결과 나열 선택
ignore_order = st.checkbox("주사위 결과를 순서와 상관없이 나열 (예: (1,4), (4,1) 중복 제거)", value=True)

if st.button("주사위 굴리기"):
    import random
    from itertools import product
    results = set()
    all_rolls = []
    dice_faces = {
        1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
    }
    if num_rolls_input.strip() == "모든 경우의 수":
        all_combinations = product(range(1, int(num_faces)+1), repeat=int(num_dice))
        for comb in all_combinations:
            if ignore_order:
                roll = tuple(sorted(comb))
                results.add(roll)
            else:
                results.add(tuple(comb))
        # all_rolls는 실제 굴림 결과가 아니므로, 그림 출력은 생략
    else:
        num_rolls = int(num_rolls_input)
        for _ in range(num_rolls):
            raw_roll = [random.randint(1, int(num_faces)) for _ in range(int(num_dice))]
            if ignore_order:
                roll = tuple(sorted(raw_roll))
            else:
                roll = tuple(raw_roll)
            results.add(roll)
            dice_imgs = []
            for v in raw_roll:
                if v in dice_faces:
                    dice_imgs.append(dice_faces[v])
                else:
                    dice_imgs.append(str(v))
            all_rolls.append(dice_imgs)

    if not (num_rolls_input.strip() == "모든 경우의 수"):
        st.subheader("굴린 결과:")
        if int(num_rolls_input) >= 101:
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
    show_multiple = multiple_of.strip().isdigit() and int(multiple_of) > 1
    if show_multiple:
        left_col, right_col = st.columns(2)
        left_list = []  # 배수인 경우
        right_list = [] # 배수가 아닌 경우
        m = int(multiple_of)
        for r in sorted(results):
            s = sum(r)
            is_multiple = (s % m == 0)
            line = f"({' ,'.join(map(str, r))}) → 합: {s}"
            if is_multiple:
                left_list.append(line)
            else:
                right_list.append(line)
        with left_col:
            st.markdown("**배수(✅)**")
            for l in left_list:
                st.write(l)
        with right_col:
            st.markdown("**배수 아님(❌)**")
            for l in right_list:
                st.write(l)
    else:
        st.write("  ".join([f"({' ,'.join(map(str, r))})" for r in sorted(results)]))
