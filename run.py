from app import app
from dotenv import load_dotenv
import os

load_dotenv()
app.run(debug=os.getenv("DEBUG"))
