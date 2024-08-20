import streamlit as st
import pprint
import google.generativeai as palm

palm.configure(api_key='your api key here')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

# Streamlit app
st.title("BUG TRACKER")

# User inputs
input_code = st.text_input("Show me your code")
error = st.text_input("Whats the error message")

prompt = """
I have coded a specific program and
I seem to have got an error while coding it

CODE:\n"""+input_code+"""\nERROR:\n"""+error+"""

Can you give an error Explanation?
Can you Suggest possible Fixes?
Can you Give the corrected code?
"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

#display it to screen
output = completion.result

if (st.button("Debug")):
    st.write(output)
