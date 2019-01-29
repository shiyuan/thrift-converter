import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thrift_converter",
    version="0.0.1",
    author="Yuan Shi",
    author_email="shiyuan404@hotmail.com",
    description="Thrift converting tools: json2thrift, thrift2json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shiyuan/thrift_converter",
    packages=setuptools.find_packages(),
    install_requires=[
        'ptsd>=0.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
