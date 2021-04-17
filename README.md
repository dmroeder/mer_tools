# mer_tools

This project is a set of tools to extract data from MER files developed using
Rockwell Automation's FactoryTalk View Studio.

This started out as a way to figure out what version a MER file was generated
in.  Other tools and features will be added over time as I can figure
them out

See the [documentation](docs/README.md) for information in the various functions

## Depenencies

olefile

```
pip install olefile
```

## Getting Started

```
from mer_tools import mer
# get the version the MER was generated with
version = mer('myfile.mer').get_version()
print(version)
```

## Authors

* **Dustin Roeder** - *Maintainer* - [dmroeder](https://github.com/dmroeder)

## License

This project is licensed under Apache 2.0 License - see the [LICENSE](LICENSE.txt) file for details.

