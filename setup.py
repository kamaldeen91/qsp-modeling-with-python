from setuptools import setup, find_packages
from General import files_in_dir

setup(name='pqsp',
      version='pqsp_0.1.0',
      packages=find_packages(),
      author='K. Okuneye',
      author_email='kokuneye@northwestern.edu',
      url='https://github.com/kamaldeen91/qsp-modeling-with-python',
      keywords=['Quantitative Pharmacology', 'Ordinary Differential Equations'],
      install_requires=['numpy',
                        'scipy'],
      classifiers=['Topic :: QSP modeling with Python',
                   'Programming Language :: Python :: 3.7'],
      package_data={'': files_in_dir('python_QSP')},
      )
