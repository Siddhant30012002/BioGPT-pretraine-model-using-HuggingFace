from transformers.pipelines import pipeline
from transformers import set_seed,BioGptTokenizer,BioGptForCausalLM
import streamlit as st

model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
set_seed(42)

with st.form("Drug Information Form"):
    drug_name = st.text_input("Enter the name of drug which you wanna know about:")
    submit_button = st.form_submit_button("Let BioGPT Think")


if submit_button:
    if drug_name.strip():  
        prompt_structure = f"the {drug_name} is used in condition of"
        with st.spinner("Generating response... Please wait."):
            predicted_op = generator(prompt_structure, max_length=50, num_return_sequences=1, do_sample=True, top_k=50, temperature=0.5)
        st.success("Response generated!")
        st.write("**BioGPT Response:**")
        st.write(predicted_op[0]['generated_text'])  
    else:
        st.error("Please enter a valid drug name.")

# with st.form("enter the name of drug which you want the  information about",clear_on_submit=False):
#     drug_name = st.text_input("enter the name of drug which you want the  information about")
#     prompt_structure = "the {} is used in condition of".format(drug_name)
#     st.write("")
#     st.write("")
    
#     submit_button = st.form_submit_button("let BioGPT Think")
#     predicted_op = generator(prompt_structure, max_length=50, num_return_sequences=1, do_sample=True, top_k=50, temperature=0.5)

#     if submit_button:
#         st.write(predicted_op)




