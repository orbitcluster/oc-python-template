# Python Boilerplate

This is a Python boilerplate project that can be used as a GitHub template. It includes a basic structure, tests, and Docker support.

## Structure

- `src/`: Source code directory
- `test/`: Test code directory
- `Dockerfile`: Docker configuration
- `requirements.txt`: Project dependencies

## Usage

### Local Development

1.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2.  Run the application:

    ```bash
    python src/main.py
    ```

3.  Run tests:
    ```bash
    python -m unittest discover test
    ```

### Docker

1.  Build the Docker image:

    ```bash
    docker build -t my-python-app .
    ```

2.  Run the Docker container:
    ```bash
    docker run --rm my-python-app
    ```
