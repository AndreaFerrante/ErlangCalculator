from setuptools import setup, find_packages


setup(
    name                          = 'erlang',
    version                       = '0.0.1',
    description                   = 'Erlang Call Center staffing Python package',
    author                        = 'Andrea Ferrante',
    author_email                  = 'nonicknamethankyou@gmail.com',
    classifiers                   = ['Development Status :: 3 - Alpha',
                                     'Intended Audience :: Developers',
                                     'Topic :: Software Development :: Build Tools',
                                     'License :: OSI Approved :: MIT License',
                                     'Programming Language :: Python :: 3.6',
                                     'Programming Language :: Python :: 3.7',
                                     'Programming Language :: Python :: 3.8',
                                     'Programming Language :: Python :: 3.9',
                                     'Programming Language :: Python :: 3 :: Only'],
    keywords                      = 'datetime, setuptools',
    packages                      = find_packages(where='src'),
    python_requires               = '>=3.6, <4',
    install_requires              = ['datetime', 'os'],
    py_modules                    = ['erlang']
    
)
