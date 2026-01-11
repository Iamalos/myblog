from fasthtml.common import *
from monsterui.all import *
import uvicorn


# Initialize FastHTML app with MonsterUI
app, rt = fast_app(
    hdrs=(
        Theme.blue.headers(),  # MonsterUI theme
        Link(rel="stylesheet", href="/static/css/custom.css"),
    )
)

# Mount static files directory
from fasthtml.common import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

# Import and setup routes
from app.routes import setup_routes
setup_routes(app)


if __name__ == "__main__":
    print("Starting blog server at http://localhost:8000")
    print("Press Ctrl+C to stop")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
