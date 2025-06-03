# roominator

**Generative Layouts for Small-Scale Housing**

Welcome to **roominator** — your backend buddy that helps generate smart housing layouts by turning plot specs and room needs into a preliminary floorplan! Built with Python and FastAPI, this project is a playground for mixing architecture, geometry, and backend wizardry.

---

## 🚀 Tech Stack

- Python 3.10+
- FastAPI – for blazing-fast APIs
- Pydantic – for clean, strict data validation
- Uvicorn – ASGI server for local development
- (Coming soon): SVG-based layout visualizations

---

## 🏗️ What Does It Do?

- Accepts plot dimensions and setback rules
- Accepts a list of rooms with minimum area requirements
- Calculates buildable area based on setbacks
- Automatically places rooms using a simple greedy packing algorithm
- Returns 2D positions (x, y) and dimensions (width, depth) of each placed room

---

## 🧠 How It Works
### 📦 Modular project structure:
      ```bash
      generative-housing-backend/
      ├── main.py                         # FastAPI app setup
      ├── api/
      │   └── layout_routes.py            # API routing logic
      ├── services/
      │   └── layout_generator.py         # Core layout generation logic
      ├── models/
      │   └── schemas.py                  # Pydantic models for validation
      
   The layout engine (layout_generator.py) calculates room placement within the buildable zone using a row-wise packing method (like Tetris but for homes 🏡).


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
   Sample Input Payload for /generate-layout:
    ```bash
    POST to /generate-layout
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
-  Geometry engine to compute layout
-  Room adjacency & clustering logic
-  Orientation-aware planning
-  SVG layout visualizer (in progress!)
-  AI optimization for better space utilization
-  Frontend to visualize layout results

## 🦾 Why “roominator”?
- Because it terminates indecision in early design layouts 😉
- Simple, modular, and ready to help architects and developers explore design possibilities — fast.

## 💬 Contributions & Feedback
- Got ideas? Found a bug?
- Feel free to open an issue or submit a PR — feedback is welcome!

Made with ❤️ by Swetha — part architect, part coder, turning blueprints into bytes!
