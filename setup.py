import setuptools


with open('README.md', 'r') as readme_file:
    long_desc = readme_file.read()

setuptools.setup(
    name='Classy-Json',
    version='1.0.0',
    author='Iapetus-11',
    description='An emulation of the way json behaves in Javascript, but in Python',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/Iapetus-11/Classy-Json',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)