# Troubleshooting Log

This document logs the troubleshooting process for deploying the Streamlit web application, particularly within a VirtualBox environment.

### Initial Goal

To create an interactive Streamlit application for a simple linear regression problem and deploy it.

### Problem 1: Python Environment Errors

- **Symptom**: `pip install -r requirements.txt` failed with an `externally-managed-environment` error.
- **Reason**: The system's base Python installation is protected. Direct installation of packages is discouraged.
- **Solution**: Created a dedicated virtual environment (`python3 -m venv gemini_venv`) and used its `pip` to install dependencies. This isolates the project and avoids conflicts.

### Problem 2: Server Not Accessible from Host Machine

- **Symptom**: After starting the server, it was not accessible from the host machine's browser, resulting in `ERR_CONNECTION_REFUSED`.
- **Reason**: By default, Streamlit binds to `localhost`, meaning it only accepts connections from within the VM itself.
- **Solution**: Restarted the server with the `--server.address=0.0.0.0` flag, telling it to listen on all available network interfaces.

### Problem 3: Server Crashing on Startup

- **Symptom**: The server process was starting but then immediately disappearing. `curl` and `ss` commands confirmed it was not staying active.
- **Reason**: Running the server in the foreground (`streamlit run app.py` without `&`) revealed that Streamlit was showing a one-time interactive prompt asking for an email. In the background, this prompt could not be answered, causing the server to hang and exit.
- **Solution**: Restarted the server with the `--server.headless=true` flag. This tells Streamlit it's in a non-interactive environment and suppresses such prompts.

### Problem 4: Persistent `localhost refused to connect` Error

- **Symptom**: Despite the server running correctly, the user still reported a `localhost refused to connect` error.
- **Reason**: This specific error message confirmed the user was typing `localhost` in their host browser, not the VM's IP address (`192.168.56.101`). Further investigation revealed they were also omitting the `http://` prefix, causing the browser to treat the IP address as a search query.
- **Solution**: Provided explicit instructions to type the **full URL** (`http://192.168.56.101:8501`) into the browser's address bar.

### Problem 5: Final Network Blockage

- **Symptom**: Even with the correct full URL, the connection timed out. The server was verified to be running and listening on `0.0.0.0`.
- **Reason**: This pointed to a network configuration issue within VirtualBox itself. The default **NAT** network mode prevents direct access from the host to the guest's IP address.
- **Solution**: Instructed the user to set up **Port Forwarding** in the VM's network settings. A rule was added to forward traffic from the host's port `8501` to the guest's port `8501`.

### Final Success

After setting up port forwarding, the user was finally able to access the application from their **host machine's browser** by navigating to **`http://localhost:8501`**.

### Key Takeaways

1.  Always use a virtual environment for Python projects.
2.  When hosting services in a VM, ensure the server binds to `0.0.0.0` to be accessible externally.
3.  Use `--server.headless=true` when running Streamlit in automated or non-interactive environments.
4.  The default **NAT** mode in VirtualBox requires **Port Forwarding** to expose services to the host machine.
