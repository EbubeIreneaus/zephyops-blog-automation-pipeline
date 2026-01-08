from google import genai
from dotenv import load_dotenv
from .data import fetch_data
import re
import json

load_dotenv()

client = genai.Client()

titles = fetch_data()


def gen_content():
    prompt = f"""
Role:
You are a senior business operator and content strategist focused on ai automation, systems design, and long-term business performance.

Task:
You will receive a list of previously used blog titles.
1. Analyze them to identify themes already covered.
2. Generate ONE new blog post with a clearly different strategic angle (no overlap in idea, framing, or keyword focus).

Angle Guidance:
Choose ONE fresh lens such as ROI, risk reduction, operational scalability, decision-making systems, organizational resilience, or future-proofing.
Avoid generic automation benefits.

Tone Rules:
- Write like an experienced operator explaining ideas to busy founders
- Plain English, short sentences
- Practical and concrete, not academic
- No consultant or marketing jargon

Output Format (STRICT – return ONLY JSON):

  "title": "string",
  "content": "HTML",
  "meta_description": "string"

Content Rules:
- Original, business-focused, insightful
- Explain automation with real-world business logic
- Content should be 500 words minimum
- Emphasize long-term impact and measurable outcomes
- Human-friendly and direct

HTML Rules:
- Valid HTML only
- Use <h1>, <h2>, <p>, <ul>, <strong>
- Include EXACTLY ONE <img> tag
- Place image immediately after <h1>

Image Rules (STRICT):
- Image MUST be a direct, publicly accessible image file from Unsplash.
- Selection Logic: Pick ONE Image ID from the "Approved List" below that best fits the blog title. If none fit perfectly, pick any one from the list.
- URL(src) Format: Use exactly: https://images.unsplash.com/[imageId] (no commas or extra characters).
- Use descriptive, SEO-optimized alt text

Approved Image ID List:
1. photo-1504384308090-c894fdcc538d (Data & Cloud)
2. photo-1518770660439-4636190af475 (Logic/Circuits)
3. photo-1498050108023-c5249f4df085 (Code/Automation)
4. photo-1531297484001-80022131f5a1 (Future/Office)
5. photo-1550751827-4bd374c3f58b (Futuristic Interface & AI)
6. photo-1451187580459-43490279c0fa (Digital Connectivity & Network)

SEO Rules:
- Unique, keyword-optimized title
- Meta description 150–160 characters
- Natural keyword usage
- Clear, skimmable structure

Restrictions:
- Do NOT reference AI tools, prompts, or models
- Do NOT add explanations or text outside the JSON
- Ensure the topic is clearly distinct from previous titles

Previously Used Blog Titles:
{titles}
"""

    response = client.models.generate_content(
        model='gemini-2.5-flash-lite', contents=prompt
    )
    clean_response =re.sub(r"```[a-zA-Z]*\n?|```", "", response.text).strip()
  
    return json.loads(clean_response)