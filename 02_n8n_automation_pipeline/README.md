# n8n Automation Pipeline: Lead Management & Outreach

# n8n Automation Pipeline: Lead Management & Outreach

## Purpose
This n8n workflow automates a comprehensive lead management and outreach process. It demonstrates how to ingest leads from a sample CSV (`sample_leads.csv`), enrich their data, score them based on predefined criteria, integrate with CRM/Google Sheets, send personalized emails, schedule meetings via Calendly, and summarize activities in Slack. The accompanying runbook includes a detailed section on failure analysis, proving operational maturity and resilience.

## Quickstart in 60 Seconds
1.  **Import Workflow:** Import `workflow.json` into your n8n instance.
2.  **Configure Credentials:** Update the `.env.example` with your actual credentials and configure them in n8n.
3.  **Provide Data:** Upload the `sample_leads.csv` file to the "Read Leads" node or configure a webhook trigger.
4.  **Activate Workflow:** Activate the workflow and trigger it manually or via the configured input.

## Architecture Diagram Link
[Mermaid Flowchart](diagram.md)

## Test Instructions
1.  **Manual Trigger:** Trigger the workflow manually in n8n using the `sample_leads.csv` data.
2.  **Data Flow:** Verify that data flows correctly through each node: data enrichment, scoring, CRM/Sheet update, email sending, Calendly event creation, and Slack notification.
3.  **Operational Maturity:** Review the `runbook.md` for the detailed troubleshooting steps on handling a Clearbit 404 failure, demonstrating your operational readiness.

## Results/Metrics
This automation pipeline aims to achieve:
*   **Increased Lead Conversion:** Improve lead-to-opportunity conversion by 10% through timely and personalized outreach.
*   **Reduced Manual Effort:** Automate lead processing, saving up to 5 hours per week of manual data entry and follow-up.
*   **Enhanced Resilience:** Detailed failure analysis in the runbook ensures 99.9% uptime for the lead processing pipeline.

## License
MIT License

Copyright (c) 2025 Jorge Mora
