# MMoF
Repo for working with the course [Mathematical Modelling of Football](https://uppsala.instructure.com/courses/65231).

## Installation

### Simple, for usage
To pip install the latest version of py-tools for usage in another project
```
pip install XXX 
```

### For development
To pip install py-tools for development, first clone to the py-tools repo to your computer. 
```
git clone 
```
Then, in the py-tools folder, pip install py-tools in editable mode, including the developer dependencies.
```
pip install --editable .['dev']
```
For development work, to avoid problems with conflicting dependency requirements, we recommend installing py-tools in a clean virtual environment, see further information below on how to create a virtual environment.
If developing in the VS Code IDE, the .vscode/__recommended_settings.json file can be used as a base for configuring the dataframe-explorer project in VS Code. To apply it in your VS Code project, copy the content into a file named .vscode/settings.json.

##### Virtual Environment

A Python virtual environment can be used to create a development environment that is independent and isolated from the "system" Python environment on the computer.

On Mac, to create a virtual environment called `venv`.
```
python3 -m venv venv
source venv/bin/activate
```
On Windows
```
python -m venv venv
venv/Scripts/activate.bat
```
The new virtual environment contains only the most basic Python packages (pip and setuptools). Type:
`pip list`
to confirm that only pip and setuptools are installed. Update these packages to the latest version by typing:
```
pip install --upgrade pip
pip install --upgrade setuptools
```
Now install the py-tools package in editable mode and including the developer dependendcies, as described above.
```
pip install --editable .['dev']
```

To uninstall all packages in the virtual environment, type:
```
pip uninstall -y -r <(pip freeze)
```
##### Testing

Pytest is used for testing. To run the tests, type:
```
pytest
```
or try, e.g.:
```
pytest --cov-report term-missing --cov="src"
```
to get a test coverage report as output as well.