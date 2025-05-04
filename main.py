import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer

tokenizer = AutoTokenizer.from_pretrained("fdtn-ai/Foundation-Sec-8B")
model = AutoModelForCausalLM.from_pretrained("fdtn-ai/Foundation-Sec-8B", device_map='auto')

# Example: Matching CWE to CVE IDs
prompt="""which vulnerabilities did UNC5221 exploit?"""

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate the response
outputs = model.generate(
    inputs["input_ids"],
    max_new_tokens=3,
    do_sample=True,
    temperature=0.1,
    top_p=0.9,
)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
response = response.replace(prompt, "")
print(response)