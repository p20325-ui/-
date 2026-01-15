import streamlit as st
import pandas as pd

experience = st.selectbox('실험(활동)을 선택해주세요:', ['탄소포집 실험','이항분포기 만들기 활동'
])

\
experience_data={'탄소포집 실험':data = {
    "시간(분)": list(range(21)),
    "활성탄": [5000,4612,4235,3827,3502,3208,2951,2698,2465,2243,
             2048,1863,1704,1568,1442,1331,1230,1142,1065,1002,950],
    "숯": [5000,4948,4890,4832,4774,4720,4675,4632,4593,4556,
          4521,4488,4459,4430,4404,4380,4358,4336,4315,4297,4280],
    "흑연": [500,499,499,498,498,498,498,497,497,497,
           497,497,497,497,497,497,497,496,496,496,496]
}

df = pd.DataFrame(data)

if st.button(" 데이터 생성"):
    
    st.header("1. 실험 데이터")
    st.dataframe(df, use_container_width=True)

    st.header("2. 시간별 CO₂ 농도 변화")
    st.line_chart(
        df.set_index("시간(분)")[["활성탄", "숯", "흑연"]],
        height=400
    )

    st.header("3. 시간 선택 분석")
    time = st.slider("확인할 시간을 선택하세요 (분)", 0, 20, 10)
    selected = df[df["시간(분)"] == time]

    st.write(f"⏱ **{time}분 후 CO₂ 농도 (ppm)**")
    st.table(selected.set_index("시간(분)"))

    st.header("4. CO₂ 제거 효율 분석")
    initial = 5000
    final_values = df.iloc[-1][["활성탄", "숯", "흑연"]]
    efficiency = (initial - final_values) / initial * 100

    eff_df = pd.DataFrame({
        "흡착제": efficiency.index,
        "제거 효율 (%)": efficiency.values
    }).set_index("흡착제")

    st.bar_chart(eff_df)

    st.header("5. 결론")
    st.markdown("""
    - **활성탄**: 가장 높은 CO₂ 제거 효율  
    - **숯**: 중간 수준의 흡착 성능  
    - **흑연**: 거의 흡착되지 않음  

    -> **비표면적과 기공 구조가 탄소 포집 효율을 결정**
    """)},{'이항분포기 만들기 활동':import streamlit as st
st.set_page_config(page_title="이항분포기 만들기", layout="centered")
st.title("📊 이항분포기 만들기 활동")
st.header("1️⃣ 이항분포기란 무엇인가")
st.markdown("""
이항분포기는 **성공 또는 실패의 두 가지 결과만 가지는 시행**을  
여러 번 반복할 때, **성공 횟수의 확률 분포**를 나타내는 도구이다.

예를 들어,
- 동전을 여러 번 던질 때 앞면이 나오는 횟수
- 문제를 맞히거나 틀리는 경우

와 같은 상황에서 이항분포를 사용할 수 있다.
""")
st.header("2️⃣ 이항분포기를 어떻게 만들었는가")
st.markdown("""
- 각 시행은 **성공 또는 실패** 두 가지 경우만 가지도록 설정하였다.
- 시행 횟수(n)와 성공 확률(p)을 정하여 확률을 계산하였다.
- 이를 바탕으로 성공 횟수에 따른 확률을 확인할 수 있도록 구성하였다.

이 과정을 통해 **확률의 누적과 분포 개념**을 이해할 수 있었다.
""")

st.header("3️⃣ 이 활동을 통해 무엇을 배웠는가")

st.markdown("""
- 확률은 단순한 계산이 아니라 **반복 실험의 결과를 예측하는 도구**임을 알게 되었다.
- 시행 횟수와 성공 확률에 따라 분포의 모양이 달라진다는 것을 이해하였다.
- 수학적 개념을 **프로그램으로 구현**하면서 개념이 더 명확해졌다.
""")}


