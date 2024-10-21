from setuptools import setup, find_packages

setup(
    name='ttp_assistant',  # Name of the package
    version='0.1.0',  # Version of the package
    author='Scott Peterman',  # Your name as the author
    author_email='scottpeterman@gmail.com',  # Your email
    description='A tool to assist with TTP template building in a GUI, testing and execution',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/scottpeterman/ttpassistant',  # Your project URL
    project_urls={
        'Bug Tracker': 'https://github.com/scottpeterman/ttpassistant/issues',
        'Source Code': 'https://github.com/scottpeterman/ttpassistant',
    },
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-python files specified in MANIFEST.in
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
    python_requires='>=3.9',  # Minimum Python version required
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
        'ttp>=0.9.5',
    ],  # Dependencies from requirements.txt
    entry_points={
        'console_scripts': [
            'ttp_assistant=ttp_assistant.__main__:main',  # Command line entry point
        ],
    },
    license='GPLv3',  # Updated license
)
