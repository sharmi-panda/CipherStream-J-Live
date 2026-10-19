# Getting started

By the end of this guide, you will have CipherStream Pro running in your browser.

## Before you begin

You need:

- Java JDK 8 or higher
- Python 3.8 or higher

## Install and run

1. Clone the repository and open the folder:

    ```bash
    git clone https://github.com/sharmi-panda/CipherStream-J-Live.git
    cd CipherStream-J-Live
    ```

2. Install the Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Compile the Java engine:

    ```bash
    javac src/FileCipher.java
    ```

4. Start the app:

    ```bash
    streamlit run app.py
    ```

5. Open the address that Streamlit prints in the terminal, usually `http://localhost:8501`.

You should see the CipherStream Pro interface in your browser.
