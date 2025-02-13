ROLE_ASSISTANT="""
You are an email classificate assistant that is used to read emails
and classify with one word the content readed.
"""

RULES="""
- You should answer with one word.
- You should read the categories before classify, if the mail doesn't match, you can 
say a new category 
- If composite word category, you can use underline to union the sentence but
keeping the one word.
- Don't provide any information about others topics beyond the classification.
"""

EMAIL_TEST="""
Subject: Confidential: Q4 Financial Performance & Global Sales Report - Board Review Required
From: michael.chen@company.com
To: board.members@company.com
CC: finance.team@company.com, sales.directors@company.com

CONFIDENTIAL - DO NOT FORWARD

Dear Board Members,

Please find attached our comprehensive Q4 2024 Financial & Sales Performance Report for immediate review. Key highlights:

Financial Metrics:
- Revenue: $89.2M (↑12% YoY)
- Operating Margin: 28.3%
- EBITDA: $25.1M
- Cash Position: $142M

Sales Performance:
- Enterprise deals closed: 47 (+15% QoQ)
- Average deal size: $1.89M
- Customer acquisition cost: reduced by 18%
- Pipeline value: $215M

Immediate attention required on:
1. APAC market underperformance
2. Q1 2025 revenue projections
3. Proposed M&A targets

Meeting scheduled: January 15th, 9 AM EST.

Best regards,
Michael Chen
CFO | Global Sales Operations

--
This email contains confidential financial information. Any unauthorized disclosure, copying, or distribution is strictly prohibited.
"""