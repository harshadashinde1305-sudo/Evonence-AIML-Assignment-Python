Scenario 9: Gemini API (Structured JSON)
Python
import google.generativeai as genai
import json

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-pro")

def get_response():
    prompt = """
    List 3 benefits of Python for data science.
    Return only JSON:
    {"benefits": ["...", "...", "..."]}
    """
    
    response = model.generate_content(prompt)
    text = response.text.strip()
    
    try:
        return json.loads(text)
    except:
        start = text.find("{")
        end = text.rfind("}") + 1
        try:
            return json.loads(text[start:end])
        except:
            return {"error": "Invalid JSON", "raw": text}
