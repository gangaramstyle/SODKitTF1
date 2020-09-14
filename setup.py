from setuptools import setup
from setuptools import find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='SODKit',
      version='0.0.1',
      author='Simi',
      author_email='',
      description='',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url="https://github.com",
      packages=find_packages(),
      classifiers=[],
      install_requires=[
           'opencv-python',
           'nibabel',
           'SimpleITK',
           'medpy',
           'pynrrd',
           'moviepy'
      ]
)
      
