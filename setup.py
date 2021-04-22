import setuptools  # import order matters here wth
from Cython.Build import cythonize

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="classy-json",
    version="4.0.0",
    author="Iapetus-11",
    description="Dot access for Python dictionaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Iapetus-11/classy-json",
    packages=setuptools.find_packages(),
    ext_modules=cythonize("classyjson/*.pyx"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["cython"]
)
