from playwright.sync_api import Page
import os


def fill_form(page: Page):
    email_field = page.get_by_role("textbox", name="Email or phone")
    email_field.press_sequentially(os.getenv('EMAIL_ADDR'))
    page.get_by_role("button", name="Next").click()
    page.wait_for_selector('h1:has-text("Welcome")', timeout=10000)
    psw_field = page.get_by_role("textbox", name="Enter your password")
    psw_field.press_sequentially(os.getenv("EMAIL_PASS"))
    page.get_by_role("button", name="Next").click()


class Blogger:
    def __init__(self, page: Page):
        self.page = page

    def login(self):
        page = self.page
        page.get_by_role("link", name="Sign in").first.click()
        h1_text = page.locator("h1").text_content()
        if h1_text == "Sign in":
            fill_form(page=page)
            page.get_by_role("link", name="Continue").click()
        else:
            email = page.get_by_role("link", name=f"{os.getenv("EMAIL_ADDR")}")
            if email.count() > 0:
                email.click()
            else:
                email = page.get_by_role("link", name="Use another account")
                email.click()
                page.wait_for_selector('h1:has-text("Sign in")', timeout=10000)
                fill_form(page=page)
                page.get_by_role("link", name="Continue").click()

    def create_post(self, content):
        page = self.page
        page.get_by_role("button", name="New post").first.click()
        title_field = page.get_by_role("textbox", name="Title")
        editor = page.locator(".CodeMirror")
        page.get_by_role('button', name="Search Description").click()
        search_desc_field = page.get_by_role("textbox", name="Enter search description")
        title_field.fill(content["title"])
        search_desc_field.fill(content["meta_description"])
        toggle = page.get_by_role("listbox", name="Toggle view")
        toggle.click()
        toggle.press("ArrowUp")
        toggle.press("Enter")
        cnt = content['content'].replace("\n\n", "<br />").strip()
        cnt = cnt.replace("\n", "").strip()
        editor.evaluate("(el, value)=> {el.CodeMirror.setValue(value);}", cnt
        )
        page.wait_for_timeout(10000)
        page.get_by_role('button', name="Publish").first.click()
        dialog = page.get_by_role("alertdialog")
        dialog.wait_for(state="visible")
        dialog.get_by_role("button", name="Confirm").click()
        page.wait_for_timeout(10000)