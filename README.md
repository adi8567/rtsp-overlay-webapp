# RTSP Livestream Overlay Web Application

## A web-based application that allows users to play a livestream video and add custom overlays (text and images) on top of the video in real time. Users can create, move, resize, update, and delete overlays dynamically.

This project was built as part of an internship assignment to demonstrate skills in frontend development, backend APIs, real-time UI interaction, and data persistence.

# 🚀 Features
## 🎥 Livestream Playback

Play / Pause controls

Volume control

Fullscreen support

HLS playback (RTSP supported via conversion pipeline)

## 🖊 Overlay System

Text overlays

Image overlays (via image URL)

Drag-and-drop positioning

Resizable overlays

Real-time updates

Delete overlays

## ⚙ Backend

REST APIs for overlay management

SQLite database (free, local, no cloud dependency)

CORS-enabled

Flask-based server

## 🎨 Frontend

React-based UI

Interactive overlay canvas

Modern UI styling

## 📁 Project Structure
```
rtsp-overlay-app/
│
├── frontend/
│ └── React application
│
├── backend/
│ ├── app.py
│ ├── overlays.db
│ └── static/
│
└── README.md
```
## 🛠 How to Run the Project Locally

## 1️⃣ Clone the Repository
```
git clone <your-github-repo-url>
cd rtsp-overlay-app
```

## 🔙 Backend Setup

## Step 1: Create Virtual Environment (Optional but Recommended)
```
cd backend
python -m venv venv
venv\Scripts\activate
```
## Step 2: Install Dependencies
```
pip install flask flask-cors
```
## Step 3: Run Backend Server
```
python app.py
```
## Backend will run on:
```
http://127.0.0.1:5000
```
## Test API:
```
http://127.0.0.1:5000/api/overlays/
```
# 🎨 Frontend Setup

## Step 1: Install Dependencies
```
cd frontend
npm install
```
## Step 2: Start React App
```
npm start
```
## Frontend will run on:
```
http://localhost:3000
```
## 🧑‍💻 Using the Application

## ➕ Adding an Overlay

Select overlay type (Text or Image)

Enter content (text or image URL)

Click Add Overlay

## 🖱 Moving an Overlay

Drag the overlay to any position on the video

## 🔲 Resizing an Overlay

Drag from the edges or corners

## ❌ Deleting an Overlay

Click the ❌ button on the overlay

## ▶ Video Controls

Play / Pause

Volume

Fullscreen

## 📡 RTSP Support (How It Works)
Browsers do not support RTSP streams directly.
Pipeline:
```
RTSP Stream → FFmpeg → HLS (.m3u8) → HTML5 Video Player
```
Currently, a demo HLS stream is used for testing. RTSP input and FFmpeg pipeline can be added for real-time RTSP sources.

## 📘 API Documentation
🔹 Get All Overlays

GET /api/overlays/

Response:
```
[
{
"id": 1,
"x": 100,
"y": 80,
"width": 200,
"height": 100,
"content": "Hello",
"type": "text"
}
]
```
🔹 Create Overlay

POST /api/overlays/

Request Body:
```
{
"x": 50,
"y": 50,
"width": 150,
"height": 80,
"content": "Sample",
"type": "text"
}
```
🔹 Update Overlay

PUT /api/overlays/{id}

Request Body (partial allowed):
```
{
"x": 120,
"y": 100
}
```
🔹 Delete Overlay

DELETE /api/overlays/{id}


## 🎬 Demo Video (Mandatory for Submission)

The demo video should include:

Starting backend and frontend

Playing the livestream

Adding text overlay

Adding image overlay

Dragging overlays

Resizing overlays

Deleting overlays

Demonstrating real-time behavior

## 👤 Author

Aditya

