from fastmcp import FastMCP
from tools.analyze_code import analyze_code as analyze_code_impl, AnalyzeInput
mcp = FastMCP("codeGuard")

@mcp.tool()
def analyze(input: AnalyzeInput):
    """Analyze code for vulnerabilities"""
    return analyze_code_impl(input)


if __name__ == "__main__":
    mcp.run()