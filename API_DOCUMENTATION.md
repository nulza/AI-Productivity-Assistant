# 📚 Complete API Documentation

## Base URL
```
http://localhost:3001/api
```

## Authentication
Currently, the API does not require authentication. In production, implement JWT tokens or API keys.

---

## Endpoints

### 1. Email Generation

**Endpoint:** `POST /api/email`

**Purpose:** Generate professional emails with context-aware tone and structure.

**Request Body:**
```json
{
  "audience": "Senior Manager",
  "tone": "Professional & Formal",
  "context": "Inform about project delay and new timeline"
}
```

**Parameters:**
- `audience` (string, required): Target recipient (e.g., "Client", "Team", "CEO")
- `tone` (string, required): Email tone - options:
  - `Professional & Formal`
  - `Friendly & Casual`
  - `Urgent & Direct`
  - `Persuasive & Engaging`
  - `Apologetic & Clarifying`
- `context` (string, required): Key points and content to cover (150+ chars recommended)

**Response:**
```json
{
  "success": true,
  "email": "Subject: Project Timeline Update\n\nDear [Audience],\n\n...",
  "generated_at": "2026-09-03T10:30:00.000Z",
  "disclaimer": "AI-generated content may require human review"
}
```

**Status Codes:**
- `200 OK`: Email generated successfully
- `400 Bad Request`: Missing required fields
- `500 Internal Server Error`: API error

**Example cURL:**
```bash
curl -X POST http://localhost:3001/api/email \
  -H "Content-Type: application/json" \
  -d '{
    "audience": "Client",
    "tone": "Professional & Formal",
    "context": "Follow up on proposal submitted last week"
  }'
```

---

### 2. Meeting Summarization

**Endpoint:** `POST /api/meeting`

**Purpose:** Analyze meeting transcripts and extract key decisions, action items, and deadlines.

**Request Body:**
```json
{
  "transcript": "John: We discussed Q4 objectives... Alice: Agreed, let's target June... Bob: Action items..."
}
```

**Parameters:**
- `transcript` (string, required): Full meeting notes or transcript (500+ chars recommended)

**Response:**
```json
{
  "success": true,
  "summary": "Executive Summary:\nTeam aligned on Q4 objectives...\n\nKey Decisions:\n- Approved timeline...",
  "generated_at": "2026-09-03T10:35:00.000Z",
  "disclaimer": "AI-generated summary may require verification"
}
```

**Status Codes:**
- `200 OK`: Meeting summarized successfully
- `400 Bad Request`: Missing transcript
- `500 Internal Server Error`: API error

**Example cURL:**
```bash
curl -X POST http://localhost:3001/api/meeting \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "Meeting with product team about Q4 roadmap. Discussed timeline, resources, and priorities. Approved expansion of feature X. Alice will lead implementation. Deadline: end of October."
  }'
```

---

### 3. Task Planning

**Endpoint:** `POST /api/tasks`

**Purpose:** Generate structured task plans with phases, milestones, and dependencies.

**Request Body:**
```json
{
  "objective": "Launch new customer portal by end of Q3. Team size: 4 developers, 2 designers. Budget: $100k"
}
```

**Parameters:**
- `objective` (string, required): Project goal and constraints (200+ chars recommended)

**Response:**
```json
{
  "success": true,
  "plan": "Phase 1: Discovery & Planning (Days 1-3)\n- Requirement gathering\n- Design mockups\n\nPhase 2: Development (Days 4-15)...",
  "generated_at": "2026-09-03T10:40:00.000Z",
  "disclaimer": "Review and adjust timeline based on actual team capacity"
}
```

**Status Codes:**
- `200 OK`: Task plan generated successfully
- `400 Bad Request`: Missing objective
- `500 Internal Server Error`: API error

**Example cURL:**
```bash
curl -X POST http://localhost:3001/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "objective": "Migrate legacy database to cloud infrastructure. Timeline: 8 weeks. Team: 2 engineers, 1 DevOps. Priority: High"
  }'
```

---

### 4. Research Assistant

**Endpoint:** `POST /api/research`

**Purpose:** Synthesize information and extract key insights on a topic.

**Request Body:**
```json
{
  "topic": "AI applications in workplace productivity. Focus on email automation and time savings."
}
```

**Parameters:**
- `topic` (string, required): Research topic or text to analyze (150+ chars recommended)

**Response:**
```json
{
  "success": true,
  "insights": "Key Insights:\n1. Market demand for AI productivity tools is growing...\n\nTrends:\n- Integration with existing workflows...",
  "generated_at": "2026-09-03T10:45:00.000Z",
  "disclaimer": "Verify insights with authoritative sources"
}
```

**Status Codes:**
- `200 OK`: Research completed successfully
- `400 Bad Request`: Missing topic
- `500 Internal Server Error`: API error

**Example cURL:**
```bash
curl -X POST http://localhost:3001/api/research \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Remote work trends and productivity tools in 2026. What are the key adoption factors?"
  }'
```

---

### 5. Chatbot

**Endpoint:** `POST /api/chat`

**Purpose:** Interactive conversational AI for workplace assistance.

**Request Body:**
```json
{
  "message": "How can I improve my email writing skills?"
}
```

**Parameters:**
- `message` (string, required): User message or question

**Response:**
```json
{
  "success": true,
  "reply": "Great question! Here are some tips for better email writing: 1. Be clear and concise... 2. Use proper structure...",
  "timestamp": "2026-09-03T10:50:00.000Z"
}
```

