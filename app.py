import subprocess
import os
import streamlit as st

repo_path = 'content_review_agent'

# Clone the repository only if it doesn't exist
if not os.path.exists(repo_path):
    token = st.secrets["GITHUB_TOKEN"]  # Get the token from Streamlit Secrets
    if token:
        # Use token to access the private repository
        repo_url = f"https://{token}@github.com/vlsathvika/content_review_agent.git"
        try:
            subprocess.run(['git', 'clone', repo_url, repo_path], check=True)
            st.success("Repository cloned successfully!")
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to clone repository: {e}")
    else:
        st.error("GITHUB_TOKEN is missing. Please add it to Streamlit Secrets.")

