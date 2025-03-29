
import streamlit as st

def render_mermaid(mermaid_code: str):
    st.markdown(
        f"""
        <div class="mermaid">
        {mermaid_code}
        </div>
        <script type="module">
          import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
          mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        unsafe_allow_html=True
    )
