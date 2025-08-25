import os
from dotenv import load_dotenv
from flask import Flask
from src.pogo_max_particle_optimizer import create_app

app: Flask = create_app()

if __name__ == "__main__":
    load_dotenv(override=True)
    env = os.getenv("DEBUG")
    debug = bool(env) if env else False
    app.run(host="0.0.0.0", debug=debug)
