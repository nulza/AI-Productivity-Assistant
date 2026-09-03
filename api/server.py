"""
AI Workplace Productivity Assistant - Backend API Server
Provides AI-powered endpoints for email generation, meeting summarization, task planning, research, and chatbot
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import openai
from datetime import datetime
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')
MODEL = "gpt-3.5-turbo"

# ==================== PROMPT TEMPLATES ====================

SYSTEM_PROMPTS = {
    'email': """You are a professional business communication expert specializing in workplace emails. 
Your task is to generate clear, professional, and contextually appropriate emails.
Always maintain professional tone unless specifically requested otherwise.
Format the email with Subject line, proper greeting, body, and closing.
Keep emails concise but informative.""",
    
    'meeting': """You are an expert executive assistant skilled at summarizing meetings and extracting actionable insights.
Analyze meeting transcripts to identify:
1. Executive summary (2-3 sentences of main topics)
2. Key decisions made
3. Action items with assigned owners and deadlines
4. Important dates and milestones
5. Follow-up items
Format output in a clear, scannable structure.""",
    
    'task': """You are an experienced project manager with expertise in task planning and prioritization.
Break down projects into clear, actionable phases and tasks.
Consider:
- Timeline and deadlines
- Resource requirements
- Dependencies between tasks
- Risk mitigation strategies
- Milestone definitions
Organize tasks by priority and logical sequence.""",
    
    'research': """You are a research analyst expert at synthesizing information and extracting key insights.
Analyze provided information or topic to deliver:
1. Key insights and takeaways
2. Important trends and patterns
3. Practical recommendations
4. Relevant data points and statistics
Provide balanced, evidence-based analysis.""",
    
    'chatbot': """You are a helpful and professional workplace assistant AI.
Provide clear, concise answers to workplace questions.
Help with:
- Email drafting advice
- Workflow optimization
- Task management strategies
- General workplace guidance
Always offer to help users navigate to specific tools if relevant."""
}

# ==================== EMAIL GENERATION ====================

@app.route('/api/email', methods=['POST'])
def generate_email():
    """Generate professional email based on parameters"""
    try:
        data = request.json
        audience = data.get('audience', 'Team')
        tone = data.get('tone', 'Professional & Formal')
        context = data.get('context', '')
        
        prompt = f"""Generate a professional email with these parameters:
Recipient/Audience: {audience}
Tone: {tone}
Context/Key Points: {context}

Requirements:
- Include Subject line
- Professional greeting and closing
- Clear body content addressing the context
- 150-250 words
- Ready to send format

Generate the email:"""
        
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPTS['email']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        email_content = response['choices'][0]['message']['content']
        
        return jsonify({
            'success': True,
            'email': email_content,
            'generated_at': datetime.now().isoformat(),
            'disclaimer': 'AI-generated content may require human review'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ==================== MEETING SUMMARIZER ====================

@app.route('/api/meeting', methods=['POST'])
def summarize_meeting():
    """Summarize meeting transcript and extract action items"""
    try:
        data = request.json
        transcript = data.get('transcript', '')
        
        if not transcript:
            return jsonify({'success': False, 'error': 'Transcript required'}), 400
        
        prompt = f"""Analyze this meeting transcript and provide:

1. Executive Summary (2-3 sentences)
2. Key Decisions Made (bulleted list)
3. Action Items (format: Task | Owner | Deadline | Priority)
4. Important Dates/Deadlines
5. Follow-up Required

Transcript:
{transcript}

Provide structured output with clear sections."""
        
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPTS['meeting']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=800
        )
        
        summary = response['choices'][0]['message']['content']
        
        return jsonify({
            'success': True,
            'summary': summary,
            'generated_at': datetime.now().isoformat(),
            'disclaimer': 'AI-generated summary may require verification'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ==================== TASK PLANNER ====================

@app.route('/api/tasks', methods=['POST'])
def plan_tasks():
    """Generate task plan from project objective"""
    try:
        data = request.json
        objective = data.get('objective', '')
        
        if not objective:
            return jsonify({'success': False, 'error': 'Objective required'}), 400
        
        prompt = f"""Create a detailed task plan for this project:

Project Objective: {objective}

Provide:
1. Major Phases (with estimated duration)
2. Key Tasks/Milestones
3. Dependencies
4. Resource Requirements
5. Risk Considerations
6. Success Metrics

Format as a structured project timeline."""
        
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPTS['task']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=1000
        )
        
        plan = response['choices'][0]['message']['content']
        
        return jsonify({
            'success': True,
            'plan': plan,
            'generated_at': datetime.now().isoformat(),
            'disclaimer': 'Review and adjust timeline based on actual team capacity'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ==================== RESEARCH ASSISTANT ====================

@app.route('/api/research', methods=['POST'])
def conduct_research():
    """Synthesize research topic and extract insights"""
    try:
        data = request.json
        topic = data.get('topic', '')
        
        if not topic:
            return jsonify({'success': False, 'error': 'Topic required'}), 400
        
        prompt = f"""Analyze and synthesize information about this topic:

Topic: {topic}

Provide:
1. Key Insights (main takeaways)
2. Important Trends & Patterns
3. Relevant Data Points
4. Practical Recommendations
5. Potential Risks/Considerations

Format as clear, actionable insights."""
        
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPTS['research']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        insights = response['choices'][0]['message']['content']
        
        return jsonify({
            'success': True,
            'insights': insights,
            'generated_at': datetime.now().isoformat(),
            'disclaimer': 'Verify insights with authoritative sources'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ==================== CHATBOT ====================

# Store conversation history for context
conversation_history = []

@app.route('/api/chat', methods=['POST'])
def chat():
    """Interactive chatbot endpoint"""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'success': False, 'error': 'Message required'}), 400
        
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Keep only last 10 messages for context
        messages = conversation_history[-10:] if len(conversation_history) > 10 else conversation_history
        
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPTS['chatbot']}
            ] + messages,
            temperature=0.7,
            max_tokens=300
        )
        
        assistant_message = response['choices'][0]['message']['content']
        
        # Add assistant response to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return jsonify({
            'success': True,
            'reply': assistant_message,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ==================== UTILITY ENDPOINTS ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'operational',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/config', methods=['GET'])
def get_config():
    """Get application configuration"""
    return jsonify({
        'app_name': 'AI Workplace Productivity Assistant',
        'version': '1.0.0',
        'model': MODEL,
        'features': [
            'Email Generation',
            'Meeting Summarization',
            'Task Planning',
            'Research Assistant',
            'AI Chatbot'
        ],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/reset-chat', methods=['POST'])
def reset_chat():
    """Reset chat conversation history"""
    global conversation_history
    conversation_history = []
    return jsonify({'success': True, 'message': 'Chat history cleared'})

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3001))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    print(f"""
    ╔════════════════════════════════════════════════════════════════╗
    ║        🤖 AI WORKPLACE PRODUCTIVITY ASSISTANT - API 🤖        ║
    ║                                                                ║
    ║  Server running on: http://localhost:{port}                  ║
    ║  Model: {MODEL}                                             ║
    ║  Debug: {debug}                                              ║
    ║                                                                ║
    ║  Available Endpoints:                                         ║
    ║  POST /api/email        - Generate professional emails        ║
    ║  POST /api/meeting      - Summarize meeting transcripts       ║
    ║  POST /api/tasks        - Create task plans                   ║
    ║  POST /api/research     - Synthesize research insights        ║
    ║  POST /api/chat         - Interactive chatbot                 ║
    ║  GET  /api/health       - Health check                        ║
    ║  GET  /api/config       - App configuration                   ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)
