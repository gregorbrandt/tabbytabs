# Variables
VENV = env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PROJECT_NAME = newworld

# Default target (run when you type `make`)
all: install

# Set up the virtual environment
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

# Install dependencies
install: $(VENV)/bin/activate
	$(PIP) install --upgrade pip
	$(PIP) install flake8 isort black pytest mkdocs
	$(PIP) freeze > requirements.txt

# Format code
format:
	$(VENV)/bin/black src/ test/
	$(VENV)/bin/isort src/ test/

# Lint code
lint:
	$(VENV)/bin/flake8 src/ test/

# Run test
test:
	$(VENV)/bin/pytest test/

# Serve documentation
docs:
	$(VENV)/bin/mkdocs serve

# Clean up temporary files
clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Initialize the project (one-time setup)
init: $(VENV)/bin/activate install
	@echo "Creating project structure..."
	mkdir -p src test docs data
	touch src/__init__.py test/__init__.py
	touch .gitignore README.md requirements.txt
	@echo "Adding default .gitignore..."
	@echo "env/" >> .gitignore
	@echo "__pycache__/" >> .gitignore
	@echo "*.pyc" >> .gitignore
	@echo ".DS_Store" >> .gitignore
	@echo "site/" >> .gitignore
	@echo "Initializing MkDocs..."
	$(VENV)/bin/mkdocs new docs
	@echo "Initializing Git repository..."
	git init
	git add .
	git commit -m "Initial commit: Project setup complete."
	@echo "Project setup complete!"

# Help command (list all available commands)
help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make format        - Format code with black and isort"
	@echo "  make lint          - Lint code with flake8"
	@echo "  make test          - Run test with pytest"
	@echo "  make docs          - Serve documentation with MkDocs"
	@echo "  make clean         - Clean up temporary files"
	@echo "  make init          - Initialize the project (one-time setup)"
	@echo "  make help          - Show this help message"