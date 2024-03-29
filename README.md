# RecordFlux Parser

This is the parser for the [RecordFlux](https://github.com/Componolit/RecordFlux) language which is based on [Langkit](https://github.com/AdaCore/langkit).

## Development

As a prerequisite to build the parser, the following dependencies need to be installed:

- [GNAT Community Edition](https://www.adacore.com/download) >= 2020
- [GNU MP Arithmetic Library](https://gmplib.org/) This is provided as a package for various distributions e.g. libgmp-dev (Debian/Ubuntu), gmp-devel (Fedora) or gmp (Arch Linux).

**Note**: GNAT must be added to the PATH environment variable after installation: `export PATH=<GNAT-directory>/bin:$PATH`.

The configuration of the development tools and some dependencies are managed in separate repositories and must be downloaded and set up once.

```Console
$ make init
```

To run the tests, the RecordFlux parser package and its dependencies must be installed. Use the respective make target:

```Console
$ make install_devel
```

**Note:** Develop mode of setuptools (`pip -e`) is unsupported. The parser must be reinstalled before changes to the code take effect.

All checks and tests can be executed at once with `make` or individually with `make check` or `make test`.
