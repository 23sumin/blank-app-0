import streamlit as st

problems = [
	{
		"question": "1. 의자 5개에 5명의 학생(철수, 영희, 민수, 수지, 현우)이 앉을 때, 철수는 항상 첫 번째, 현우는 항상 마지막 의자에 앉는다고 할 때, 나올 수 있는 모든 경우의 수는 몇 개인가요?",
		"answer": "6"
	},
	{
		"question": "2. 6면체 주사위 2개를 동시에 던질 때, 나올 수 있는 눈의 합이 8의 배수(8, 16, ...)가 되는 경우의 수는 몇 개인가요?",
		"answer": "5"
	},
	{
		"question": "3. 6면체 주사위 3개를 동시에 던질 때, 나올 수 있는 눈의 합이 10이 되는 경우의 수는 몇 개인가요?",
		"answer": "27"
	}
]

# 세션 상태로 현재 문제 번호와 정답 여부 관리
if 'quiz_idx' not in st.session_state:
	st.session_state.quiz_idx = 0
if 'quiz_correct' not in st.session_state:
	st.session_state.quiz_correct = [False] * len(problems)

idx = st.session_state.quiz_idx

if idx < len(problems):
	st.write(problems[idx]["question"])
	user_answer = st.text_input("정답을 입력하세요", key=f"quiz_{idx}")
	if st.button("제출", key=f"submit_{idx}"):
		if user_answer.strip() == problems[idx]["answer"]:
			st.success("정답입니다! 다음 문제로 이동합니다.")
			st.session_state.quiz_correct[idx] = True
			st.session_state.quiz_idx += 1
		else:
			st.error("오답입니다. 다시 시도해보세요.")
else:
	st.success("모든 문제를 맞췄습니다! 수고하셨습니다.")
