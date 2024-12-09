from setuptools import setup, find_packages

setup(
    name="finances",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    author="Gabriel Henrique Marengoni, Lorenzo Cruz Coneglian",
    author_email="marengoni.gabriel@escola.pr.gov.br",
    description="Um pacote para gerenciamento de finanças pessoais",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/finances",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)