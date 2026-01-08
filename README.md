# AI Blogpost Content Automation Pipeline (Google Blogger)

An end-to-end AI-powered automation pipeline that **generates blog content and automatically publishes it to Google Blogger (blogspot.com)** without manual intervention.

This system is designed for **speed, consistency, and scale**, enabling content creators and businesses to publish high-quality blog posts on autopilot.

---

## 🚀 What This Project Does

This automation pipeline:

1. Generates blog content using AI
2. Extracts structured content from the AI response
3. Stores the generated data for tracking and reuse
4. Automatically logs into Blogger
5. Creates and publishes a blog post programmatically

---

## 🧠 AI Content Structure

Each AI-generated response returns structured data in the following format:

- **Title**: `string`
- **Content**: `HTML`
- **Meta Description**: `string`

This structure ensures the content is:
- SEO-ready
- Directly publishable
- Easy to store and reuse

---

## 🔧 Tech Stack & Tools

### 🤖 LLM
- **Google Generative AI (Google Gen AI)**

### 🛠 Automation & Scraping
- **Playwright** – Browser automation for Blogger interactions
- **BeautifulSoup** – HTML parsing and validation
- **Xvfb** – Headful browser execution in serverless environments

### 📊 Data Storage
- **Google Sheets (Excel App Script API)**  
  Used to store:
  - AI-generated titles
  - HTML content
  - Meta descriptions
  - Publishing status

### ⏱ Scheduling
- **Cron Jobs** – Automated scheduling for content generation and posting

---

## ⚙️ How the Pipeline Works

1. **Cron Scheduler triggers the automation**
2. **Google Gen AI generates blog content**
3. **Response is parsed into structured fields**
4. **Data is saved to Google Sheets**
5. **Playwright launches a browser session**
6. **Automation logs into Blogger**
7. **Title, HTML content, and meta description are injected**
8. **Blog post is published automatically**

---

## ✅ Problems This Automation Solves

- Manual content writing
- Repetitive blog publishing tasks
- Human error during posting
- Inconsistent publishing schedules
- Poor scalability for content marketing

---

## 🎯 Use Cases

- SEO content automation
- Blogger-based niche sites
- Programmatic content marketing
- Solo founders & small teams
- AI-driven blogging systems

---

## 📌 Key Benefits

- Fully automated blogging workflow
- SEO-friendly structured output
- Serverless-compatible headful UI automation
- Centralized content tracking
- Scalable and repeatable publishing process

---

## 📄 License

This project is for educational and internal automation use.  
Modify and extend responsibly.

---

## 👤 Author

**Ebube Ireneaus**  
AI Automation & Workflow Engineering  
SEO-focused systems for scalable growth
