# roominator

**Generative Layouts for Small-Scale Housing**

Welcome to **roominator** — your backend buddy that helps generate smart housing layouts by turning plot specs and room needs into a preliminary floorplan! Built with Python and FastAPI, this project is a playground for mixing architecture, geometry, and backend wizardry.

---

## 🚀 Tech Stack

- Python 3.10+
- FastAPI (for lightning-fast APIs)
- Pydantic (for data validation)
- Uvicorn (ASGI server)

---

## 🏗️ What Does It Do?

- Takes plot dimensions and setback rules  
- Accepts a list of rooms with minimum area requirements  
- Prepares the ground for generating room layouts (coming soon!)  
- Provides an API endpoint `/generate-layout` that accepts layout specs and returns room info  

---

## ⚡ How to Run Locally

1. Clone the repo:  
   ```bash
   git clone https://github.com/SwethaVijayaraju/generative-housing-backend.git
   cd generative-housing-backend

2. Create and activate a virtual environment: 
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows

3. Install dependencies: 
   ```bash
   pip install fastapi uvicorn

4. Start the FastAPI server: 
   ```bash
   uvicorn main:app --reload

5. Open http://localhost:8000/docs to explore and test the API!

## 🧩 Sample Input Payload for /generate-layout
    ```bash
    {
    "plot": { "width": 30, "depth": 40 },
    "setbacks": { "front": 5, "back": 5, "sides": 3 },
    "rooms": [
      { "type": "bedroom", "min_area": 120 },
      { "type": "kitchen", "min_area": 80 },
      { "type": "bathroom", "min_area": 50 }
    ],
    "orientation": "north"
    }

## 🔭 What’s Next?
- Geometry engine to calculate buildable area and smartly place rooms
- Room adjacency and orientation logic
- Visualization support (maybe SVG or simple web front-end)
- AI-driven optimization to maximize space utility

## 🦾 Why “roominator”?
- Because it helps automate room layouts — a simple backend tool inspired by architecture, built to make early-stage housing design easier.

## 💬 Contributions & Feedback
- Got ideas, found a bug, or just want to say hello?
- Feel free to open an issue or submit a pull request — your input makes this project better!

Made with ❤️ by Swetha — part architect, part coder, all about turning blueprints into bytes and having fun doing it!
