# 🎓 Prepare Me AI - Intelligent Learning Platform

An AI-powered educational platform that combines advanced AI, emotion detection, and interactive learning tools to create a personalized study experience. Prepare Me AI helps students learn concepts through explanations, examples, analogies, visual flowcharts, and adaptive assessments.

## 🌟 Features

### Core Learning Features
- **📚 PDF Analysis & Concept Extraction** - Upload study materials and automatically extract important concepts using AI
- **🤖 AI-Powered Explanations** - Get comprehensive explanations with analogies, examples, and visual flowcharts
- **💬 Interactive Doubt Chat** - Real-time conversational AI for clearing doubts and answering questions
- **📝 Adaptive Assessment** - Generate and evaluate test questions based on difficulty levels
- **🎨 Visual Flowcharts** - Auto-generate Mermaid diagrams to visualize concept relationships
- **🔄 Code Translation** - Translate code between different programming languages

### Engagement & Personalization
- **😊 Real-time Emotion Detection** - Facial emotion detection during learning sessions to track engagement
- **📖 Educational Stories** - Generate engaging stories across multiple genres:
  - Animal Tales with moral lessons
  - Mythology Stories
  - Science Fiction
  - Humorous Stories
- **🎯 Fun Facts** - Learn through interesting facts about:
  - Animals
  - Nature
  - Science & Technology
  - Space
  - Mythology
  - Food & Inventions

### Technical Features
- **WebSocket Support** - Real-time emotion data broadcasting
- **Multi-format Support** - PDF processing and text extraction
- **RESTful API** - Clean API endpoints for all features
- **Session Management** - Track learning progress and time spent on concepts

## 🛠️ Technology Stack

### Backend
- **Node.js** with Express.js - Main server and API
- **Python** - AI processing and data analysis
- **Flask** - Alternative backend framework

### AI & ML
- **Google Gemini AI** - Core AI engine for content generation and analysis
- **DeepFace** - Facial emotion detection
- **OpenCV** - Computer vision for face detection

### Data Processing
- **PyPDF2** - PDF text extraction
- **PyMuPDF** - Alternative PDF processing
- **python-dotenv** - Environment configuration

### Frontend
- **HTML5** - Markup
- **JavaScript** - Interactive features
- **WebSocket** - Real-time communication
- **Mermaid.js** - Diagram visualization

### Additional Libraries
- **Multer** - File upload handling
- **Express-FileUpload** - File upload middleware
- **Express-Session** - Session management
- **ws** - WebSocket library

## 📋 Prerequisites

- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn** package manager
- **Google Gemini API Key** - [Get it here](https://makersuite.google.com/app/apikey)
- **Webcam** (for emotion detection features)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Abhinavaa-S-Kumar/Prepare-Me-AI.git
cd Prepare-Me-AI
```

### 2. Install Node.js Dependencies
```bash
npm install
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Backend Python Dependencies (Optional)
```bash
pip install -r backend/requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SERVER_URL=http://localhost:3000
```

**⚠️ Important**: Never commit your `.env` file to version control. Add it to `.gitignore`.

## 🎯 Quick Start

### Start the Server
```bash
node server.js
```

The server will start on `http://localhost:3000`

### Access the Application
Open your browser and navigate to:
```
http://localhost:3000
```

### Available Pages
- **Home** - `index.html` - Main landing page
- **Chat** - `chat.html` - Interactive doubt clearing
- **Topic Explanation** - `TOPICBEST.html` - Detailed concept learning

## 📡 API Endpoints

### Content Generation
- `POST /generate-image` - Generate Mermaid diagram images
- `POST /animal_story` - Generate animal stories
- `POST /fairy_story` - Generate fairy tales
- `POST /fiction` - Generate science fiction stories
- `POST /mythology_story` - Generate mythology stories
- `POST /humor` - Generate humorous stories

### Learning Tools
- `POST /upload` - Upload PDF and extract concepts
- `POST /explain` - Get explanation with emotion detection
- `POST /chat` - Doubt chat conversation
- `POST /test` - Generate test questions
- `POST /evaluate` - Evaluate student answers

### Fun Facts
- `POST /animal_fact` - Animal facts
- `POST /science` - Science facts
- `POST /mythology_fact` - Mythology facts
- `POST /nature_fact` - Nature facts
- `POST /space` - Space facts
- `POST /food_fact` - Food facts
- `POST /invention` - Invention facts

### Utilities
- `POST /translate` - Code translation between languages

## 📁 Project Structure

```
Prepare-Me-AI/
├── frontend/                    # Frontend HTML, CSS, JS files
│   ├── index.html              # Home page
│   ├── chat.html               # Chat interface
│   ├── TOPICBEST.html          # Topic explanation page
│   ├── mermaid.js              # Mermaid diagram generation
│   ├── modelStore.js           # Data management
│   └── assets/                 # Images and backgrounds
├── backend/                     # Python backend modules
│   ├── app.py                  # Flask application
│   ├── imp_concepts.py         # PDF concept extraction
│   ├── topicexplain.py         # Comprehensive explanations
│   ├── qanda.py                # Question generation
│   ├── evaluate.py             # Answer evaluation
│   ├── doubtchat.py            # Doubt chat logic
│   ├── explanation.py          # Explanation generation
│   ├── analogy.py              # Analogy generation
│   ├── example.py              # Example generation
│   ├── flowchart.py            # Flowchart generation
│   ├── emotion_detection.py    # Emotion detection module
│   └── requirements.txt         # Python dependencies
├── server.js                    # Main Express server
├── dummyserver.js              # Alternative server setup
├── mermaid.py                  # Mermaid converter utility
├── package.json                # Node.js dependencies
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in repo)
└── output/                     # Generated files (images, diagrams)
```

## 🔑 Key Files Overview

### Server Files
- **server.js** - Main Express server with all API routes and WebSocket support
- **dummyserver.js** - Alternative server without WebSocket functionality

### Python Modules
- **imp_concepts.py** - Extracts important concepts from PDFs using Gemini AI
- **topicexplain.py** - Generates comprehensive explanations with analogies, examples, and flowcharts
- **qanda.py** - Generates test questions with various difficulty levels
- **evaluate.py** - Evaluates student answers using AI
- **emotion_detection.py** - Real-time facial emotion detection

### Standalone Scripts
- **animal.py, animal_tales.py, mythology.py, science.py, space.py, nature.py** - Generate fun facts and stories

## 🎮 Usage Examples

### Upload a PDF and Extract Concepts
```javascript
const formData = new FormData();
formData.append('file', pdfFile);

fetch('/upload', {
  method: 'POST',
  body: formData
})
.then(res => res.json())
.then(data => console.log('Concepts:', data));
```

### Get Explanation with Flowchart
```javascript
fetch('/explain', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ concept: 'Photosynthesis' })
})
.then(res => res.json())
.then(data => console.log('Explanation:', data));
```

### Generate Test Questions
```javascript
fetch('/test', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    topic: 'Biology',
    number: 5,
    difficulty: 'medium'
  })
})
.then(res => res.json())
.then(data => console.log('Questions:', data));
```

## ⚙️ Configuration

### Emotion Detection
The emotion detection module tracks 7 emotions:
- Happy
- Sad
- Angry
- Fear
- Disgust
- Surprise
- Neutral

Data is collected every 30 seconds during learning sessions.

### Mermaid Diagrams
Flowcharts are automatically generated and converted to images using the Mermaid API. Images are saved in the `output/` directory.

## 🐛 Troubleshooting

### API Key Issues
- Ensure `GEMINI_API_KEY` is set in `.env`
- Check that the API key has sufficient quota
- Verify the key is valid on [Google AI Studio](https://makersuite.google.com/app/apikey)

### Emotion Detection Not Working
- Ensure webcam is connected and permissions are granted
- Check that DeepFace and OpenCV are properly installed
- Verify Python environment has all dependencies

### PDF Upload Fails
- Ensure PDF is not corrupted
- Check file size is reasonable
- Verify PyPDF2 is installed

### Server Won't Start
- Check if port 3000 is already in use
- Ensure all npm dependencies are installed
- Verify Node.js version is compatible

## 📚 Documentation

For detailed function documentation, see `PROJECT_FUNCTIONS_DOCUMENTATION.md`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as an intelligent learning platform to enhance student engagement and comprehension through AI-powered personalized learning.

## 🙏 Acknowledgments

- Google Gemini AI for powerful language models
- DeepFace for emotion detection
- Mermaid for diagram visualization
- The open-source community

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Happy Learning! 🚀**
