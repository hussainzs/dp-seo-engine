# DP SEO Engine

**RAG-based SEO Optimizer** that leverages internal style guides and SEO optimization rules to generate URL slugs, tags, and other functionalities for articles written by the Daily Pennsylvania Inc.

This project uses **Retrieval-Augmented Generation (RAG)** with **LLMs** to provide SEO guidance to the editorial team by combining internal style guides with advanced SEO techniques. The system takes in PDFs, CSV data, and external web documents, processes them, and offers suggestions for optimizing SEO performance.

## Project Structure

```bash
your_project/
├── README.md
├── .gitignore                # Excludes unnecessary files from version control
├── pyproject.toml            # Poetry project configuration
├── src/                      # All source code is located here
│   ├── __init__.py           # Marks the directory as a Python package
│   ├── app.py                # Main application ENTRY POINT (run this)
│   ├── chain.py              # Defines the LLM chain and retrieval logic
│   ├── data_loader.py        # Functions to load PDFs, CSVs, and web data
│   ├── prompt.py             # Defines the prompt template for the LLM
│   ├── text_splitter.py      # Splits long documents into smaller chunks
│   ├── ui.py                 # Contains the Gradio UI logic for interaction
│   └── vector_store.py       # Handles vector storage and retrieval using Chroma
├── files/
│   ├── 34_Style.pdf
│   ├── All_Style.pdf
│   ├── DEI_Style.pdf
│   ├── Sports_Style.pdf
│   ├── organic_search.csv
├── .env                      # Environment variables (API keys, etc.)
```

### File Descriptions

- **README.md**: Documentation for the project setup, structure, and usage guidelines.
- **.gitignore**: Excludes unnecessary files like virtual environments, `.env`, and cache files from version control.
- **pyproject.toml**: Defines dependencies and project configurations using Poetry.
- **src/**: Contains the source code for the project.
  - **app.py**: Main entry point for the application. Sets up data loading, vector stores, and launches the Gradio UI.
  - **chain.py**: Sets up the language model chain that interacts with the LLM to generate responses. Integrates vector retrieval.
  - **data_loader.py**: Contains functions to load documents from CSVs, web URLs, and PDFs.
  - **prompt.py**: Defines the template for the LLM prompt, ensuring the correct format for SEO-optimized output.
  - **text_splitter.py**: Splits documents into smaller chunks to be processed by the LLM.
  - **ui.py**: Contains the Gradio UI setup, which provides an interface for users to interact with the system.
  - **vector_store.py**: Manages the creation of vector databases using Chroma to store and retrieve document embeddings.
- **data/**: Contains the files and data inputs for the system.
  - **files/**: Includes all style guide PDFs used for content generation.
  - **organic_search.csv**: CSV file with SEO-related data, such as organic search data, used for vector retrieval.
- **.env**: Contains sensitive information like API keys. This file is not included in version control for security purposes.

## Setup Guide

Follow the steps below to clone, set up, and run the project. The setup involves using **Poetry** for dependency management and a virtual environment for isolation.

### Step 1: Install Poetry

Poetry is a dependency manager for Python that helps in project management and ensures consistency across environments.

1. **Install Poetry**:

   If Poetry is not installed, follow these instructions:

   - For Unix/macOS:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```
   - For Windows (Powershell):
     ```powershell
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
     ```

2. **Verify the installation**:
   ```bash
   poetry --version
   ```

   If you see the version number, Poetry is successfully installed.

### Step 2: Clone the Repository

To get started, clone the project repository:

```bash
git clone https://github.com/yourusername/your_project.git
cd your_project
```

### Step 3: Set Up the Virtual Environment

Poetry automatically manages virtual environments for each project. To create and activate the environment:

1. **Install dependencies**:
   ```bash
   poetry install
   ```

2. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

   This will spawn a new shell with the project's virtual environment activated.

3. **Set Python interpreter (for VS Code users)**:

   - Open VS Code.
   - Press `Ctrl + Shift + P` and type `Python: Select Interpreter`.
   - Select the interpreter created by Poetry, which should be located in the `.venv/` directory.

### Step 4: Set Up Environment Variables

You will need to configure environment variables (e.g., API keys). These should be placed in the `.env` file in the project root. For example:

**`.env`**:

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

Make sure to replace `your_api_key_here` with your actual API key for the Anthropic model.

### Step 5: Running the Application

Once everything is set up, you can run the application as follows:

```bash
python src/app.py
```

This will launch the Gradio UI, allowing you to interact with the SEO optimizer.

## Contribution Guidelines

To contribute to this project, please follow these steps:

1. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**, ensuring they adhere to the coding standards.

3. **Commit your changes** with a meaningful commit message:
   ```bash
   git commit -m "Add feature: your-feature-name"
   ```

4. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a pull request** to merge your changes into the main branch.

## Best Practices

- **Follow the project structure** to maintain consistency across the codebase.
- **Use Poetry** for adding/removing dependencies:
  - To add a new dependency:
    ```bash
    poetry add package_name
    ```
  - To remove a dependency:
    ```bash
    poetry remove package_name
    ```
- **Test your changes** before pushing to the repository.

## Troubleshooting

If you encounter issues while setting up or running the project:

1. **Virtual Environment Not Activated**:
   - Ensure you're in the Poetry shell by running:
     ```bash
     poetry shell
     ```

2. **Dependencies Not Installed**:
   - If dependencies are not installed, try:
     ```bash
     poetry install
     ```

3. **API Issues**:
   - Verify that your `.env` file contains the correct API keys.

## Additional Resources

- **Poetry Documentation**: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
- **Gradio Documentation**: [https://gradio.app/docs/](https://gradio.app/docs/)
- **LangChain Documentation**: [https://langchain.com/docs/](https://langchain.com/docs/)

---