from playwright.sync_api import sync_playwright, expect
import time

def verify_features(page):
    # Load app
    page.goto("http://localhost:8501")
    page.wait_for_timeout(5000)
    
    # Check for new UI elements
    # Title
    expect(page.get_by_role("heading", name="Static Code Analysis")).to_be_visible()
    
    # Check default code contains UDF
    text_area = page.locator("textarea")
    # Streamlit text area value might not be directly accessible via text_content, but let's try inputting something else to verify interaction
    # Actually, the default value should be processed if we click Analyze.
    
    # Click Analyze Code
    page.get_by_role("button", name="ANALYZE CODE").click()
    
    # Wait for results
    # We expect "Validation Successful" because the default code uses new features (UDF, Switch) which we just implemented parser support for.
    # If parser fails, we get errors.
    
    # Check for Success Card
    expect(page.locator("h3").filter(has_text="Validation Successful")).to_be_visible()
    
    # Screenshot
    page.screenshot(path="/home/jules/verification/new_ui_success.png")
    print("Screenshot saved.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_features(page)
        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="/home/jules/verification/new_ui_error.png")
            raise e
        finally:
            browser.close()
