
# PRailgun

**PRailgun** is a lightweight public relations tool designed to simplify crafting professional media inquiries. Built with Flask and OpenAI, it generates tailored inquiries using client-provided details and custom instructions.

## Features

- **Client Details Form**: Input client name, DBA (Doing Business As), industry, and custom instructions.
- **AI-Powered Inquiries**: Leverages OpenAI's GPT-4 to generate personalized media inquiries.
- **Dockerized Deployment**: Quick and easy setup with Docker and Docker Compose.
- **Environment Management**: Securely manage API keys using `.env` files.

## Requirements

- Docker & Docker Compose
- Python 3.9+ (for local development)
- Poetry (optional, for local development)

## Installation

### Using Docker

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DJStompZone/prailgun.git
   cd prailgun
   ```

2. **Set up environment variables**:
   Copy `.env.example` to `.env` and add your OpenAI API key:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and replace `your_openai_api_key` with your OpenAI API key:

   ```yaml
   OPENAI_API_KEY=your_openai_api_key
   ```

3. **Build and run the Docker container**:

   ```bash
   docker-compose up --build
   ```

4. **Access the application**:
   Visit `http://localhost:5000` in your browser.

### Local Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DJStompZone/prailgun.git
   cd prailgun
   ```

2. **Install dependencies**:
   Install Poetry if not already installed, and use it to install dependencies:

   ```bash
   poetry install
   ```

3. **Set up environment variables**:
   Copy `.env.example` to `.env` and add your OpenAI API key:

   ```bash
   cp .env.example .env
   ```

4. **Run the application**:

   ```bash
   poetry run flask run
   ```

5. **Access the application**:
   Visit `http://localhost:5000` in your browser.

## Usage

1. **Open the app**: Launch the app in your browser.
2. **Fill out the form**:
   - **Client Name**: The name of your client.
   - **DBA (Doing Business As)**: The client's alternate business name (if applicable).
   - **Industry**: The client's business industry.
   - **Custom Instructions**: Optional (up to 250 characters).
3. **Generate the inquiry**: Click "Generate Email" to create a professional media inquiry.
4. **Review the result**: The generated inquiry will appear in the output section.

## File Structure

```plaintext
prailgun/
├── app.py                 # Main Flask application
├── Dockerfile             # Docker build file
├── docker-compose.yml     # Docker Compose setup
├── .env.example           # Example environment variables
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Poetry configuration
├── README.md              # Project README
└── templates/
    └── index.html         # Frontend form template
```

## Development

To modify or extend the app:

1. **Install dependencies**:

   ```bash
   poetry install
   ```

2. **Run locally**:

   ```bash
   poetry run flask run
   ```

3. **Lint and format**:

   ```bash
   poetry run black .
   poetry run flake8
   ```

## Deployment with Docker

The included `Dockerfile` and `docker-compose.yml` make it easy to deploy the application:

1. **Build the Docker image**:

   ```bash
   docker build -t prailgun .
   ```

2. **Run the container**:

   ```bash
   docker run -p 5000:5000 --env-file .env prailgun
   ```

3. **Use Docker Compose**:

   ```bash
   docker-compose up --build

