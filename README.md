# CipherStream-J-Live
### *Bridging Java’s Robustness with Python’s Agility*

**CipherStream J-Live** is a personal privacy tool designed to keep your digital notes secure. Developed as part of an MCA Data Science journey, this project moves away from "black box" security and brings the encryption process to life through a modern web interface.

---

## The Vision
Most encryption tools are either too complex for everyday use or too hidden in a terminal for a user to understand. **CipherStream** changes that by providing:
* **Visual Feedback:** See your message transform into a secret code in real-time.
* **Hybrid Power:** The speed and safety of **Java** combined with the intuitive interface of **Streamlit**.
* **Total Privacy:** Your data never leaves your computer. No cloud, no tracking—just local, mathematical security.

---

## How it Works
The application functions as a conversation between two different programming worlds:

1.  **The Interface (Python):** Collects your private thoughts and your "Secret Shift Key."
2.  **The Bridge (Subprocess):** Python securely passes these instructions to the Java Virtual Machine.
3.  **The Engine (Java):** Our "Brain" processes the text using a custom **Modulo 26** algorithm, ensuring that every letter wraps perfectly from Z back to A.
4.  **The Vault (Local I/O):** The results are saved as physical files on your machine, which you can download and keep.

---

## Getting Started

### Prerequisites
* **Java JDK 17+** (The Engine)
* **Python 3.10+** (The Interface)

### Installation & Launch
1.  **Compile the Java Engine:**
    ```bash
    javac src/FileCipher.java
    ```
2.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch the App:**
    ```bash
    streamlit run app.py
    ```

---

## Technical Milestones
Building this project was a deep dive into the fundamentals of software engineering:
* **Interoperability:** Managing cross-language communication between Python and Java.
* **Data Integrity:** Using `FileInputStream` and `FileOutputStream` to ensure byte-perfect data handling.
* **Human-Centered Design:** Crafting an interface that makes complex math feel like a simple "Lock & Key" experience.

---

## Future Roadmap
* **Phrase-Based Keys:** Moving from numbers to "Secret Passwords."
* **Image Encryption:** Applying the same logic to protect visual data.
* **Advanced Algorithms:** Implementing AES-256 for industrial-grade security.

---

**Developed as part of the MCA Data Science curriculum.**
