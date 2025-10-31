```mermaid
graph TD
    A[Start] --> B(Read Leads: CSV/Form)
    B --> C(Enrich Lead Data: Clearbit)
    C --> D{Split: Enriched vs. Raw}
    D -- True (Enriched) --> E(Score Lead: Enriched)
    D -- False (Raw) --> F(Score Lead: Raw)
    E --> G(Update Google Sheet/CRM)
    G --> H(Send Personalized Email)
    H --> I[Slack Summary: Success]
    F --> J[Slack Notification: Enrichment Failure]
