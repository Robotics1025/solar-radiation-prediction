import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

print("Loading Group_notebook_updated.ipynb...")
with open('Group_notebook_updated.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

print("Executing the notebook... This may take about a minute.")
try:
    ep.preprocess(nb, {'metadata': {'path': './'}})
    print("Execution successful!")
    
    with open('Group_notebook.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Saved completed notebook to Group_notebook.ipynb.")
except Exception as e:
    print(f"Error executing notebook: {e}")

