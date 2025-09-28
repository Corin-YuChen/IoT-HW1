# Setup and Usage Guide

Follow these steps to set up the environment and run the interactive linear regression application.

### Step 1: Prerequisites

- **Python 3**: Ensure you have Python 3 installed on your system.
- **Git**: To clone the repository.

### Step 2: Get the Code

Clone the repository to your local machine:

```bash
# Replace the URL with your actual repository URL
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 3: Create a Virtual Environment

It is highly recommended to use a virtual environment to keep project dependencies isolated.

```bash
# Create a new virtual environment named 'venv'
python3 -m venv venv
```

### Step 4: Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
# Activate the virtual environment first (on Linux/macOS)
source venv/bin/activate

# Install the packages
pip install -r requirements.txt
```

### Step 5: Run the Application

With the dependencies installed, you can now run the Streamlit application.

```bash
streamlit run app.py
```

### Step 6: Accessing the Application

After running the command, Streamlit will provide you with a URL. How you access it depends on your setup:

- **Running on your local machine**: Simply open your browser and go to **`http://localhost:8501`**.

- **Running inside a VirtualBox VM (using NAT with Port Forwarding)**: If you are running the app inside a VirtualBox VM and want to access it from your host machine's browser, you need to:
    1.  **Configure Port Forwarding** in your VM's network settings to forward Host Port `8501` to Guest Port `8501`.
    2.  Run the app inside the VM.
    3.  On your **host machine's browser**, access the application via **`http://localhost:8501`**.
