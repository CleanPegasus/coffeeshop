from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(

    name = "coffeeshop",
    version = "1.2.0",
    description = "A python package that sends your deep learning training and validation metrics to your slack channel or user after every specified epoch.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/CleanPegasus/coffeeshop",
    author = "Arunkumar L - A roboVITics project",
    author_email = "arunk609@gmail.com",
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages = ["coffeeshop"],
    include_package_data = True,
    install_requires = ["keras>=2.2.0", "slackclient"]

)
