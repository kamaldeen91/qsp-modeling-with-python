from setuptools import setup, find_packages
from simtools.Utilities.General import files_in_dir

setup(name='pqsp',
      version='$VERSION$',
      packages=find_packages(),
      author='K. Okuneye',
      author_email='kokuneye@northwestern.edu',
      package_data={'': files_in_dir('python_QSP')},
      # install_requires=['dtk-tools']
      )
