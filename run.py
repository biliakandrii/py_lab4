from app import app  # Замініть "your_app" на ім'я вашого Flask-додатку

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
