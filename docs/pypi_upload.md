---
layout: default
title: PyPi Upload
parent: Programmer's Guide
nav_order: 1
---
# Uploading a new NOMAD-CAMELS version to PyPi
The "backbone" of creating the PyPi project is the `pyproject.toml` file located in the root directory. Here almost all important settings are configured. The dependencies on other python packages is maintained with the `requirements.txt` file. \
The `MANIFEST.in` file contains information about static non-python files that should be included (e.g. folders of images). 

## Workflow
1. Make your desired changes in the `nomad_camels` folder (the main app folder). 
2. Run `python -m build` in the folder where the `pyproject.toml` file is located (should be located in the parent folder of the `nomad_camels` folder). This creates the succesfull builds (`nomad_camels-X.Y.Z.tar.gz` and `nomad_camels-X.Y.Z-py3-none-any.whl`) in `/dist/`.  \
   The folder structure should look something like this
   ```
   main_folder/
   |--- dist/
         --- Nomad_camels-X.Y.Z.tar.gz
         --- nomad_camels-X.Y.Z-py3-none-any.whl
   |--- pyproject.toml
   |--- requirements.txt
   |--- MANIFEST.in
   |--- nomad_camels/
         |--- MainApp.py
         |--- 'many other files' 
   ```
   where X.Y.Z is the version number given in the `.toml` file
3. To upload the builds to PyPi (**!currently uploads to TestPyPi during development!**) run:
    ```bash
    pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple nomad-camels
    ```
   The `extra-index-url` allows dependency installations from PyPi.\
   Now enter `__token__` as the username and enter your saved API token as the password to complete the upload.
4. The new version should then be available on https://test.pypi.org/project/nomad-camels/


<p style="text-align:left;">
  <span style="color: grey;">
  <a href="../index.html">&larr; Back</a>
  </span>
  <span style="float:right;">
    <a href="quick_start.html">Next &rarr;</a><br>
  </span>
</p>