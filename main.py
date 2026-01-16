import streamlit as st
import pandas as pd

experience = st.selectbox(
    "실험(활동)을 선택해주세요:",
    ["탄소포집 실험", "이항분포기 만들기 활동"]
)

if experience == "탄소포집 실험":

    data = {
        "시간(분)": list(range(21)),
        "활성탄": [5000,4612,4235,3827,3502,3208,2951,2698,2465,2243,
                 2048,1863,1704,1568,1442,1331,1230,1142,1065,1002,950],
        "숯": [5000,4948,4890,4832,4774,4720,4675,4632,4593,4556,
              4521,4488,4459,4430,4404,4380,4358,4336,4315,4297,4280],
        "흑연": [500,499,499,498,498,498,498,497,497,497,
               497,497,497,497,497,497,497,496,496,496,496]
    }

    df = pd.DataFrame(data)

    if st.button("데이터 생성"):
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

        st.write(f"{time}분 후 CO₂ 농도 (ppm)")
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
        """)

elif experience == "이항분포기 만들기 활동":

    if st.button("데이터 생성"):
        st.title("이항분포기 만들기 활동")

        data = {
            "시행 횟수": list(range(8)),
            "성공할 확률": [1/64, 6/64, 15/64, 20/64, 15/64, 6/64, 1/64]
        }

        df = pd.DataFrame(data)

        st.header("1. 이항분포기란 무엇인가")
        st.markdown("""
        이항분포기는 성공 또는 실패의 두 가지 결과만 가지는 시행을
        여러 번 반복할 때 성공 횟수의 확률 분포를 나타낸다.
        """)

        st.header("2. 이항분포기를 어떻게 만들었는가")
        st.markdown("""
        - 시행은 성공/실패 두 경우만 갖도록 설정하였다.
        - 시행 횟수와 성공 확률을 정하여 분포를 이해하였다.
        """)

        st.header("3. 이 활동을 통해 무엇을 배웠는가")
        st.markdown("""
        - 반복 실험에서 확률 분포가 형성됨을 이해했다.
        - 수학 개념을 프로그래밍으로 표현할 수 있음을 배웠다.
        """)

        st.header("4. 이항분포 그래프")
        st.bar_chart(df.set_index("시행 횟수"))
