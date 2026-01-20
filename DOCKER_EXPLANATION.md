# Dockerfile Logic Explanation

The `Dockerfile` is now set up as a **multi-stage build**. This is a best practice to keep the final image size small and secure.

## Stage 1: Builder (`FROM ... AS builder`)

1.  **Purpose**: This stage is used solely to prepare dependencies.
2.  **Steps**:
    - It starts from `python:3.9-slim`.
    - It copies `requirements.txt` and runs `pip install` to install dependencies into the system locations (which will be `/usr/local` in the container).
    - We do this here so we can simply _copy_ these installed packages to the next stage, leaving behind any build tools or cache files (like `gcc` or pip cache) that might have been used.

## Stage 2: Final Image (`FROM ...`)

1.  **Purpose**: This is the actual image that we will run.
2.  **Arguments & Environment**:
    - We re-declare `ARG`s (like `WORKDIR`, `SRC_PATH`) because `ARG`s are scoped to the build stage they are in.
    - We set `ENV` variables so the running application can access them (e.g., `PORT`, `MAIN_EXECUTABLE`).
3.  **Setup**:
    - **User**: We create a non-root user `appuser` for security. Running as root is dangerous.
    - **Dependencies**: We copy the installed Python packages from the `builder` stage:
      ```dockerfile
      COPY --from=builder /usr/local /usr/local
      ```
      This gives us the Python libraries without the build overhead.
    - **System Tools**: We install `curl` (via `apt-get`) because it's often needed for health checks, but we clean up apt lists immediately to save space.
4.  **Code Copy**:
    - We copy the application code (`src`, `test`, `README.md`) and change ownership to `appuser` simultaneously.
5.  **Execution**:
    - We switch to `USER appuser`.
    - We expose the port.
    - Finally, we run the python script defined by `MAIN_EXECUTABLE`.
