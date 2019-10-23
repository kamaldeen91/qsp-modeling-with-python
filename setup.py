from setuptools import setup, find_packages
from General import files_in_dir

setup(name='pqsp',
      version='pqsp_0.1.0',
      packages=find_packages(),
      author='K. Okuneye',
      author_email='kokuneye@northwestern.edu',
      package_data={'': files_in_dir('python_QSP')},
      )
