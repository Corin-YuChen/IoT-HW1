# Interactive Linear Regression App (CRISP-DM)

This project is an interactive web application built with Python and Streamlit to demonstrate a simple linear regression problem. The entire process follows the Cross-Industry Standard Process for Data Mining (CRISP-DM) methodology, providing explanations at each stage.

## Features

- **Interactive Controls**: Adjust sliders to modify the slope (`a`), noise level, and number of data points for the generated dataset.
- **CRISP-DM Framework**: The application is structured around the six phases of CRISP-DM, making it a great educational tool.
- **Live Model Training**: The linear regression model (from scikit-learn) retrains automatically as you change the data parameters.
- **Performance Evaluation**: View key regression metrics like R-squared, MSE, and MAE in real-time.
- **Rich Visualizations**: An interactive Plotly chart displays the original data points, the true underlying relationship, and the model's fitted line.

## Tech Stack

- **Language**: Python
- **Web Framework**: Streamlit
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Plotting**: Plotly

## Setup and Usage

For detailed instructions on how to set up the environment and run the application, please refer to the **[steps.md](steps.md)** file.

## Troubleshooting

A detailed log of the troubleshooting process encountered during development (especially regarding VirtualBox deployment) is available in **[log.md](log.md)**.
