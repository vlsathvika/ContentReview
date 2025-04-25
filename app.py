import subprocess
import os
import sys
import streamlit as st
import importlib.util

repo_path = 'content_review_agent'
app_module_path = os.path.join(repo_path, 'app.py')

# Clone the repository only if it doesn't exist
if not os.path.exists(repo_path):
    token = st.secrets["GITHUB_TOKEN"]
    if token:
        repo_url = f"https://{token}@github.com/vlsathvika/content_review_agent.git"
        try:
            subprocess.run(['git', 'clone', repo_url, repo_path], check=True)
            st.success("Repository cloned successfully!")
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to clone repository: {e}")
    else:
        st.error("GITHUB_TOKEN is missing. Please add it to Streamlit Secrets.")

# 👉 Fix: Add repo_path to sys.path so imports like 'from utils.file_handler' work
if repo_path not in sys.path:
    sys.path.insert(0, repo_path)

# Import and run the app
if os.path.exists(app_module_path):
    spec = importlib.util.spec_from_file_location("content_review_agent_app", app_module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["content_review_agent_app"] = module
    spec.loader.exec_module(module)
    
    if hasattr(module, 'main'):
        module.main()
    else:
        st.error("No 'main()' function found in content_review_agent/app.py")
else:
    st.error("app.py not found inside content_review_agent.")
