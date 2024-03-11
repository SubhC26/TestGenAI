from openai import OpenAI
import streamlit as st
 
clt = OpenAI(api_key="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")
 
def main():
  st.title("Article Writer")
  notes = st.text_area("Enter topic information")
  content = "I want you to write short literature review")
  if st.button("GeneratingArticle"):
    with st.spinner("GeneratingArticle..."):
      response=clt.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{'role':'user','content':content}]
      )
      description=response.choices[0].message.com
      st.subheader("Generated Writeup:")
      st.write(description)
if__name__=='__main__':
  main()
