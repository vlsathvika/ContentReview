import os
import subprocess
import streamlit as st

repo_path = 'content_review_agent'

# Clone the repository only if it doesn't exist
if not os.path.exists(repo_path):
    token = os.getenv("GITHUB_TOKEN")
    if token:
        repo_url = f"https://{token}@github.com/vlsathvika/content_review_agent.git"
        try:
            subprocess.run(['git', 'clone', repo_url, repo_path], check=True)
            st.success("Repository cloned successfully!")
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to clone repository: {e}")
    else:
        st.error("GITHUB_TOKEN is missing. Please add it to Streamlit Secrets.")

# Execute the script
script_path = os.path.join(repo_path, 'persona_s.py')
if os.path.exists(script_path):
    try:
        exec(open(script_path).read())
    except Exception as e:
        st.error(f"Error while running the script: {e}")
else:
    st.error(f"{script_path} not found.")
