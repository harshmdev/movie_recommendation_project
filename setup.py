import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.1"

REPO_NAME = "Movie Recommendation"
AUTHOR_USER_NAME="harshmdev"
SRC_REPO= "movie_recommendation_project"
AUTHOR_EMAIL="hmohandev@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for movies recommendations.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)