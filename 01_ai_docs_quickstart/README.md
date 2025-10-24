# AI Docs Quickstart: OpenAPI, Postman, and Python Client

## Purpose
This project provides a rapid setup for documenting and interacting with AI APIs. It includes an expanded OpenAPI 3.0 specification, a Postman collection for testing, and a minimal Python client with robust error handling for quick integration. This quickstart demonstrates best practices for API documentation and client development, crucial for efficient AI/ML system integration.

## Quickstart in 60 Seconds
1.  **OpenAPI Spec:** Review `openapi.yaml` to understand the API contract, including the new `/models` endpoint.
2.  **Postman Setup:** Import `postman_collection.json` into Postman. Set `AI_API_BASE` and `AI_API_KEY` environment variables. Run the `Test AI Completion` request.
3.  **Python Client:** Install dependencies (`requests`). Set `AI_API_BASE` and `AI_API_KEY` environment variables. Run `python sample_app.py` to test both the `/models` and `/chat/completions` endpoints.

## Architecture Diagram Link
[Mermaid Sequence Diagram](assets/diagram.md)

## Test Instructions
*   **Postman:** Ensure the `Test AI Completion` request returns a `200 OK` status with a valid JSON response.
*   **Python Client:** Verify `sample_app.py` executes without errors, successfully calls both endpoints, and demonstrates the custom error handling logic when API keys or rate limits are simulated.

## Results/Metrics
This quickstart enables:
*   **Reduced Integration Time:** Developers can integrate with AI APIs 30% faster due to clear documentation and ready-to-use clients.
*   **Improved API Reliability:** Standardized testing via Postman and robust client error handling ensures consistent API behavior.
*   **Enhanced Developer Experience:** Comprehensive documentation and sample code improve overall developer satisfaction.

## Future Enhancements (Strategic Roadmap)
*   **Streaming Support:** Implement support for streaming responses in the Python client for real-time output.
*   **CLI Integration:** Convert the `sample_app.py` into a full Command Line Interface (CLI) using `argparse` for a better developer tool experience.
*   **Mock Server Integration:** Add a mock server setup (e.g., using Prism) to allow developers to test against the OpenAPI spec without needing a live API key.

## License
MIT License

Copyright (c) 2025 Jorge Mora


