# CipherStream Pro: Byte-Level Vault

**CipherStream Pro** is a hybrid cryptographic application that bridges a **Java backend** with a **Streamlit frontend**. Unlike basic ciphers that only handle English text, this "Universal Vault" works at the byte level, so it can process simple sentences, emojis, and multi-language scripts.

**Live demo:** [CipherStream Pro on Streamlit](https://cipherstream-pro-5uqutxcjur3ifz9mbircs3.streamlit.app/)

> **Note:** This is an educational project. A byte-shift cipher is not secure by modern standards, so do not use it to protect sensitive data.

## Key Features

- **Hybrid architecture:** A Python (Streamlit) interface calls a Java encryption engine.
- **Universal compatibility:** Modulo 256 byte-shifting supports emojis 🚀, symbols, and non-English characters.
- **Frequency analysis dashboard:** Plots how often each byte value occurs in the encrypted data.
- **Key files:** Generates a unique `.key` file that is used to encrypt and decrypt your data.
- **Hexadecimal view:** Shows the raw bytes of your data in hexadecimal.

## Tech Stack

- **Java:** the `FileCipher` encryption engine
- **Python:** the application and interface
- **Streamlit:** the web interface and session handling
- **Pandas and Matplotlib:** the frequency analysis charts

## How It Works

1. **Frontend (Python):** Streamlit handles the interface, session state, and charts.
2. **Bridge (subprocess):** Python runs the Java program in the background, so the interface stays responsive while files are processed.
3. **Backend (Java):** The `FileCipher` engine transforms the raw byte stream.

## Getting Started

### Prerequisites

- Java JDK 8 or higher
- Python 3.8 or higher

### Installation

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

Streamlit prints a local address (usually `http://localhost:8501`). Open it in your browser.

## Project Files

| File | Purpose |
| --- | --- |
| `app.py` | The Streamlit application |
| `src/FileCipher.java` | The Java encryption engine |
| `requirements.txt` | Python dependencies |
| `packages.txt` | System packages for the hosted demo |

## Frequency Analysis

The dashboard counts how often each byte value (0 to 255) appears in the encrypted data, so you can compare the result with the original. Every character is mapped to an 8-bit value and shifted using a randomly generated secret key.

## Future Scope

- Upgrade to AES-256 symmetric encryption
- Add biometric authentication with OpenCV for vault access
- Store keys in the cloud with Google Firestore or Supabase

---

Developed by Sharmila | MCA Data Science
