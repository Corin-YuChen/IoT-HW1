
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# --- 1. Business Understanding (商務理解) ---
st.title("CRISP-DM 流程：簡單線性迴歸分析")

st.header("1. Business Understanding (商務理解)")
st.write(
    """
    **目標：** 建立一個互動式應用程式，讓使用者可以透過調整參數來生成資料，並觀察線性迴歸模型的表現。
    
    **情境：** 假設我們想探討一個變數 `x` 和 `y` 之間的線性關係。我們相信它們的關係可以用 `y = ax + b` 來描述，但在真實世界中，觀測到的數據總是會帶有一些隨機的「雜訊」。
    
    這個應用程式將幫助我們：
    1.  **生成模擬資料**：根據使用者設定的 `a` (斜率)、`b` (截距)、雜訊量和資料點數量。
    2.  **建立迴歸模型**：使用生成的資料來訓練一個簡單線性迴歸模型。
    3.  **評估模型**：視覺化模型結果並計算評估指標，了解模型擬合的好壞。
    """
)

# --- Sidebar for User Input (使用者輸入) ---
st.sidebar.header("參數設定")
st.sidebar.write("調整以下參數來生成新的數據集：")

# 讓使用者調整 a, noise, 和 number of points
a_true = st.sidebar.slider("真實斜率 (a)", -10.0, 10.0, 2.5, 0.1)
b_true = 50.0  # 為了簡化，我們固定 b
noise_level = st.sidebar.slider("雜訊量 (Noise)", 0.0, 100.0, 20.0, 1.0)
n_points = st.sidebar.slider("資料點數量 (Number of Points)", 10, 1000, 200, 10)

# --- 2. Data Understanding (資料理解) ---
st.header("2. Data Understanding (資料理解)")
st.write(
    """
    在這個階段，我們將根據您在側邊欄設定的參數來生成資料，並對其進行初步的探索。
    """
)

# Data Generation Function
@st.cache_data
def generate_data(a, b, noise, n):
    """根據給定參數生成線性數據"""
    X = np.random.rand(n, 1) * 10  # X 在 0 到 10 之間
    noise_array = np.random.randn(n, 1) * noise
    y = a * X + b + noise_array
    df = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})
    return df

data = generate_data(a_true, b_true, noise_level, n_points)

st.subheader("生成的資料預覽")
st.write(data.head())

st.subheader("資料視覺化")
fig_scatter = px.scatter(data, x='X', y='y', title="生成的數據分佈 (X vs y)")
st.plotly_chart(fig_scatter, use_container_width=True)

# --- 3. Data Preparation (資料準備) ---
st.header("3. Data Preparation (資料準備)")
st.write(
    """
    在這個階段，我們需要將資料整理成模型可以接受的格式。對於 scikit-learn 的線性迴歸模型，我們需要將特徵 (X) 和目標 (y) 分開。
    
    -   **特徵 (X)**：獨立變數，我們用它來進行預測。
    -   **目標 (y)**：相依變數，我們想要預測的對象。
    
    在這個案例中，生成的資料已經很乾淨，不需要進行複雜的清洗或轉換。
    """
)

X_train = data[['X']]
y_train = data['y']

st.write("**特徵 (X) 的前5筆:**")
st.write(X_train.head())
st.write("**目標 (y) 的前5筆:**")
st.write(y_train.head())

# --- 4. Modeling (模型建立) ---
st.header("4. Modeling (模型建立)")
st.write(
    """
    我們選擇了**簡單線性迴歸 (Simple Linear Regression)** 模型，因為我們假設 `X` 和 `y` 之間存在線性關係。我們將使用 scikit-learn 函式庫來建立和訓練模型。
    """
)

# 建立並訓練模型
model = LinearRegression()
model.fit(X_train, y_train)

a_pred = model.coef_[0]
b_pred = model.intercept_

st.subheader("模型訓練結果")
st.write(f"模型預測的斜率 (a): `{a_pred:.2f}` (真實斜率為: `{a_true:.2f}`)")
st.write(f"模型預測的截距 (b): `{b_pred:.2f}` (真實截距為: `{b_true:.2f}`)")

# --- 5. Evaluation (模型評估) ---
st.header("5. Evaluation (模型評估)")
st.write(
    """
    在這個階段，我們評估模型的表現如何。除了比較預測的係數與真實係數外，我們還會計算一些常見的評估指標，並將模型的預測結果視覺化。
    """
)

# 進行預測
y_pred = model.predict(X_train)

# 計算評估指標
mse = mean_squared_error(y_train, y_pred)
r2 = r2_score(y_train, y_pred)
mae = mean_absolute_error(y_train, y_pred)

st.subheader("評估指標")
col1, col2, col3 = st.columns(3)
col1.metric("R-squared (R²)", f"{r2:.3f}", help="R² 衡量模型對數據變異性的解釋程度，越接近1越好。")
col2.metric("Mean Squared Error (MSE)", f"{mse:.2f}", help="MSE 是預測誤差平方的平均值，值越小越好。")
col3.metric("Mean Absolute Error (MAE)", f"{mae:.2f}", help="MAE 是預測誤差絕對值的平均值，值越小越好。")

st.subheader("視覺化評估")

# 建立包含所有線條的圖表
fig_results = go.Figure()

# 1. 原始數據點
fig_results.add_trace(go.Scatter(x=data['X'], y=data['y'], mode='markers', name='原始數據點', marker=dict(opacity=0.7)))

# 2. 真實關係線 (無雜訊)
line_x = np.array([0, 10])
line_y_true = a_true * line_x + b_true
fig_results.add_trace(go.Line(x=line_x, y=line_y_true, mode='lines', name='真實關係線', line=dict(color='green', dash='dash')))

# 3. 模型擬合線
line_y_pred = a_pred * line_x + b_pred
fig_results.add_trace(go.Line(x=line_x, y=line_y_pred, mode='lines', name='模型擬合線', line=dict(color='red', width=3)))

fig_results.update_layout(
    title="模型評估：真實關係 vs. 模型擬合結果",
    xaxis_title="X",
    yaxis_title="y",
    legend_title="圖例"
)

st.plotly_chart(fig_results, use_container_width=True)

# --- 6. Deployment (部署) ---
st.header("6. Deployment (部署)")
st.write(
    """
    這個階段是將模型或分析結果整合到實際應用中。您現在看到的**這個 Streamlit 網頁應用本身，就是一個部署的範例**。
    
    它提供了一個使用者介面，讓非技術人員也能透過互動的方式來使用這個模型、探索數據，並從中獲得洞見。
    
    **如何執行這個應用程式：**
    1.  確保您已經安裝了所有必要的套件：
        ```bash
        pip install -r requirements.txt
        ```
    2.  在您的終端機中，導航到這個 `app.py` 檔案所在的目錄，然後執行以下命令：
        ```bash
        streamlit run app.py
        ```
    """
)

st.info("應用程式結束。您可以繼續在側邊欄調整參數，觀察模型的變化。")
