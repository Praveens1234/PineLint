import streamlit as st
import json
from pinelint.lexer import Lexer
from pinelint.parser import Parser, ParseError
from pinelint.semantic import SemanticAnalyzer
from pinelint.rules import RuleEngine
from pinelint.diagnostics import DiagnosticManager, ReportFormat

st.set_page_config(page_title="PineLint", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for Hyper Modern Glassy Look ---
st.markdown("""
<style>
    /* Global Reset & Dark Theme Base */
    .stApp {
        background: #0e1117;
        background-image: radial-gradient(circle at 10% 20%, rgba(37, 38, 44, 0.4) 0%, transparent 20%),
                          radial-gradient(circle at 90% 80%, rgba(37, 38, 44, 0.4) 0%, transparent 20%);
        font-family: 'Inter', sans-serif;
        color: #e0e0e0;
    }

    /* Glassmorphism Cards */
    .css-1r6slb0, .stTextArea, .stSelectbox {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Header Styling */
    h1 {
        font-weight: 700;
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(14, 17, 23, 0.9);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Buttons (Neon Accent) */
    .stButton > button {
        background: linear-gradient(45deg, #2196F3, #21CBF3);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px rgba(33, 150, 243, 0.5);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 20px rgba(33, 150, 243, 0.7);
    }

    /* Text Area */
    .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.3);
        color: #00ffcc; /* Cyberpunk code color */
        border: 1px solid rgba(255, 255, 255, 0.1);
        font-family: 'Fira Code', monospace;
    }

    /* Diagnostics Cards */
    .diagnostic-card {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid;
        border-radius: 4px;
        padding: 10px;
        margin-bottom: 10px;
        backdrop-filter: blur(5px);
    }
    .diagnostic-error { border-color: #ff4b4b; box-shadow: 0 0 5px rgba(255, 75, 75, 0.2); }
    .diagnostic-warning { border-color: #ffa726; box-shadow: 0 0 5px rgba(255, 167, 38, 0.2); }
    .diagnostic-info { border-color: #29b6f6; }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0e1117;
    }
    ::-webkit-scrollbar-thumb {
        background: #333;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 4])

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png", width=50) # Placeholder logo
    st.markdown("### PineLint")
    st.caption("v0.2.0-beta")
    st.divider()
    
    version_override = st.selectbox("Pine Version", ["Auto", "v5", "v6"])
    output_fmt = st.selectbox("Output Format", ["Text", "JSON"])
    
    st.info("💡 **Pro Tip:** Use `cmd+enter` to run analysis quickly.")

with col2:
    st.title("Static Code Analysis")
    st.markdown("Professional validation for TradingView strategies and indicators.")

    default_code = """//@version=5
indicator("My Script", overlay=true)

// Example: User-Defined Function
f(x) => x * 2

// Example: Switch
string col = switch
    close > open => "green"
    => "red"

plot(f(close), color=color.new(col, 0))
"""
    source_code = st.text_area("Source Code", value=default_code, height=400, label_visibility="collapsed", placeholder="Paste your Pine Script code here...")

    col_act, col_res = st.columns([1, 5])
    with col_act:
        analyze_btn = st.button("ANALYZE CODE")

    if analyze_btn:
        diagnostics = DiagnosticManager()
        
        # 1. Lexer
        try:
            lexer = Lexer(source_code, diagnostics)
            tokens = lexer.tokenize()
            
            # 2. Parser
            if not diagnostics.has_errors():
                parser = Parser(tokens, diagnostics)
                script = parser.parse()
                
                # 3. Semantic & Rules
                if not diagnostics.has_errors():
                    analyzer = SemanticAnalyzer(diagnostics)
                    if version_override != "Auto":
                        analyzer.version = int(version_override[1])
                        
                    analyzer.analyze(script)
                    
                    engine = RuleEngine(diagnostics)
                    engine.run(script, analyzer)

        except ParseError:
            pass # Diagnostics already populated
        except Exception as e:
            st.error(f"❌ Internal Tool Error: {str(e)}")
        
        # Results Display
        st.divider()
        if not diagnostics.has_errors() and not diagnostics.diagnostics:
            st.markdown("""
            <div style="background: rgba(0, 255, 127, 0.1); border: 1px solid #00ff7f; padding: 20px; border-radius: 10px; text-align: center;">
                <h3 style="color: #00ff7f; margin:0;">✅ Validation Successful</h3>
                <p style="color: #ccc; margin-top:5px;">No syntax or semantic errors found.</p>
            </div>
            """, unsafe_allow_html=True)
        
        if output_fmt == "JSON":
            report = diagnostics.generate_report(ReportFormat.JSON)
            st.json(report)
        else:
            if diagnostics.has_errors():
                st.markdown(f"### Found {sum(1 for d in diagnostics.diagnostics if d.severity.value == 'ERROR')} Errors")
            
            for d in diagnostics.diagnostics:
                color_class = "diagnostic-error" if d.severity.value == "ERROR" else "diagnostic-warning"
                icon = "🔴" if d.severity.value == "ERROR" else "⚠️"
                
                st.markdown(f"""
                <div class="diagnostic-card {color_class}">
                    <div style="display:flex; justify-content:space-between;">
                        <strong>{icon} {d.code}</strong>
                        <span style="opacity:0.6; font-family:monospace;">Ln {d.line}, Col {d.column}</span>
                    </div>
                    <div style="margin-top:5px; font-size:1.1em;">{d.message}</div>
                    {f'<div style="margin-top:8px; font-size:0.9em; opacity:0.8; padding-top:5px; border-top:1px solid rgba(255,255,255,0.1);">💡 {d.suggestion}</div>' if d.suggestion else ''}
                </div>
                """, unsafe_allow_html=True)

