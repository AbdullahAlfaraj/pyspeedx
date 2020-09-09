from distutils.core import setup
setup(
  name = 'pyspeedx',         # How you named your package folder (MyLib)
  packages = ['pyspeedx'],   # Chose the same as "name"
  version = '0.1_1_2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'python extension library for accelerating the making of prototypes ',   # Give a short description about your library
  author = 'Abdullah Alfaraj',                   # Type in your name
  author_email = 'abdullah.a.f2014@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/AbdullahAlfaraj',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AbdullahAlfaraj/pyspeedx/archive/v_01_1_2.tar.gz',    # I explain this later on
  keywords = ['Quick', 'Prototyping', 'Extension'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          '',
          '',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)