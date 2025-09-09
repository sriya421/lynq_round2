import os
from dotenv import load_dotenv
from google import genai 
from pypdf import PdfReader # pyright: ignore[reportMissingImports]
import streamlit as st

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="PDF Analyzer", page_icon="📄")
st.title("📄 PDF Reader & Analyzer")

#file upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file is not None:
    # Create a PdfReader object by opening the PDF file in binary read mode ('rb')
    reader = PdfReader(uploaded_file)

    # Get the total number of pages
    number_of_pages = len(reader.pages)
    print(f"Total number of pages: {number_of_pages}")

    # Extract text from the page
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
            #print(f"Text from page:{text}")
        st.success("✅ PDF uploaded and text extracted!")

# Initialize the client
client = genai.Client(api_key=api_key)

# Send a simple prompt
user_prompt = st.text_input("Ask a question about this PDF:")
if user_prompt:
# Build prompt (limit text so it fits model input size)
    prompt = f"""
    You are an AI PDF analyzer. Here is the document content
    (truncated to first 6000 characters to fit input limit):

    {text[:6000]}

    Based on this document, answer the following question:
    {user_prompt}
    """
    #connect prompt to gemini

    response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=prompt
    )

    #print(response.text)
    st.subheader("🤖 Gemini says:")
    st.write(response.text)
