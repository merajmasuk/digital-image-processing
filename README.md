# Digital Image Processing
Course materials for Digital Image Processing course

### Prepare a notebook

1. Install Jupyter Notebook

```
sudo apt update && sudo apt install -y jupyter-notebook
```

2. Run notebook server

```
jupyter notebook
```

This will run the notebook server and open the working directory in the default browser

### Working with virtual environment(s)

1. Install python pip and venv modules

```
sudo apt update && sudo apt install -y python3-pip python3-venv
```

2. Create a virtual environment

```
python3 -m venv venv
```

3. Activate the virtual environment. This will modify your shell's PATH environment variable to use the Python executable and packages installed in the virtual environment.

```
source venv/bin/activate
```

On Windows, you can activate by the following (remember to unrestrict the script execution policy for your current user first)

```
venv\Scripts\activate.psql
```

Alternatiely, you can use `venv\Scripts\activate.bat`. But it's not reliable and may not always work on the modern versions of Windows.

4. Install ipykernel. This package provides the Jupyter Notebook kernel for the virtual environment.

```
pip install ipykernel
```

5. Add the virtual environment as a new kernel in Jupyter Notebook by running the following command:

```
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```

6. After opening a notebook, change the kernel from the menu and select `Python (venv)`.

### Tracking dependencies

While working on multiple devices, one may need to keep track of dependencies. The list of dependencies can be maintained with `pip freeze` command and a text file.

1. Activate the virtual environment

(Linux):
```
source venv/bin/activate
```

(Windows):
```
venv\Scripts\activate.psql
```

2. Install a package using pip:

```
pip install numpy
```

3. Generate the list of installed packages and extract the output to a text file.

```
pip freeze > requirements.txt
```

4. Later, on a different machine or environment, all the required packages can be installed using just one command

```
pip install -r requirements.txt
```

Last, but not the least, don't forget to update the `requirements.txt` file regularly after installing a new package
