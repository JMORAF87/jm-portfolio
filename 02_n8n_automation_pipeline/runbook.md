# Runbook: n8n Lead Management & Outreach Pipeline

This runbook provides essential information for operating, maintaining, and troubleshooting the n8n Lead Management & Outreach Pipeline. It covers operational procedures, secret management, failure modes, key performance indicators (KPIs), and on-call notes.

## 1. Operational Procedures

### 1.1. Starting the Workflow
1.  Log in to the n8n instance.
2.  Navigate to the "Lead Management & Outreach Pipeline" workflow.
3.  Ensure all credentials (Google Sheets, SMTP, Calendly, Slack) are correctly configured.
4.  Activate the workflow.
5.  The workflow can be triggered manually or via a webhook (if configured for form submissions).

### 1.2. Monitoring
*   Regularly check the n8n execution logs for successful runs and errors.
*   Monitor the designated Slack channel for lead processing summaries and error notifications.
*   Verify new leads are appearing in the Google Sheet/CRM.

## 2. Secret Management

All sensitive credentials are managed as environment variables within the n8n instance or directly in the `.env.example` file for local development.

*   `GOOGLE_SHEETS_ID`: ID of the Google Sheet for lead storage.
*   `SMTP_USER`: Email address for sending personalized emails.
*   `SMTP_PASS`: Password for the SMTP email account.
*   `CALENDLY_LINK`: Jorge Mora's Calendly scheduling link.
*   `SLACK_WEBHOOK_URL`: Slack webhook URL for notifications.

**Action:** Ensure these secrets are stored securely and not hardcoded into the workflow itself.

## 3. Failure Modes & Troubleshooting

| Failure Mode | Symptoms | Troubleshooting Steps | On-Call Notes |
|---|---|---|---|
| **Google Sheets Integration Failure** | Leads not appearing in Google Sheet; n8n execution error related to Google Sheets node. | 1. Verify `GOOGLE_SHEETS_ID` is correct. 2. Check Google Sheets API permissions. 3. Test Google Sheets node connectivity in n8n. | Check Google Cloud Console for API errors. |
| **Email Sending Failure** | Personalized emails not being sent; n8n execution error related to Email Send node. | 1. Verify `SMTP_USER` and `SMTP_PASS` are correct. 2. Check SMTP server logs for errors. 3. Test Email Send node connectivity. | Check email service provider status page. |
| **Clearbit Enrichment Failure** | Lead data not enriched; n8n execution error related to Clearbit node. | 1. Verify Clearbit API key is valid. 2. Check Clearbit API rate limits. 3. Test Clearbit node connectivity. | Clearbit API status page. |
| **Slack Notification Failure** | No Slack summaries or error notifications; n8n execution error related to Slack node. | 1. Verify `SLACK_WEBHOOK_URL` is correct. 2. Test Slack node connectivity. | Check Slack API status page. |
| **Lead Scoring Logic Error** | Incorrect lead scores; unexpected lead routing. | 1. Review the Function node logic (`Score Lead`). 2. Test with sample data to debug scoring. | Consult with Product/Sales for scoring criteria. |

### 3.1. Deep Dive: Resolving Clearbit Enrichment Failure (Example)

**Scenario:** The workflow fails at the "Enrich Lead Data" node with an HTTP 404 error for a specific lead.

**Root Cause Analysis:**
The Clearbit API returns a 404 when it cannot find any data for the provided email address (i.e., the lead is not in their database). The workflow is currently configured to fail the entire batch when this happens.

**Resolution Strategy (Operational Fix):**
1.  **Isolate the Failure:** In the n8n workflow, modify the "Enrich Lead Data" node settings to "Continue on Fail" (or "Ignore Errors"). This prevents a single 404 from stopping the entire batch of leads.
2.  **Conditional Routing:** Immediately after the "Enrich Lead Data" node, add an "IF" node.
    *   **Branch 1 (Success):** If the Clearbit data exists, proceed to "Score Lead."
    *   **Branch 2 (Failure/No Data):** If the Clearbit data is empty or the node returned an error, route the lead directly to "Score Lead" with a default score (e.g., 25) and log the "No Data" event to a separate Slack channel for manual review.

**Impact:** This change increases the workflow's resilience and ensures that valuable leads are not lost due to a third-party data enrichment failure.

## 4. Key Performance Indicators (KPIs)

*   **Lead Processing Success Rate:** Percentage of leads successfully processed through the entire pipeline.
*   **Email Open Rate:** Percentage of personalized emails opened by leads.
*   **Calendly Booking Rate:** Percentage of leads who book a meeting via Calendly.
*   **Lead-to-Opportunity Conversion Rate:** (Tracked in CRM) Percentage of processed leads that convert to sales opportunities.

## 5. On-Call Notes

*   **Primary Contact:** Jorge Mora (contact@jmmultiservices.xyz)
*   **Escalation:** [Team Lead/Manager Contact]
*   **Emergency Procedure:** In case of critical failure, deactivate the n8n workflow, investigate the root cause using execution logs, and notify relevant stakeholders.
