from setuptools import setup

setup(name='oneconsole',
      version='0.1.7',
      description='Python Package for Oneconsole',
      url='http://github.com/sachinvettithanam/oneconsole',
      author='Sachin Philip Mathew',
      author_email='sachinvettithanam@gmail.com',
      license='MIT',
      packages=['oneconsole'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
