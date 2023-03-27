import joblib
import numpy as np
import pandas as pd
import streamlit as st

# 랜덤 포레스트 모델 불러오기
model_path = "MH/RFmodel.pkl"
model = joblib.load(model_path)

# Streamlit 앱 설정
st.title('Random Forest Model')
st.write('입력 변수')

# 입력 변수를 위한 슬라이더 추가
x1 = st.slider('X1', 0.0, 1.0, 0.5, 0.01)
x2 = st.slider('X2', 0.0, 1.0, 0.5, 0.01)
x3 = st.slider('X3', 0.0, 1.0, 0.5, 0.01)
x4 = st.slider('X4', 0.0, 1.0, 0.5, 0.01)

# 모델을 사용하여 예측 수행
x = np.array([x1, x2, x3, x4] * 19 + [x4]).reshape(1, -1)

y = model.predict(x)[0]

# 예측 결과 출력
st.subheader('예측 결과')
st.write('Y:', y)

# import joblib
# import numpy as np
# import streamlit as st

# # 결정트리 모델 불러오기
# model_path = "MH/DecisionTree.pkl"
# model = joblib.load(model_path)

# # Streamlit 앱 설정
# st.title('결정트리 모델')
# st.write('입력 변수')

# # 입력 변수를 위한 슬라이더 추가
# x1 = st.slider('X1', 0.0, 10.0, 0.5, 0.01)
# x2 = st.slider('X2', 0.0, 1.0, 0.5, 0.01)

# # 모델을 사용하여 예측 수행
# # x = np.array([x1 * 77], [x2]).reshape(1, -1)
# x = np.array([x1]*77).reshape(1, -1)  # 입력값의 차원을 맞춰줍니다.

# y = model.predict(x)
# y = y[0]

# # 예측 결과 출력
# st.subheader('예측 결과')
# st.write('Y:', round(y, 2))
