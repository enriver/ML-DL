※ 공지사항

1. 보고서 제출시 PDF형태로 제출(word, ppt, excel모두 사용 가능)


### No.1

https://statinknu.tistory.com/19?category=883360

17회 ADP 실기 후기 

1. 출제자가 R을 좋아하는 느낌
2. 시간이 부족함
3. EDA나 전처리는 적정선에서 마무리
4. 문제 문장들이 애매모호한 경우 많음
5. 이건 몰랐지?하는 문제들을 출제(MAPE, FA, 시계열등)
6. ML 문제의 배점은 낮음

문제 예시 (17회)

- Housing Data(집값 예측)

  1-1) EDA 및 데이터 전처리 (시각화 및 통계량)

  1-2) Train Valid Test Set으로 분할 및 시각화 제시

  1-3) 2차 교호작용항까지 고려한 회귀분석 수행 및 변수 선택 과정 제시

  1-4) 벌점, 앙상블을 포함하여 모형에 적합한 기계학습 모델 3가지 (MSE, MAPE, R2제시)

- Corona Data(시계열)

  2-1) 인구대비 코로나 확진자 비율이 가장 높은 국가 5개 제시하고 일일확진자, 누적확진자, 일일 사망자, 누적 사망자 추이를 각각 1장씩의 시각화 그래프로 시각화 (차분을 이용)

  2-2) 

  2-3) 코로나 위험지수를 개발하고 위험지수가 높은 국가 10개를 추려내서 막대그래프로 시각화

  2-4) 시계열 모델링 및 비선형 모델링

- Survey Data

  3-1) 항목별 그룹별 만족도 응답의 평균, 표준편차, 왜도, 첨도 구하기

  3-2) 응답항목별 차이가 있는지 분석 (ANOVA)

  3-3) 탐색적 요인분석 수행 (Factor Analysis)

  3-4) 신뢰성 지수를 개발하는 문제 항목별 신뢰성 지수 구하기

---

### No.2

https://0dood0.tistory.com/33?category=1012731

11회 ADP 실기 후기

1. 통계학 기반 분석 (40점)
   - 각 설명변수들과 출산률의 관계를 회귀분석으로 결과를 해석
2. 텍스트 마이닝을 적용한 분석 (20점)
   - 영화평 Data를 전처리 후, 형용사를 추출하여 감성분석
   - KoNLPP 패키지를 익숙하게 사용할 줄 알아야함
3. ML학습을 통한 결과 도출 (40점)
   - 타이타닉 생존자 Data를 데이터 마이닝 학습해 생존여부 예측
   - Test Data의 정답만을 제출해 예측 적중률을 채점

---

### No.3

https://0dood0.tistory.com/64?category=1012731

15회 ADP 실기 후기

문제 예시 

- 제철 회사 lot data

  1-1) EDA

  1-2) 독립변수 선별(feature engineering)

  1-3) 종속변수를 이항으로 변경후 로지스틱 회귀분석

  1-4) 종속변수 다항인 상태에서 SVM포함해 3가지 알고리즘으로 돌리고 평가

  1-5) 위에서 만든 모델 중 적합한 모델 찾아 군집분석 실시하고 F1 Score값으로 모델이 나이지는지 확인 

- 전력 사용량 data

  2-1) Timestamp 데이터를 datetime 패키지를 이용해 데이터 변환 

---

### No.4

https://didalsgur.tistory.com/32

14회 ADP 실기 후기

문제 예시

- 기계학습을 이용한 집 가격 예측 및 검증
- 다중 로지스틱 회귀분석 및 confusion matrix 해석



---

시험공부하기 좋은 데이터셋 (Kaggle)

- Solar Power Generation Data

  출처 : https://www.kaggle.com/anikannal/solar-power-generation-data

  - 예측, 시계열, 시각화 연습에 좋은 데이터셋

- Credit Card Fraud Detection 

  출처 : https://www.kaggle.com/mlg-ulb/creditcardfraud

  - 로지스틱회귀, 분류 모델 연습에 좋은 데이터셋

- Mall Customer Segmentation Data

  출처 : https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python

  - 군집분석 (KMeans, DBSCAN등 사용가능) 연습에 좋은 데이터셋

- 코로나 또는 미국대선 관련 데이터셋 (현재 발생하는 이슈)