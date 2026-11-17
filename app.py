#import necessary modules
import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_Key import api_Key
#configure genai with api key
genai.configure(api_key =api_Key)
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
# apply safety settings
safety_settings = [
    {
        "category": "HARM_ CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold":"BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category":"HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold":"BLOCK_MEDIUM_AND_ABOVE"
        
    },
]


system_prompt = """
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Responsibilities include:
1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Suggest further tests or treatments if applicable.
4. Treatment Suggestions: Recommend possible treatment options if appropriate.

Important Notes:
- Only respond if the image pertains to human health issues.
- Mention if the image quality impedes analysis.
- Include the disclaimer: "Consult with a doctor before making any decisions."

Please provide me an output response with these 4 headings Detailed Analysis,Finding Report,Recommendation  and Next Steps, Treatment Suggestions
"""




#model configuration
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)



#set the page configuration
st.set_page_config(page_title="vitalImage Analysis,p",page_icon=":robot")


#set the title
st.title("👩🏻‍⚕️Vital Image Analytics 📈")

st.subheader("An application that can help users to identify medical images")
uploaded_file = st.file_uploader("Upload the medical image for analysis",type=["png","jpg","jpeg"])
if uploaded_file :
    st.image(uploaded_file,width=300,caption="Uploaded  Medical Image")
submit_button = st.button("Generate the Analysis")

if submit_button:
    #process the uploaded image
    image_data=uploaded_file.getvalue()

# making our image ready
    image_parts = [
        {
            "mime_type":"image/jpeg",
            "data":image_data
        },
    ]
    #making our prompt ready
    prompt_parts= [

        image_parts[0],
        system_prompt,
        
         ]
    #Generate a response based on prompt and Image

    st.image(image_data,width=250)
    response =model.generate_content(prompt_parts)
    if response:
        st.title("Here is  the analysis based on your image : ")
    st.write(response.text)



