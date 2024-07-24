from setuptools import setup, find_packages

setup(
    name='swirl',  # The name of your package
    version='0.1.0',  # The initial release version
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        # List your package dependencies here
        # 'requests>=2.24.0',
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here
            # 'mycommand=mypackage.module:function',
        ],
    },
    author='Your Name',  # Your name as the package author
    author_email='your.email@example.com',  # Your email address
    description='A short description of your package',  # A brief description
    long_description=open('README.md').read(),  # Long description read from README.md
    long_description_content_type='text/markdown',  # Content type of the long description
    url='https://github.com/yourusername/mypackage',  # URL to the project homepage
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],  # Classifiers help users find your package
    python_requires='>=3.6',  # Specify the Python versions compatible with your package
)
