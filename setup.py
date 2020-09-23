from setuptools import setup

setup(name='decidim.electionguard',
      version='0.1.0',
      description='ElectionGuard wrappers to be used by Decidim eVoting project',
      url='http://github.com/codegram/decidim.electionguard',
      author='Codegram',
      author_email='leo@codegram.com',
      license='MIT',
      packages=['decidim.electionguard'],
      package_dir = {
        'decidim.electionguard': 'src'
      })
