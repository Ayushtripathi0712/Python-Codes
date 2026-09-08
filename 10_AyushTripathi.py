"""
=====================================================================
EMAIL PATTERN FINDER USING REGULAR EXPRESSIONS
=====================================================================
A regular expression (regex) defines a search template describing
the structural shape of an email address:
[local part] + @ + [domain name] + . + [top-level domain/suffix]
=====================================================================
"""

import re

# =====================================================================
# 1. THE EMAIL PATTERN
# - Local part: [a-zA-Z0-9_.+-]+ allows letters, numbers, dots, hyphens, pluses
# - Separator: @
# - Domain label: [a-zA-Z0-9-]+ allows alphanumeric characters and hyphens
# - Extension: \.[a-zA-Z0-9.-]+ matches the dot and domain suffixes/subdomains
# =====================================================================
EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+"


# =====================================================================
# 2. FIND ALL EMAILS IN A BLOCK OF TEXT
# =====================================================================
def find_emails(text: str) -> list[str]:
    """Scans `text` and returns all matching email addresses."""
    return re.findall(EMAIL_PATTERN, text)


# =====================================================================
# 3. VALIDATE A SINGLE STRING AS AN EMAIL
# =====================================================================
def is_valid_email(candidate: str) -> bool:
    """Returns True only if the entire string matches the email pattern."""
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


# =====================================================================
# 4. DEMO / DRIVER CODE
# =====================================================================
if __name__ == "__main__":
    sample_text = """
    Please contact us for support:
    - General queries: support@examplecorp.com
    - Sales team: sales.team@business-hub.co.in
    - Personal note from Rahul (rahul_23@gmail.com) sent yesterday.
    - Invalid mentions: not-an-email, @missing-local.com, plain.text@
    - Newsletter sign-up: newsletter+promo@my-site.org
    """

    print("--- Original Text ---")
    print(sample_text.strip())

    print("\n--- Extracted Emails ---")
    found_emails = find_emails(sample_text)
    print(f"Found {len(found_emails)} email address(es):")
    for email in found_emails:
        print(f"  • {email}")

    print("\n--- Validation Test Cases ---")
    test_cases = [
        "john.doe@example.com",
        "invalid-email",
        "user@site",
        "user@site.com",
        "plain.text@",
        "a.b-c_d+e@sub.domain.co.in",
    ]

    for candidate in test_cases:
        status = "VALID" if is_valid_email(candidate) else "INVALID"
        print(f"  {candidate:<32} -> {status}")