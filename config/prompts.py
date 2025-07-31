SCAN_REPORT_PROMPT = """Analyze these vulnerability scan results and generate a comprehensive security report:
{scan_results}

Include:
1. Executive summary
2. Critical vulnerabilities with CVSS scores
3. Recommended remediation steps
4. Long-term security recommendations

Format as markdown with proper headings."""

SCAN_TEMPLATES = {
    "web": "nmap -sV -T4 -Pn --script vuln {target}",
    "api": "nmap -sV -T4 -Pn -p 80,443,8080 --script http-vuln* {target}"
}
