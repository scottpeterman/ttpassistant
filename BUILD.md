# Build and Publish Guide

This guide explains how to build a Python wheel for **Visual TTP Assistant**, install the package from the wheel, and publish it to PyPI.

## 1. Build the Wheel

To build the wheel for the project, follow these steps:

### 1.1. Install `setuptools` and `wheel`

Ensure that you have `setuptools` and `wheel` installed in your Python environment. You can install them using `pip`:

```bash
pip install setuptools wheel
```

### 1.2. Build the Wheel

From the root of the project directory (where the `setup.py` file is located), run the following command to build the source distribution (`sdist`) and the wheel (`bdist_wheel`):

```bash
python setup.py sdist bdist_wheel
```

This will create two files inside the `dist/` directory:
- A `.tar.gz` source distribution file
- A `.whl` wheel file

For example, the output files in the `dist/` folder might look like this:
```text
dist/
    ttp_assistant-0.1.0.tar.gz
    ttp_assistant-0.1.0-py3-none-any.whl
```

---

## 2. Install from Wheel

After building the wheel, you can install it locally to test the package.

### 2.1. Install the Wheel Locally

To install the package from the generated wheel file, use the `pip install` command with the path to the `.whl` file:

```bash
pip install dist/ttp_assistant-0.1.0-py3-none-any.whl
```

This will install the package on your local machine. You can verify the installation by running the package:

```bash
ttp_assistant  # Assuming the entry point is correctly set up
```

---

## 3. Publish to PyPI

Once you are satisfied with the build and local installation, you can publish the package to PyPI.

### 3.1. Install `twine`

You will use `twine` to upload your package to PyPI. If you don’t have `twine` installed, install it with:

```bash
pip install twine
```

### 3.2. Test Upload to TestPyPI (Optional)

Before uploading to the official PyPI, it's a good idea to upload to TestPyPI to ensure everything works as expected.

You can upload the wheel to TestPyPI using:

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

You can install your package from TestPyPI to test it:

```bash
pip install --index-url https://test.pypi.org/simple/ ttp_assistant
```

### 3.3. Upload to PyPI

Once you've confirmed everything works fine on TestPyPI, upload the package to the official PyPI repository:

```bash
twine upload dist/*
```

### 3.4. Install from PyPI

After uploading to PyPI, you can install the package directly from PyPI to test it:

```bash
pip install ttp_assistant
```

---

## Additional Tips

- **Versioning**: Make sure to update the version in your `setup.py` file (`version='0.1.0'`) before each release. If you forget to update the version, PyPI will reject the upload with a "file already exists" error.
- **Tagging**: It’s a good practice to tag your release in Git after publishing:
  
  ```bash
  git tag v0.1.0
  git push origin v0.1.0
  ```
