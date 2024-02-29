import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "trial_repo",
    version = "0.0.1",
    author = "MyFaduGame",
    author_email = "navinsharma9376319931@gmail.com",
    description = "This is an sample Package to build it only contains the sample multiply 3 structure",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://www.github.com/MyFaduGame/",
    project_urls = {
        "Bug Tracker": "https://www.github.com/MyFaduGame/",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)