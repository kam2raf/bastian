# API Client

API Client is a small Python project demonstrating communication with REST-style services.

The demo sends requests to sample endpoints, parses responses and displays formatted results.

---

## Flow

```
Endpoint
    │
    ▼
Request
    │
    ▼
API Client
    │
    ▼
Response
    │
    ▼
Parser
```

---

## Example

```
Connecting...

GET /users

Status : 200

Items received : 3

Operation completed.
```

---

## Project Files

- app.py — application entry
- client.py — API client
- endpoint.py — endpoint model
- request.py — request object
- response.py — response model
- parser.py — response parser
- repository.py — endpoint provider
- sample_api.py — demo API
- config.py — settings

Run

```bash
python app.py
```

The project uses sample responses without Internet access.
