from setuptools import setup

setup(name = 'SneakPeak',
      version = '1.0',
      description = 'A security camera applicataion that monitors any changes and saves the images',
      long_description = open('README.md').read()
      url = 'https://github.com/kishorevasan/securityCamera',
      author = 'Kishore Vasan',
      author_email = 'kishorev@uw.edu',
      license = 'MIT',
      install_requires=[
            'cv2',
            'numpy',
          ],
      classifiers = [
            'Development Status :: 3-Alpha'
            'Intended Audience :: Everyone'
            'License :: MIT License',
            'Programming Language :: Python :: 2.7',
          ],
      )
