# Global Chat Platform

A real-time global chat application built with Flask, Flask-SocketIO, and Redis.

## Features

- Multi-user chat in a single global room
- Real-time messaging with WebSockets
- Redis message queue for horizontal scaling

## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/saipavank63/global-chat-platform.git
   cd global-chat-platform
   ```

````
2. Install dependencies:
   ```bash
pip install -r requirements.txt
````

3. Configure environment variables in a `.env` file:
   ```dotenv
   SECRET_KEY=your_secret_key
   REDIS_URL=redis://localhost:6379/0
   ```

````
4. Run the app:
   ```bash
python app.py
````

5. Open http://localhost:5000 in your browser.

## Docker

```bash
docker build -t global-chat-platform .
docker run -p 5000:5000 --env-file .env global-chat-platform
```
