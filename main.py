from app import create_app
from app.config import DEBUG

if __name__ == "__main__":
    app = create_app()

    app.run(port=8080, debug=DEBUG)
