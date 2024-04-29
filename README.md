saugatucket-fish-passage
==============================

Processing and analysis of fish passage data along the Saugatucket River, RI.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

Certainly! Here's the revised version with instructions tailored for Windows users:

---

## Cloning the GitHub Repository

To clone this GitHub repository to your local machine on Windows, follow these steps:

1. Open Command Prompt or PowerShell.
2. Navigate to the directory where you want to clone the repository using the `cd` command. For example:

```bash
cd path\to\desired\directory
```

3. Use the following command to clone the repository:

```bash
git clone https://github.com/gtdang/saugatucket-fish-passage.git
```

4. Once the cloning process is complete, navigate into the cloned repository directory:

```bash
cd repository-name
```

## Creating a Python Environment

This repository contains a `.tool-versions` file and a `requirements.txt` file to manage the Python environment using `pyenv` and `pip`. Follow these steps to create a Python environment on Windows:

1. Ensure you have `pyenv-win` installed on your system. If not, you can download and install it from the [pyenv-win GitHub releases page](https://github.com/pyenv-win/pyenv-win/releases).

2. Once `pyenv-win` is installed, navigate to the cloned repository directory in Command Prompt or PowerShell.

3. Use the following command to set up the Python version specified in the `.tool-versions` file:

```bash
pyenv install $(type .tool-versions)
```

This will install the Python version specified in the `.tool-versions` file if it's not already installed on your system.

4. After installing the required Python version, use the following command to create a virtual environment and activate it:

```bash
pyenv virtualenv $(type .tool-versions) <environment-name>
```

Replace `<environment-name>` with the desired name for your virtual environment.

5. Activate the virtual environment by running:

```bash
pyenv local <environment-name>
```

6. Finally, install the Python dependencies listed in the `requirements.txt` file using `pip`:

```bash
pip install -r requirements.txt
```

Now you have successfully created a Python environment and installed the required dependencies for this repository on Windows.

---

These instructions should help Windows users set up the environment effectively. Let me know if you need further assistance!


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
