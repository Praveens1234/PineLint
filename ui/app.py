import streamlit as st
import subprocess
import os
import tempfile
import json

st.set_page_config(page_title="PineLint", layout="wide")

st.title("🌲 PineLint - Pine Script Static Analyzer")

source_code = st.text_area("Paste your Pine Script here:", height=300)

if st.button("Check"):
    if source_code:
        # Save to temp file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".pine", delete=False) as tmp:
            tmp.write(source_code)
            tmp_path = tmp.name
        
        try:
            # Run pinelint
            result = subprocess.run(
                ["python3", "-m", "pinelint.cli", "check", tmp_path, "--format", "json"],
                capture_output=True,
                text=True
            )
            
            if result.stdout:
                try:
                    report = json.loads(result.stdout)
                    
                    col1, col2 = st.columns(2)
                    col1.metric("Errors", report["error_count"])
                    col2.metric("Warnings", report["warning_count"])
                    
                    if report["valid"]:
                        st.success("✅ No issues found!")
                    
                    for diag in report["diagnostics"]:
                        severity = diag["severity"]
                        msg = f"**[{diag['code']}]** {diag['message']} (Line {diag['location']['line']})"
                        if severity == "error":
                            st.error(msg)
                        elif severity == "warning":
                            st.warning(msg)
                        else:
                            st.info(msg)
                            
                except json.JSONDecodeError:
                    st.error("Failed to parse PineLint output.")
                    st.code(result.stdout)
            else:
                if result.returncode != 0:
                     st.error("PineLint execution failed.")
                     st.code(result.stderr)
                else:
                     st.success("No output (Success?)")
                
        finally:
            os.remove(tmp_path)
    else:
        st.warning("Please enter some code.")
