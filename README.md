# **Dyslexi-AI: Early Detection and Therapy with Multi Feature**

## **Overview**

**Dyslexi-AI** is a gamified platform designed to assist in the early detection and therapy for dyslexia. The platform leverages educational games to track a user's progress, adjust difficulty levels dynamically using Q-learning, and provide personalized feedback. It includes various interactive games aimed at improving the skills of dyslexic students, such as the **Phonics Game**, **Rhyme Race**,  and others, while focusing on learning and cognitive development.

The platform also includes a comprehensive system for tracking user performance, awarding badges, providing a leaderboard, and offering personal dashboards with graphs that show overall improvement across games.

## **Key Features**

- **Q-learning-powered Difficulty Adjustment**: Dynamic difficulty adaptation based on user performance.
- **Multilingual Support**: The platform supports multiple languages (English, Kannada, Hindi) to cater to a diverse user base.
- **Gamification**: Includes badges, points, daily streaks, and weekly challenges to motivate users.
- **User Performance Tracking**: Detailed user dashboards displaying progress, performance, and earned badges.
- **Leaderboard**: Display users' points, accuracy, and rankings across games.
- **Interactive Educational Games**: Games like Phonics, Rhyme Race, and Sequence Sorter are designed to help with dyslexia therapy.

## **Technologies Used**

- **Frontend**: React, Tailwind CSS
- **Backend**: Node.js, Express.js, MongoDB
- **Database**: MongoDB (for storing user stats, points, accuracy, and badges)
- **Game Logic**: Q-learning algorithm for dynamic difficulty adjustment
- **Authentication**: JWT (JSON Web Tokens) for user authentication

## **SDG Applicable**
### 🎯 SDG 3: Good Health and Well-being
Target 3.4: Promote mental health and well-being.

Your project contributes to early detection of learning disabilities like dyslexia and provides accessible therapeutic tools, reducing the learning gap and supporting mental well-being in children.
### 🎯 SDG 4: Quality Education
Target 4.1: Ensure inclusive and equitable quality education.

Target 4.5: Eliminate gender disparities and ensure equal access to education for vulnerable groups, including persons with disabilities.

Dyslexi-AI empowers children with learning difficulties to improve their reading and cognitive skills through fun and adaptive learning tools, supporting inclusive education.
---

## **Project Structure**

```bash
project-root/
├── chatbotserver/
│   ├── app.py
│   ├── chatbot.py
│   ├── main.py
├── dyslexia/
│   ├── app/
│   ├── components/
│   ├── context/
│   ├── lib/
│   ├── models/
│   ├── public/
│   ├── utils/
│   ├── node_modules/
│   ├── .next/
│   ├── .gitignore
│   ├── components.json
│   ├── eslint.config.mjs
│   ├── jsconfig.json
│   ├── next.config.mjs
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.mjs
│   ├── README.md
│   ├── scene.splinecode
├── serverpy/
│   ├── model/
│   ├── temp_uploads/
│   ├── dyslexia_model.pkl
│   ├── main.py
│   ├── requirements.txt
│   ├── temp_recording.webm
│   ├── Untitled.ipynb
```
## **How to Run Project Locally**
### 1. Clone the Repository
```bash
git clone https://github.com/Ganapaved/Dyslexia-Buddy.git
cd Dyslexi-AI
```
### 2. Install Dependencies
#### Prerequisites
Make sure you have the following installed:
- Python (version 3.8+ recommended)
- Node.js and npm
```bash
python --version
node --version
npm --version
```
#### 1. Backend Setup
Navigate to the ```serverpy``` directory:
```bash
cd serverpy
```
Install the Python dependencies:
```bash
pip install -r requirements.txt
```
Run the server:
```bash
python main.py
```
#### 2.  Setting up chatbotserver
Navigate to the ```chatbotserver``` directory:
```bash
cd ../chatbotserver
```
If you encounter CORS errors, install Flask-CORS:
```bash
pip install flask-cors
```
Run the server:
```bash
python main.py
python app.py
```
#### 3.Frontend Setup(Next.js app)
Navigate to the dyslexia directory:
```bash
cd ../dyslexia
```
Install the Node.js dependencies:
```bash
npm install
```
Run the development server:
```bash
npm run dev
```
The frontend will be available at [http://localhost:3000](http://localhost:3000/).




