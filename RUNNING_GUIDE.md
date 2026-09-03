# 🚀 Running the Application

This guide explains how to run the AI Workplace Productivity Assistant.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git (optional)
- A modern web browser

## Quick Start (Automated Setup)

### For macOS/Linux:
```bash
chmod +x setup.sh
./setup.sh
```

### For Windows:
```cmd
setup.bat
```

These scripts will automatically:
- ✅ Create a Python virtual environment
- ✅ Install all dependencies
- ✅ Set up logging directories
- ✅ Configure environment files

## Manual Setup

If you prefer manual setup, follow these steps:

### 1. Create Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r api/requirements.txt
```

### 3. Configure Environment
```bash
# Copy the example environment file
cp api/.env.example api/.env

# Edit api/.env and add your OPENAI_API_KEY
nano api/.env  # macOS/Linux
notepad api\.env  # Windows
```

### 4. Start the API Server
```bash
python api/server.py
```

You should see:
```
╔════════════════════════════════════════════════════════════════╗
║        🤖 AI WORKPLACE PRODUCTIVITY ASSISTANT - API 🤖        ║
║                                                                ║
║  Server running on: http://localhost:3001                     ║
║  Model: gpt-3.5-turbo                                         ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

### 5. Open Web Application

**Option A: Direct File Access**
- Navigate to `web-app/` folder
- Open `index.html` in your web browser
- Use demo features (no API required)

**Option B: Local Web Server**
```bash
# Terminal 2 (from project root)
cd web-app
python -m http.server 8000
```
Then visit: `http://localhost:8000`

## Testing the Application

### Using Demo Mode (No API)
- All features work with demo data
- No OpenAI API key needed
- Perfect for UI/UX testing

### Using Live API
1. Ensure API server is running on port 3001
2. Update `web-app/index.html` if needed:
   - Change `API_BASE` to your server URL
3. Use any feature, and it will call the actual OpenAI API

## Troubleshooting

### "Module not found" Error
```bash
# Make sure virtual environment is activated
# And dependencies are installed
pip install -r api/requirements.txt
```

### "API key not found" Error
```bash
# Check api/.env has your OPENAI_API_KEY
cat api/.env
# Edit and add your key
nano api/.env
```

### Port Already in Use
```bash
# If port 3001 is busy, change in api/server.py
# Or kill the process:

# macOS/Linux
lsof -i :3001
kill -9 <PID>

# Windows
netstat -ano | findstr :3001
taskkill /PID <PID> /F
```

### CORS Issues
- API server has CORS enabled by default
- If issues persist, check `api/.env` CORS settings
- Ensure `http://localhost:8000` is in `CORS_ORIGINS`

## API Endpoints Reference

When API server is running, you can test endpoints:

```bash
# Health check
curl http://localhost:3001/api/health

# Generate email
curl -X POST http://localhost:3001/api/email \
  -H "Content-Type: application/json" \
  -d '{
    "audience": "Manager",
    "tone": "Professional & Formal",
    "context": "Project update"
  }'

# Summarize meeting
curl -X POST http://localhost:3001/api/meeting \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "Meeting notes here..."
  }'

# Plan tasks
curl -X POST http://localhost:3001/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "objective": "Launch new product in Q4"
  }'

# Chat
curl -X POST http://localhost:3001/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "How do I write better emails?"
  }'
```

## Development Mode

For active development with hot reload:

```bash
# Install development dependencies
pip install flask-reload

# Start server with auto-reload
FLASK_ENV=development python api/server.py
```

## Deployment

### Docker (Optional)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY api/ ./api/
COPY web-app/ ./web-app/
RUN pip install -r api/requirements.txt
EXPOSE 3001
CMD ["python", "api/server.py"]
```

Build and run:
```bash
docker build -t ai-assistant .
docker run -p 3001:3001 -e OPENAI_API_KEY=your-key ai-assistant
```

### Production Deployment
1. Use a production WSGI server (Gunicorn, uWSGI)
2. Set `DEBUG=False` in .env
3. Use environment-specific configurations
4. Enable HTTPS
5. Set up proper logging and monitoring

## Performance Tips

- **Cache prompts**: Reduce API costs by caching common operations
- **Batch requests**: Combine multiple requests when possible
- **Monitor usage**: Check OpenAI usage dashboard regularly
- **Optimize timeouts**: Adjust timeout values in .env based on needs

## Security Best Practices

- ✅ Never commit API keys to version control
- ✅ Use `.env` files and `.gitignore` (already configured)
- ✅ Rotate API keys periodically
- ✅ Validate all user inputs
- ✅ Use HTTPS in production
- ✅ Implement rate limiting
- ✅ Log and monitor API usage

## Getting Help

1. Check `GETTING_STARTED.md` for setup help
2. Review `PROMPT_ENGINEERING_GUIDE.md` for prompt tips
3. Check API logs: `logs/api.log`
4. Test endpoints manually with curl
5. Check OpenAI status page for service issues

## Next Steps

After running the application:
1. Explore each feature in the UI
2. Try different prompts and parameters
3. Review generated outputs
4. Integrate into your workflow
5. Customize prompts for your use case

---

**Happy Productivity! 🚀**
