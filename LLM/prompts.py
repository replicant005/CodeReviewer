def security_prompt(code : str, file_path : str | None = None):
    return f"""
You are a senior security engineer.

Analyze the following code for:

File: {file_path or "unknown"}

- SQL injection
- hardcoded secrets
- unsafe authentication
- command injection
- insecure coding practices

Return a short report.

Code:
{code}
"""
def security_prompt(code : str, file_path : str | None = None):
    return f"""
You are a senior security engineer.

Analyze the following code for:

File: {file_path or "unknown"}

- SQL injection
- hardcoded secrets
- unsafe authentication
- command injection
- insecure coding practices

Return a short report.

Code:
{code}
"""