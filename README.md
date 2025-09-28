# IoT Occupancy Prediction with Streamlit

This project implements an IoT occupancy prediction system using a Streamlit web application. The application allows users to input environmental sensor data (temperature, humidity, light, motion) and receive a real-time prediction of room occupancy. It also provides data visualizations to help understand the underlying patterns.

## Features

*   **Real-time Occupancy Prediction:** Input sensor data and get instant occupancy predictions.
*   **Confidence Score:** View the confidence level of the prediction.
*   **Data Visualizations:** Explore sensor data distributions, relationships, and correlations through interactive plots.

## Deployed Streamlit Application

You can access the live Streamlit application here:
[https://iot-hw1-wlhbf25qmjr3c2eazsnrkb.streamlit.app/](https://iot-hw1-wlhbf25qmjr3c2eazsnrkb.streamlit.app/)

## Technologies Used

*   **Streamlit:** For building the interactive web application.
*   **Pandas & NumPy:** For data manipulation and numerical operations.
*   **Scikit-learn:** For machine learning model (occupancy prediction) and data scaling.
*   **Matplotlib & Seaborn:** For creating insightful data visualizations.
*   **Joblib:** For saving and loading the trained machine learning model and scaler.

## Local Setup and Run

To run this application on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/IoT-HW1.git # Replace with your actual GitHub repository URL
    cd IoT-HW1
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    This will open the application in your web browser.