### Requirements
To launch the project we need Python version >= 3.8.5
It is recommended to use a virtual environment. See the [documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment).
The following dependencies should be installed. Go to the project repository and run the following command: 
```bash
pip install -r requirements.txt
```

### Launching the script

To get the French numbers (as they exist in France) run the following command from the project repository:
```bash
python main.py --from_france
```

To get the French numbers (outside of France) run the following command from the project repository:
```bash
python main.py
```

### Running tests
Run this command from the project repository:
```bash
pytest
```