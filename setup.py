from setuptools import setup, find_packages

setup(name='decidim.electionguard',
      version='0.1.0',
      description='ElectionGuard wrappers to be used by Decidim eVoting project',
      url='http://github.com/codegram/decidim.electionguard',
      author='Codegram',
      author_email='leo@codegram.com',
      license='MIT',
      package_dir={"": "src"},
      packages=find_packages('src')
      )
