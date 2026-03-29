# CipherStream Pro: Universal Byte-Level Vault

**CipherStream Pro** is a hybrid cryptographic application that bridges **Java's high-performance backend** with a **Streamlit Data Science frontend**. Unlike standard ciphers that only handle English text, this "Universal Vault" uses byte-level manipulation to secure anything from simple sentences to complex emojis and multi-language scripts.


## Key Features
* **Hybrid Architecture:** Seamless integration between Python (UI) and Java (Encryption Engine) using the JVM Bridge.
* **Universal Compatibility:** Uses **Modulo 256** byte-shifting, allowing support for Emojis 🚀, symbols, and non-English characters.
* **Security Analytics:** Built-in **Frequency Analysis** dashboard to visualize the statistical distribution of encrypted data.
* **Physical Key Infrastructure:** Generates unique `.key` files, mimicking real-world two-factor authentication.
* **Hexadecimal Inspection:** View the "Digital Fingerprint" of your data at the lowest machine level.


## Technical Architecture
The project follows a modular design to ensure high performance and clean UI:

1.  **Frontend (Python):** Streamlit handles the user interface, session memory, and data visualization (Pandas/Matplotlib).
2.  **Bridge (Subprocess):** Python executes Java commands in the background to process files without blocking the UI.
3.  **Backend (Java):** A robust `FileCipher` engine that performs raw byte-stream transformations for maximum security.




## Getting Started

### Prerequisites
* **Java JDK** (version 8 or higher)
* **Python 3.8+**
* **Libraries:** `pip install streamlit pandas matplotlib`

### Installation & Usage
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/CipherStream-Pro.git](https://github.com/your-username/CipherStream-Pro.git)
    cd CipherStream-Pro
    ```
2.  **Compile the Engine:**
    ```bash
    javac src/FileCipher.java
    ```
3.  **Launch the App:**
    ```bash
    streamlit run app.py
    ```

## Data Science in Security
This project goes beyond coding by providing **Security Audits**. By analyzing the frequency of byte occurrences, users can observe the "Entropy" of the cipher. 



* **Observation:** A more uniform distribution in the bar chart indicates a stronger scramble.
* **Methodology:** Every character is mapped to an 8-bit value (0-255) and shifted using a randomly generated secret key.




## Future Roadmap
* Upgrade to **AES-256** Symmetric Encryption for banking-grade security.
* Integrate **Biometric Authentication** using Python's OpenCV for vault access.
* Cloud-based Key Management using **Google Firestore** or **Supabase**.


**Developed by Sharmila | MCA Data Science**
