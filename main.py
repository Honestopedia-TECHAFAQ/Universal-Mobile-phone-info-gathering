import streamlit as st
import requests

def retrieve_phone_model(model):

    return model  

def detect_os(os):
    return os 

def assess_storage(storage):
    return storage  

def main():
    st.title("Mobile Phone Information Retrieval")
    
    model = st.text_input("Enter Phone Model")
    os = st.selectbox("Select Operating System", ["Android", "iOS"])
    storage = st.number_input("Enter Storage Capacity (GB)")

    if st.button("Retrieve Information"):
        retrieved_model = retrieve_phone_model(model)
        detected_os = detect_os(os)
        assessed_storage = assess_storage(storage)

        st.write("### Information Retrieved:")
        st.write(f"- Phone Model: {retrieved_model}")
        st.write(f"- Operating System: {detected_os}")
        st.write(f"- Storage Capacity: {assessed_storage} GB")

if __name__ == "__main__":
    main()
