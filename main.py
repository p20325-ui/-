import streamlit as st
import pandas as pd

\
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
    """)

