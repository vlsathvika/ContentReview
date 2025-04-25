import subprocess
import os
import streamlit as st
import importlib.util
import sys

repo_path = 'content_review_agent'
app_module_path = os.path.join(repo_path, 'app.py')

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

# Now, try to import and run the app inside content_review_agent
if os.path.exists(app_module_path):
    spec = importlib.util.spec_from_file_location("content_review_agent_app", app_module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["content_review_agent_app"] = module
    spec.loader.exec_module(module)
    
    # Now call the main function if it exists
    if hasattr(module, 'main'):
        module.main()  # <-- CALL the main() of content_review_agent/app.py
    else:
        st.error("No 'main()' function found in content_review_agent/app.py")
else:
    st.error("app.py not found inside content_review_agent.")
