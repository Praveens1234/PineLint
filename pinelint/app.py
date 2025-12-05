import streamlit as st
import traceback
from pinelint.lexer import Lexer, LexerError, TokenType
from pinelint.parser import Parser, ParseError
from pinelint.rules import RuleRunner
from pinelint.diagnostics import Severity

st.set_page_config(page_title="PineLint", layout="wide", page_icon="🌲")

# Sidebar
st.sidebar.title("🌲 PineLint")
st.sidebar.info("Static Analyzer for Pine Script v5/v6")
st.sidebar.markdown("---")
st.sidebar.markdown("**Settings**")
check_unused = st.sidebar.checkbox("Check Unused Variables", value=True)
check_shadowing = st.sidebar.checkbox("Check Shadowing", value=True)

st.title("PineLint - Code Quality Tool")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("### Source Code")
    code = st.text_area("Pine Script:", height=600, value="//@version=6\nindicator('My Script')\nvar int x = 10\nplot(close)")

with col2:
    st.markdown("### Analysis Report")
    
    if st.button("Run Analysis", type="primary", use_container_width=True):
        if not code.strip():
            st.warning("Enter code first.")
        else:
            with st.spinner("Analyzing..."):
                try:
                    lexer = Lexer(code)
                    tokens = lexer.tokenize()
                    
                    parser = Parser(tokens)
                    ast = parser.parse()
                    
                    # Parser Errors
                    if parser.errors:
                        st.error(f"Found {len(parser.errors)} syntax error(s).")
                        for e in parser.errors:
                            with st.expander(f"Line {e.line}: Syntax Error", expanded=True):
                                st.write(f"**Error**: {e}")
                    else:
                        runner = RuleRunner()
                        diagnostics = runner.run(code, ast, "editor.pine")
                        
                        # Filtering
                        filtered_diags = []
                        for d in diagnostics:
                            if d.code == "W002" and not check_unused: continue
                            if d.code == "W001" and not check_shadowing: continue
                            filtered_diags.append(d)
                            
                        errors = [d for d in filtered_diags if d.severity == Severity.ERROR]
                        warnings = [d for d in filtered_diags if d.severity == Severity.WARNING]
                        
                        # Stats
                        st.markdown("#### Statistics")
                        cols = st.columns(2)
                        cols[0].metric("Lines of Code", len(code.splitlines()))
                        # Function count approx
                        func_count = 0
                        # Check AST for FunctionDef if possible, or tokens
                        # AST root is list of statements.
                        if isinstance(ast, list):
                             # Recursive count?
                             pass
                        
                        cols[1].metric("Tokens", len(tokens))
                        
                        st.markdown("---")
                        
                        if errors:
                            st.error(f"❌ Found {len(errors)} Errors")
                            for d in errors:
                                st.error(f"**Line {d.line}**: {d.message}")
                                
                        if warnings:
                            st.warning(f"⚠️ Found {len(warnings)} Warnings")
                            for d in warnings:
                                st.warning(f"**Line {d.line}**: {d.message}")
                                if d.suggestion:
                                    st.info(f"💡 Suggestion: {d.suggestion}")
                                    
                        if not errors and not warnings:
                            st.success("✅ Clean Code! No issues found.")
                            
                except LexerError as e:
                    st.error(f"Lexer Error: {e}")
                except Exception as e:
                    st.error(f"Internal Error: {e}")
                    st.text(traceback.format_exc())
