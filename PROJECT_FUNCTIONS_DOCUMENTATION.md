# Project Functions Documentation

## Overview
This is a comprehensive documentation of all functions in the Prepare__Me AI project.

---

## Root Directory Files

### 1. **a.py**
- **Status**: Empty file (no functions)

### 2. **animal.py**
- **Functions**: None (script-based execution)
- **Purpose**: Generates fun facts about animals for 5-10 year old students using Gemini AI
- **API Key Location**: Line 6

### 3. **animal_tales.py**
- **Functions**: None (script-based execution)
- **Purpose**: Generates animal stories with moral lessons using Gemini AI
- **API Key Location**: Line 6

### 4. **mythology.py**
- **Functions**: None (script-based execution)
- **Purpose**: Generates mythology stories using Gemini AI
- **API Key Location**: Line 6

### 5. **mythology_fact.py**
- **Functions**: None (script-based execution)
- **Purpose**: Generates mythology facts using Gemini AI
- **API Key Location**: Line 6

### 6. **nature.py**
- **Functions**: None (script-based execution)
- **Purpose**: Generates nature facts using Gemini AI
- **API Key Location**: Line 6

### 7. **science.py**
- **Functions**: None (script-based execution)
- **Purpose**: Generates science and technology facts using Gemini AI
- **API Key Location**: Line 6

### 8. **space.py**
- **Functions**: None (script-based execution)
- **Purpose**: Generates space facts using Gemini AI
- **API Key Location**: Line 6

### 9. **mermaid.py**
- **Class**: `MermaidConverter`
  - **`__init__(self, output_dir: str = "output")`**: Initialize converter with output directory
  - **`encode_mermaid(self, mermaid_code: str) -> str`**: Encodes Mermaid code for API use
  - **`get_mermaid_image(self, encoded_data: str) -> Optional[bytes]`**: Fetches image from Mermaid API
  - **`save_image(self, image_data: bytes, output_filename: str) -> bool`**: Saves generated image to file
  - **`convert(self, mermaid_code: str, output_filename: str) -> bool`**: Main method to convert Mermaid code to image
- **Standalone Functions**:
  - **`read_mermaid_code(file_path: str) -> str`**: Reads Mermaid code from file

### 10. **server.js**
- **Functions**: None (Express route handlers)
- **Routes**:
  - `POST /generate-image`: Generates Mermaid diagram images
  - `POST /upload`: Uploads PDF and extracts important concepts
  - `POST /explain`: Explains concepts with emotion detection
  - `POST /chat`: Handles doubt chat conversations
  - `POST /test`: Generates test questions
  - `POST /evaluate`: Evaluates student answers
  - `POST /translate`: Translates code between languages
  - `POST /animal_story`: Generates animal stories
  - `POST /fairy_story`: Generates fairy tales
  - `POST /fiction`: Generates science fiction stories
  - `POST /mythology_story`: Generates mythology stories
  - `POST /humor`: Generates humorous stories
  - `POST /science`: Generates science facts
  - `POST /mythology_fact`: Generates mythology facts
  - `POST /animal_fact`: Generates animal facts
  - `POST /food_fact`: Generates food facts
  - `POST /nature_fact`: Generates nature facts
  - `POST /invention`: Generates invention facts
  - `POST /space`: Generates space facts
- **WebSocket Functions**:
  - **`broadcastEmotionData(data)`**: Broadcasts emotion data to all connected clients

### 11. **dummyserver.js**
- **Functions**: None (Express route handlers)
- **Routes**: Similar to server.js but without WebSocket functionality
- **Global Variable**: `timeSpentData` - stores time spent on each concept

---

## Backend Directory Files

### 1. **backend/analogy.py**
- **Functions**:
  - **`generate_analogy(text, concept)`**: Generates an analogy to explain a concept using Gemini AI
- **API Key Location**: Loaded from .env file

### 2. **backend/app.py**
- **Flask Routes**:
  - **`upload()`**: POST /upload - Handles PDF file uploads
  - **`explain()`**: GET /explain - Gets explanation for a concept
  - **`chat()`**: POST /chat - Handles chat questions
  - **`test()`**: POST /test - Generates test questions
  - **`evaluate_answers()`**: POST /evaluate - Evaluates student answers

### 3. **backend/doubtchat.py**
- **Functions**:
  - **`answer_question(conversation_history, question)`**: Answers questions based on conversation history
- **API Key Location**: Loaded from .env file

### 4. **backend/dummy.py**
- **Functions**: None (script-based execution)
- **Purpose**: Test script for generating BART system explanation
- **API Key Location**: Line 6

### 5. **backend/emotion_detection.py**
- **Functions**: None (main loop execution)
- **Purpose**: Real-time emotion detection using webcam and DeepFace
- **Key Features**:
  - Detects emotions: happy, sad, angry, fear
  - Outputs emotion data every 5 seconds
  - Uses OpenCV for face detection

