from setuptools import setup



setup(

    name = "coffeeshop",
    version = "1.0"
    description = "A python package that sends your deep learning training loss to your slack channel after every specified epoch",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url = "*ENTER GITHUB URL HERE*",
    author = "Arunkumar L",
    author_email = "arunk609@gmail.com"
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages = ["coffeeshop"],
    include_package_data = True,
    install_requires = ["keras", "slackclient"]

)