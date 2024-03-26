import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Run llama 2 model for given input
def run_llama(blog_topic, nb_words, blog_style):
  # Load the model
  llma_model = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                             model_type='llama',
                             config={'max_new_tokens':256,'temperature':0.01})
  
  # Create the prompt
  template = """
        Write a blog for {blog_style} job profile for a topic {blog_topic}
        within {nb_words} words.
         """
  prompt = PromptTemplate(input_variables=["blog_style","blog_topic","nb_words"],
                          template=template)

  # Run the model
  print("Model running")
  output = llma_model(prompt.format(blog_style=blog_style, blog_topic=blog_topic, nb_words=nb_words))
  print(output)
  return output


st.set_page_config(page_title="Blog Generator",
                    page_icon='🚀',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Blog Generator")

blog_topic = st.text_input("What is your blog topic?")


col1,col2 = st.columns([5,5])

with col1:
    nb_words = st.text_input('Number of words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Domain Experts','Adults','Childrens'),index=0)
    
submit=st.button("Generate")

# Display answer
if submit:
    st.write(run_llama(blog_topic, nb_words, blog_style))