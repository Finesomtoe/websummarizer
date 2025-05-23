import streamlit as st
from websummarizer import ReadersDigest

# Configure the page
st.set_page_config(
    page_title="Website Summarizer",
    page_icon="📚",
    layout="centered"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2e4057;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Website Summarizer 📚")

# Add a brief description
st.markdown("Enter a URL below to get a concise summary of any web page.")

# Improve input field
url = st.text_input("Website URL", placeholder="https://example.com")

# Add a loading spinner
if st.button("Generate Summary 🔄"):
    if url:
        with st.spinner('Analyzing website content...'):
            try:
                digest = ReadersDigest(url)
                summary = digest.summarize(digest)
                
                # Display summary in a nice box
                st.success("Summary Generated!")
                st.markdown("### Summary")
                st.markdown(f">{summary}")
                
                # Display metrics in a more visual way
                st.markdown("### Statistics")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Original Length", f"{len(digest.text):,} chars")
                with col2:
                    st.metric("Summary Length", f"{len(summary):,} chars")
                with col3:
                    reduction = round((1 - len(summary)/len(digest.text)) * 100)
                    st.metric("Reduction", f"{reduction}%")
                
                st.markdown("---")
                st.markdown("*✨ Summary generated using advanced NLP techniques*")
            except Exception as e:
                st.error(f"Error: Unable to process the URL. Please check if it's valid and try again.")
    else:
        st.warning("⚠️ Please enter a URL to generate a summary")
