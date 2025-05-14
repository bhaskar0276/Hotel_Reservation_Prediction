from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().split("\n")


setup(
    name="Bhaskar",
    version="0.1",
    author="Bhaskar",
    author_email="tbhaskarreddy992@gmail.com",
    description="This is a project to predict the cancellation of hotel reservations",
    packages=find_packages(),
    install_requires=requirements
)




