import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key ,openai_api_key
genai.configure(api_key=google_gemini_api_key)
from openai import OpenAI
client=OpenAI(api_key=openai_api_key)
from streamlit_carousel import carousel

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)



st.set_page_config(layout="wide")

st.title("💡🗓️🖊️ Blog Craft: Your AI  Writing Companion")

st.subheader("Now you can craft perfect blogs with the help of AI- Blogcraft is your new AI Blog Companion")

with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter details of the Blog that you want to generate")

    blog_title=st.text_input("Blog Title")

    keywords=st.text_area("Keywords (comma-seperated)")

    num_words=st.slider("Number of Words", min_value=250,max_value=1000,step=250)

    num_images=st.number_input("Number of Images",min_value=1,max_value=5,step=1)

    prompt_parts=[
        f"Generate a Comprehensive, engaging blog post relevant to the given title\"{blog_title}\" and keyword \"{keywords}\"Make sure to incorporate these keywords in the blog post. The Blog should be approximately {num_words} words in length, suitable for online audience . Ensure the content is original, Informative and maintains Consistent tone throughout"
    ]


    submit_button=st.button("Generate a Blog")

if submit_button:
    #st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhPYpCFIa-fNNmHVnZ0zTUd1V-hBICQE3p0w&s")

    response = model.generate_content(prompt_parts)
    image_urls = [
        "https://thumbs.dreamstime.com/b/earth-apocalypse-fire-ice-lightnings-elements-image-furnished-nasa-34500458.jpg",
        "https://thumbs.dreamstime.com/b/human-hands-holding-earth-planet-water-splashes-sunset-sky-background-ecology-concept-326013435.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4gSCtFyYVfsPDhR3WnbU50LTGsINAdPSF-A&s",
    ]

    #image_response = client.images.generate(
        #model="dall-e-3",
        #prompt="a white siamese cat",
        #size="1024x1024",
        #quality="standard",
        #n=1,
    #)

    #image_url=image_response.data[0].url

    #st.image(image_url,caption="Generated Image")

    # Adding images to the carousel
    carousel_images = [
        {"img": url, "caption": f"Image {i + 1}", "title": f"Image {i + 1}", "text": f"Description of Image {i + 1}"}for i, url in enumerate(image_urls)]

    # Display carousel
    carousel(carousel_images)


    st.title("YOUR BLOG POST:")

    st.write(response.text)