### 6. **backend/evaluate.py**
- **Functions**:
  - **`evaluate_answers(prompt)`**: Evaluates student answers using Gemini AI
- **API Key Location**: Loaded from .env file

### 7. **backend/example.py**
- **Functions**:
  - **`generate_example(text, concept)`**: Generates examples to illustrate a concept
- **API Key Location**: Loaded from .env file

### 8. **backend/explanation.py**
- **Functions**:
  - **`generate_explanation(text, concept)`**: Generates in-depth explanation of a concept
- **API Key Location**: Loaded from .env file

### 9. **backend/flowchart.py**
- **Functions**:
  - **`generate_flowchart(text, concept)`**: Generates flowchart description for a concept
- **API Key Location**: Loaded from .env file

### 10. **backend/imp_concepts.py**
- **Functions**:
  - **`get_pdf_page_count(file_path)`**: Returns the number of pages in a PDF
  - **`extract_pdf_text_and_store(file_path)`**: Extracts text from all PDF pages
  - **`get_important_concepts(file_path, question)`**: Extracts important concepts from PDF using Gemini AI
- **API Key Location**: Loaded from .env file

### 11. **backend/qanda.py**
- **Functions**:
  - **`generate_questions(text, number, type, level, topic)`**: Generates test questions based on parameters
- **API Key Location**: Loaded from .env file

### 12. **backend/topicexplain.py**
- **Functions**:
  - **`get_explanation(text, concept)`**: Generates comprehensive explanation with analogy, example, and flowchart
- **API Key Location**: Loaded from .env file
- **Output Format**: Returns explanation, example, analogy, and Mermaid flowchart separated by "***"

---

## Frontend Directory Files

### 1. **frontend/abc.py**
- **Functions**: None (single print statement)

### 2. **frontend/mermaid.py**
- **Class**: `MermaidConverter` (identical to root mermaid.py)
  - **`__init__(self, output_dir: str = "output")`**
  - **`encode_mermaid(self, mermaid_code: str) -> str`**
  - **`get_mermaid_image(self, encoded_data: str) -> Optional[bytes]`**
  - **`save_image(self, image_data: bytes, output_filename: str) -> bool`**
  - **`convert(self, mermaid_code: str, output_filename: str) -> bool`**
- **Standalone Functions**:
  - **`read_mermaid_code(file_path: str) -> str`**

### 3. **frontend/topicexplain.py**
- **Functions**: None (main loop execution)
- **Purpose**: Real-time emotion detection using webcam (30-second intervals)
- **Key Features**:
  - Tracks 7 emotions: angry, disgust, fear, happy, sad, surprise, neutral
  - Outputs average emotions every 30 seconds
  - Uses OpenCV and DeepFace

### 4. **frontend/mermaid.js**
- **Functions**:
  - **`splitContentIntoSections(content)`**: Splits content into 4 sections separated by "***"
  - **`generateMermaidImage(mermaidContent)`**: Async function to generate Mermaid diagram image via API

### 5. **frontend/function splitContentIntoSections(conten.js**
- **Functions**:
  - **`splitContentIntoSections(content)`**: Splits content into sections
  - **`writeMermaidToFile(mermaidCode)`**: Writes Mermaid code to file (commented out)

---

## API Key Locations Summary

### Files with Hardcoded API Keys (need updating):
1. `animal.py` - Line 6
2. `animal_tales.py` - Line 6
3. `mythology.py` - Line 6
4. `mythology_fact.py` - Line 6
5. `nature.py` - Line 6
6. `science.py` - Line 6
7. `space.py` - Line 6
8. `backend/dummy.py` - Line 6

### Files using .env file (already configured):
1. `.env` - Line 1 (GEMINI_API_KEY)
2. `backend/analogy.py`
3. `backend/doubtchat.py`
4. `backend/evaluate.py`
5. `backend/example.py`
6. `backend/explanation.py`
7. `backend/flowchart.py`
8. `backend/imp_concepts.py`
9. `backend/qanda.py`
10. `backend/topicexplain.py`

---

## Technology Stack

- **Backend**: Node.js (Express), Python (Flask)
- **AI/ML**: Google Gemini AI, DeepFace, OpenCV
- **PDF Processing**: PyPDF2
- **Visualization**: Mermaid.js
- **WebSocket**: ws library for real-time emotion data
- **Frontend**: HTML, JavaScript

---

## Key Features

1. **PDF Analysis**: Extract and identify important concepts from PDFs
2. **AI-Powered Explanations**: Generate comprehensive explanations with analogies and examples
3. **Emotion Detection**: Real-time facial emotion detection during learning
4. **Interactive Chat**: Doubt clearing through conversational AI
5. **Assessment**: Generate and evaluate test questions
6. **Story Generation**: Create educational stories across multiple genres
7. **Flowchart Generation**: Visual representation of concepts using Mermaid diagrams
8. **Code Translation**: Translate code between programming languages
