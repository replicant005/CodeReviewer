from LLM.llm_client import call_llm
from LLM.prompts import security_prompt
from pydantic import BaseModel
from typing import Optional

# pydantic schema for
class AnalyzeInput(BaseModel):
    code: Optional[str] = None
    file_path: Optional[str] = None
 

def analyze_code(input: AnalyzeInput):
    code = input.code
    file_path = input.file_path

    # If file path is given, read the file
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
        except Exception as e:
            return f"Could not read file: {e}"

    if not code:
        return "No code provided. Pass `code` or `file_path`."
    prompt = security_prompt(code , file_path)
    result = call_llm(prompt)
    print("MCP TOOL CALLED")
    return result 