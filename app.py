import streamlit as st
import subprocess
import os
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Cloud Infrastructure Setup ---
# This ensures Java is ready to go as soon as the website loads
if not os.path.exists("src/FileCipher.class"):
    subprocess.run(["javac", "src/FileCipher.java"])

# Initialize Session Memory (keeps data alive during your visit)
if 'current_key' not in st.session_state:
    st.session_state.current_key = None
if 'encrypted_hex' not in st.session_state:
    st.session_state.encrypted_hex = None

# --- 2. Helper Functions ---
def get_hex_dump(data):
    return " ".join(f"{b:02x}" for b in data).upper()

# --- 3. Page UI ---
st.set_page_config(page_title="CipherStream Pro", layout="wide", page_icon="🛡️")
st.title("🛡️ CipherStream Pro: Live Universal Vault")
st.markdown("---")

# Sidebar: Key & Session Management
with st.sidebar:
    st.header("Key Management")
    if st.button("Generate New Security Key"):
        subprocess.run(["java", "-cp", "src", "FileCipher", "generate-key"])
        if os.path.exists("vault.key"):
            with open("vault.key", "r") as f:
                st.session_state.current_key = f.read()
            st.success("New Key Generated!")

    if st.session_state.current_key:
        st.info("Key Active in Session")
        st.download_button(
            "Download vault.key",
            data=st.session_state.current_key,
            file_name="vault.key",
            help="Download this to your computer! It will vanish when you close this tab."
        )
    else:
        st.warning("No key found. Generate one to start.")

# Main Interface: Encryption
st.subheader("Secure Messaging")
message = st.text_area("Enter your message (Supports Emojis and Symbols):")

if st.button("Lock Vault"):
    if not st.session_state.current_key:
        st.error("Please generate a Security Key in the sidebar first!")
    elif not message.strip():
        st.warning("Please enter a message.")
    else:
        # Save temporary file for Java
        with open("plain.txt", "w", encoding="utf-8") as f:
            f.write(message)
        
        with st.spinner("Securing your data..."):
            subprocess.run(["java", "-cp", "src", "FileCipher", "encrypt"])
        
        st.toast("Vault Secured!", icon="🛡️")
        
        with open("encrypted.txt", "rb") as e:
            encrypted_data = e.read()
            st.session_state.encrypted_hex = get_hex_dump(encrypted_data)
            
        col_hex, col_stats = st.columns(2)
        with col_hex:
            st.subheader("Digital Fingerprint")
            st.code(st.session_state.encrypted_hex, language=None)
            st.download_button("Download message.enc", data=encrypted_data, file_name="message.enc")

        with col_stats:
            st.subheader("Vault Health Check")
            byte_list = list(encrypted_data)
            df = pd.DataFrame(byte_list, columns=['Byte Value'])
            counts = df['Byte Value'].value_counts().sort_index()
            
            fig, ax = plt.subplots()
            counts.plot(kind='bar', ax=ax, color='#4F8BF9')
            ax.set_xlabel("Unique Digital Patterns")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

# Decryption Section
st.divider()
st.subheader("Unlock an Existing Vault")
st.caption("Upload your files to restore the original message.")

col_up1, col_up2 = st.columns(2)
with col_up1:
    up_key = st.file_uploader("Upload 'vault.key'", type=["key", "txt"])
with col_up2:
    up_enc = st.file_uploader("Upload 'message.enc'", type=["enc", "txt"])

if st.button("Restore Original Message"):
    if up_key and up_enc:
        with open("vault.key", "wb") as f:
            f.write(up_key.getbuffer())
        with open("encrypted.txt", "wb") as f:
            f.write(up_enc.getbuffer())
            
        subprocess.run(["java", "-cp", "src", "FileCipher", "decrypt"])
        
        with open("decrypted_result.txt", "r", encoding="utf-8", errors="ignore") as d:
            decoded_msg = d.read()
            
        st.success("Vault Unlocked!")
        st.text_area("Decrypted Content:", value=decoded_msg, height=100)
    else:
        st.warning("Please upload both files.")