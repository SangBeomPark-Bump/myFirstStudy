from IPython.display import display, HTML, clear_output

# 출력 업데이트 예제
for i in range(10):
    clear_output(wait=True)  # 이전 출력 지우기
    display(f"Progress: {i}/10")