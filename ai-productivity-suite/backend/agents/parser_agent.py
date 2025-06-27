from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate
from utils.config import Config
import json

def parse_email(email_body):
    config = Config()
    llm = LlamaCpp(
        model_path=f"../../models/{config.LLM_MODEL}",
        temperature=0.1,
        n_ctx=2048
    )
    
    prompt = PromptTemplate.from_template("""
    Extract tasks from this email:
    {email_text}
    
    Output JSON: {{"tasks": [{{"type": "book|pay|schedule", ...}}]}}
    """)
    
    chain = prompt | llm
    result = chain.invoke({"email_text": email_body})
    
    try:
        json_start = result.find('{')
        json_end = result.rfind('}') + 1
        return json.loads(result[json_start:json_end])
    except json.JSONDecodeError:
        return {"tasks": []}