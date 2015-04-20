# CIF Software Development Kit for Python
The CIF  Software Development Kit (SDK) for Python contains library code and examples designed to enable developers to build applications using CIF.

[![Build Status](https://travis-ci.org/csirtgadgets/py-cifsdk.png?branch=master)](https://travis-ci.org/csirtgadgets/py-cifsdk)

# Installation
## Ubuntu
  ```bash
  $ sudo apt-get install -y python-dev python-pip git
  $ pip install git+ https://github.com/csirtgadgets/py-cifsdk
  ```

# Examples
## Client
### Config
  ```yaml
  # ~/.cif.yml
  client:
    remote: https://localhost
    token: 1234
  ```
### Running
  ```bash
  $ cif --token 1234 --remote 'https://localhost' -q example.com
  ```

## API
### Search
  ```python
  from cifsdk.client import Client
  from cifsdk.format import Table

  cli = Client(token=1234,
               remote='https://localhost',
               noverifyssl=1)

  ret = cli.search(query='example.com')
  print Table(ret)
  ```
### Ping
  ```python
  from cifsdk.client import Client
  ...

  ret = cli.ping()
  print "roundtrip: %s ms" % ret
  ```

# Support and Documentation

You can also look for information at the [GitHub repo](https://github.com/csirtgadgets/py-cifsdk).

# License and Copyright

Copyright (C) 2015 [the CSIRT Gadgets Foundation](http://csirtgadgets.org)

Free use of this software is granted under the terms of the [GNU Lesser General Public License](https://www.gnu.org/licenses/lgpl.html) (LGPL v3.0). For details see the file ``LICENSE`` included with the distribution.
