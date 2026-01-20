# Python Boilerplate

[![Use this template](https://img.shields.io/badge/Use%20this%20template-238636?style=for-the-badge&logo=github)](https://github.com/new?template_name=oc-python-template&template_owner=orbitcluster)

A production-ready Python boilerplate designed to be used as a GitHub Template. It comes pre-configured with Docker support, CI/CD pipelines, and best practices for modern Python development.

## 🚀 Features

- **Dockerized**: Optimized Dockerfile with multi-stage builds, non-root user, and signal handling.
- **CI/CD Ready**:
  - `pre-commit` workflow for code quality checks.
  - Semantic Versioning automation.
  - Reusable workflow integration.
- **Best Practices**:
  - `.dockerignore` and `.gitignore` configured.
  - `.python-version` for consistent environment setup.
  - Security focused (non-root container user).

## 🛠️ Getting Started

To use this template for your own project:

1.  Click the **[Use this template](https://github.com/new?template_name=oc-python-template&template_owner=orbitcluster)** button at the top of the repository.
2.  Create a new repository from this template.
3.  Clone your new repository locally:
    ```bash
    git clone https://github.com/your-username/your-new-repo.git
    cd your-new-repo
    ```

## 📦 Prerequisites

- **Python 3.13+** (Managed via `.python-version`)
- **Docker** (for containerized development)

## 💻 Local Development

1.  **Create a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:

    ```bash
    # Adjust the path if your entry point differs
    python src/api/server.py
    ```

4.  **Run Tests**:
    ```bash
    python -m unittest discover test
    ```

## 🐳 Docker Support

This project includes a production-grade `Dockerfile`.

### Build the Image

```bash
docker build -t my-python-app .
```

### Run the Container

```bash
docker run -p 5000:5000 --rm my-python-app
```

### Optimizations Included

- **`.dockerignore`**: Excludes `venv`, `.git`, and `__pycache__` for smaller builds.
- **Multi-stage Build**: Keeps the final image minimal.
- **Security**: Runs as a non-root user (`appuser`).
- **Signal Handling**: Uses `exec` to ensure graceful shutdowns.
- **Caching**: `pip` runs with `--no-cache-dir` and `--no-compile` to reduce size.

## 🐙 Docker Compose

For a simplified local development experience, use `docker compose`:

1.  **Build and Run**:

    ```bash
    docker compose up --build
    ```

2.  **Run in Background**:

    ```bash
    docker compose up -d
    ```

3.  **Stop Containers**:
    ```bash
    docker compose down
    ```

The service is mapped to port `5000` and mounts the `./src` directory for easier development.

## 🔄 CI/CD Workflows

Found in `.github/workflows/`:

- **`pre-commit.yml`**: Runs on Pull Requests to `main`. It sets up Python 3.13 and runs pre-commit checks.
- **`version.yml`**: Automates semantic versioning on push to `main`.
- **`main.yml`** (disabled): Example of a deployment workflow using reusable actions.

## 📂 Project Structure

```text
.
├── .github/            # GitHub Actions workflows
├── src/                # Source code
│   └── api/            # API endpoints (server.py)
├── test/               # Unit tests
├── .dockerignore       # Docker build exclusions
├── .gitignore          # Git exclusions
├── .python-version     # Python version definition (3.13)
├── Dockerfile          # Container definition
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```