**Status Codes:**
- `200 OK`: Message processed successfully
- `400 Bad Request`: Missing message
- `500 Internal Server Error`: API error

**Example cURL:**
```bash
curl -X POST http://localhost:3001/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What are best practices for task prioritization?"
  }'
```

**Note:** Chat maintains conversation history for context (last 10 messages).

---

### 6. Health Check

**Endpoint:** `GET /api/health`

**Purpose:** Verify API server is operational.

**Response:**
```json
{
  "status": "operational",
  "timestamp": "2026-09-03T11:00:00.000Z",
  "version": "1.0.0"
}
```

**Status Codes:**
- `200 OK`: Server is operational

**Example cURL:**
```bash
curl http://localhost:3001/api/health
```

---

### 7. Configuration

**Endpoint:** `GET /api/config`

**Purpose:** Get application configuration and available features.

**Response:**
```json
{
  "app_name": "AI Workplace Productivity Assistant",
  "version": "1.0.0",
  "model": "gpt-3.5-turbo",
  "features": [
    "Email Generation",
    "Meeting Summarization",
    "Task Planning",
    "Research Assistant",
    "AI Chatbot"
  ],
  "timestamp": "2026-09-03T11:05:00.000Z"
}
```

**Example cURL:**
```bash
curl http://localhost:3001/api/config
```

---

### 8. Reset Chat History

**Endpoint:** `POST /api/reset-chat`

**Purpose:** Clear chatbot conversation history.

**Response:**
```json
{
  "success": true,
  "message": "Chat history cleared"
}
```

**Example cURL:**
```bash
curl -X POST http://localhost:3001/api/reset-chat
```

---

## Error Handling

All endpoints return errors in this format:

```json
{
  "success": false,
  "error": "Description of error"
}
```

**Common Error Codes:**
- `400 Bad Request`: Invalid input or missing required fields
- `404 Not Found`: Endpoint does not exist
- `500 Internal Server Error`: Server-side error (check API logs)

---

## Rate Limiting (Optional)

If rate limiting is enabled in `.env`:
- Headers returned:
  - `X-RateLimit-Limit`: Maximum requests per period
  - `X-RateLimit-Remaining`: Requests remaining
  - `X-RateLimit-Reset`: Unix timestamp of reset time

**Limit Exceeded Response:**
```json
{
  "success": false,
  "error": "Rate limit exceeded. Try again later.",
  "retry_after": 3600
}
```

---

## Request/Response Formats

### Content-Type
All requests must include:
```
Content-Type: application/json
```

### Timeouts
- Default timeout: 30 seconds
- Long operations may take 10-20 seconds

### Response Structure
All successful responses follow:
```json
{
  "success": true,
  "data": "...",
  "generated_at": "ISO 8601 timestamp",
  "disclaimer": "Optional safety message"
}
```

---

## Best Practices

### 1. Input Validation
- Always validate and sanitize user inputs
- Use meaningful context in prompts
- Provide sufficient detail (200+ characters)

### 2. Error Handling
```javascript
try {
  const response = await fetch('/api/email', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  
  if (!response.ok) {
    throw new Error(`API error: ${response.statusText}`);
  }
  
  const data = await response.json();
  if (!data.success) {
    console.error('Request failed:', data.error);
  }
} catch (error) {
  console.error('Network error:', error);
}
```

### 3. Caching Results
- Cache frequently used outputs
- Reduce API calls for identical requests
- Implement local storage for user preferences

### 4. Monitoring
- Log all API calls and responses
- Track error rates and types
- Monitor response times
- Check OpenAI usage dashboard

### 5. Performance
- Use async/await for concurrent requests
- Implement request timeouts
- Batch related operations
- Paginate large results

---

## Environment Variables

Configure in `api/.env`:

```env
# Required
OPENAI_API_KEY=sk-your-key

# Optional
OPENAI_MODEL=gpt-3.5-turbo
PORT=3001
DEBUG=False
LOG_LEVEL=INFO
CORS_ORIGINS=http://localhost:3000
RATE_LIMIT_ENABLED=False
```

---

## Testing

### Postman Collection
Import this Postman collection for easy testing:

```json
{
  "info": {
    "name": "AI Productivity Assistant API",
    "version": "1.0.0"
  },
  "item": [
    {
      "name": "Email Generation",
      "request": {
        "method": "POST",
        "url": "{{base_url}}/api/email",
        "body": {
          "mode": "raw",
          "raw": "{\"audience\":\"Manager\",\"tone\":\"Professional & Formal\",\"context\":\"Project update\"}"
        }
      }
    }
  ]
}
```

### Using cURL in Scripts
```bash
#!/bin/bash

# Generate email with curl
curl -s -X POST http://localhost:3001/api/email \
  -H "Content-Type: application/json" \
  -d '{
    "audience": "Client",
    "tone": "Professional & Formal",
    "context": "Project status"
  }' | jq '.email'
```

---

## Support & Troubleshooting

**API won't start:**
- Check port 3001 is available
- Verify Python version (3.8+)
- Check OPENAI_API_KEY in .env

**Slow responses:**
- API calls typically take 5-20 seconds
- Check network connection
- Verify OpenAI API status

**CORS errors:**
- Update CORS_ORIGINS in .env
- Ensure web app URL matches

---

## Version History

- **v1.0.0** (Sept 2026): Initial release
  - Email generation
  - Meeting summarization
  - Task planning
  - Research assistant
  - Chatbot interface

---

**API Documentation v1.0.0** | Last Updated: September 3, 2026
