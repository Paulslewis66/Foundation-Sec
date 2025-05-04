import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("fdtn-ai/Foundation-Sec-8B")
model = AutoModelForCausalLM.from_pretrained("fdtn-ai/Foundation-Sec-8B", device_map='auto')

st.title("Hugging Face Transformers Streamlit App")

# User input
user_input = st.text_input("Enter your query:")

if st.button("Generate Response"):
    if user_input:
        # Tokenize the input
        inputs = tokenizer(user_input, return_tensors="pt")

        # Generate the response
        outputs = model.generate(
            inputs["input_ids"],
            max_new_tokens=50,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
        )

        # Decode and display the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.replace(user_input, "")
        st.write("Response:", response)
    else:
        st.write("Please enter a query to generate a response.")