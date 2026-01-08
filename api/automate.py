
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from playwright.sync_api import sync_playwright
from s.blogspot import Blogger
from s.ai_generate import gen_content
from s.data import save_data


def run_automation():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="chrome_data",
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
            headless=False,
        )
        page = context.new_page()
        content = gen_content()
        page.goto("https://blogger.com")
        blogger = Blogger(page=page)
        
        login_spy_element = page.locator('h2:has-text("Publish your passions, your way")')
        if login_spy_element.count() > 0:
            blogger.login()
       
        blogger.create_post(content)
        save_data(content)
        
        

