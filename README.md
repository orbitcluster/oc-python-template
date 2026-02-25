# oc-python-template

This is a Cookiecutter template for generating new Python applications within Orbit Cluster. It sets up a production-ready Python project with Docker, CI/CD, Helm charts, and best practices baked in.

## 🚀 Prerequisites

To use this template, you'll need to have `cookiecutter` installed. If you don't have it installed, you can do so via `pip` or `brew`:

```bash
# Using pip
pip install cookiecutter

# Using Homebrew (macOS)
brew install cookiecutter
```

## 🛠️ Usage

Use the `cookiecutter` command pointing to this repository to scaffold a new project.

```bash
# From a local clone of this template:
cookiecutter path/to/oc-python-template

# Or directly from the GitHub repository:
cookiecutter https://github.com/orbitcluster/oc-python-template
```

### Configuration Prompts

You will be prompted to provide values for the following variables:

- **`applicationName`**: The name of your new application (e.g., `my-awesome-api`). This will be used as the root directory name and will populate placeholders in Helm configurations.
- **`orgId`**: Your Organization ID (default: `104`).
- **`buId`**: Your Business Unit ID (default: `1002`).
- **`appId`**: The specific Application ID for this new project (default: `1`).

### What Gets Generated?

Once generated, your new project directory (named after your `applicationName`) will contain:

- A fully structured Python application (`src/`, `test/`)
- A production-grade `Dockerfile` & `docker-compose.yml`
- Helm charts configured with your provided `orgId`, `buId`, `appId`, and `applicationName`.
- GitHub Action CI/CD workflows for versioning and validation.
- An application-specific `README.md` with instructions on how to run your new service locally.

## Development

If you're updating _this template_ itself:

1. Make your changes inside the `{{cookiecutter.applicationName}}` directory.
2. If you need to add more configurable parameters, add them to `cookiecutter.json`.
3. Reference those new parameters in your files using Jinja2 syntax: `{{ cookiecutter.myNewVariable }}`.
