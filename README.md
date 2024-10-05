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
- **files/**: Contains the files (pdfs, csv etc) that are used for RAG

## Setup Guide

Follow the steps below to clone, set up, and run the project. The setup involves using **Poetry** for dependency management and a virtual environment for isolation. Poetry is the standard in modern python dependency management, resolution and handling virtual environments.

### Step 1: Install Poetry

Poetry is a dependency manager for Python that helps in project management and ensures consistency across environments.

1. **Install Poetry**:

   Follow these guidelines to install poetry for your system:
   - https://python-poetry.org/docs/
   - Make sure to add Poetry to your PATH variable (just a reminder to not skip this step during installation)

2. **Verify the installation**:
    Open shell or terminal and run
   ```bash
   poetry --version
   ```

   If you see the version number, Poetry is successfully installed.

### Step 2: Clone the Repository

To get started, clone the project repository:

```bash
git clone https://github.com/hussainzs/dp-seo-engine.git
cd dp-seo-engine
```

### Step 3: Set Up the Virtual Environment

Poetry automatically manages virtual environments for each project. To create and activate the environment:

1. **Configure Poetry to create the virtual environment in the project directory**:
   
   Before installing dependencies and activating the environment, run the following command to ensure that the virtual environment is created inside your project folder (i.e., in `.venv/`):

   ```bash
   poetry config virtualenvs.in-project true
   ```

   This command tells Poetry to always place the virtual environment inside a `.venv/` folder within the project directory. This is optional but helps setting up the interpreter and organizing overall.

2. **Proceed with the installation**:

   After setting the configuration, you can continue with the following commands:
   
   ```bash
   poetry install
   poetry shell
   ```

3. **Set the correct Python Interpreter**:

    To ensure vs code uses the correct python interpreter, follow these steps:

    - Type and select Python: Select Interpreter.
    - Paste the path to the virtual environment python interpreter.

    If you are using VS Code, you can also set the interpreter by clicking on the interpreter name in the bottom left corner and selecting the virtual environment created by Poetry.

    If you are unsure where your path is, you can find it by running the following command in the terminal:

    ```bash
    poetry env info --executable
    ```


### Step 4: Set Up Environment Variables

You will need to configure environment variables (e.g., API key). These should be placed in the `.env` file in the project root. For example:

**`.env`**:

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

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