from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="ttp-assistant",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,  # To include non-Python files like icons, static files
    python_requires='>=3.9',  # Python version requirement
    install_requires=[
        'bcrypt>=4.2.0',
        'cffi>=1.17.1',
        'click>=8.1.7',
        'colorama>=0.4.6',
        'cryptography>=43.0.3',
        'Jinja2>=3.1.4',
        'jmespath>=1.0.1',
        'MarkupSafe>=3.0.1',
        'paramiko>=3.5.0',
        'pycparser>=2.22',
        'PyNaCl>=1.5.0',
        'PyQt6>=6.7.1',
        'PyQt6-Qt6>=6.7.3',
        'PyQt6-WebEngine>=6.7.0',
        'PyQt6-WebEngine-Qt6>=6.7.3',
        'PyQt6-WebEngineSubwheel-Qt6>=6.7.3',
        'PyQt6_sip>=13.8.0',
        'pysshpass>=0.2.2',
        'pywinpty>=2.0.14',
        'PyYAML>=6.0.2',
        'ruamel.yaml>=0.18.6',
        'ruamel.yaml.clib>=0.2.8',
        'tabulate>=0.9.0',
        'ttp>=0.9.5'
    ],
    entry_points={
        'console_scripts': [
            'ttpassist = ttp_assistant.__main__:main',  # Entry point for starting the app
        ],
    },
    package_data={
        '': ['static/*', 'icons/*', 'templates/*']
    },
    license="GPLv3",  # Specify GPLv3 license
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,  # Include the README.md as the long description
    long_description_content_type="text/markdown",  # Set content type to markdown
)
