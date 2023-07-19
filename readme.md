# phpserve

`phpserve` is a simple command-line tool written in Python for building and running PHP projects with specific PHP versions and extensions. It's useful when you're working with multiple PHP projects that require different PHP versions or extensions.

## Usage

This script offers three commands: `init`, `build`, and `run`.

- `init`: This command creates a `phpserve.json` configuration file in your project directory.

- `build`: This command downloads the specified PHP version from the official PHP website, compiles it, and installs it in a `.phpserve` directory within the project root. It also installs the PHP extensions specified in the `phpserve.json` configuration file.

- `run`: This command runs the PHP server with the PHP version installed by the `build` command.

You can use these commands as follows:

```bash
phpserve init
phpserve build
phpserve run
```

## Configuration

The `init` command will prompt you to enter the PHP version that your project requires. It will then create a `phpserve.json` configuration file with the following structure:

```json
{
  "php_version": "8.2.0",
  "extensions": ["pdo", "bcmath"],
  "port": "8000",
  "endpoint": "."
}
```

- `php_version`: The PHP version that your project requires.
- `extensions`: An array of PHP extensions that your project requires.
- `port`: The port that the PHP server should listen on.
- `endpoint`: The entry point of your PHP application.

You can manually edit this file to change these settings as needed.

## Installation

To install `phpserve`, navigate to the root directory of the `phpserve` project and run the following command:

```bash
pip install .
```

This command installs the `phpserve` package and all its dependencies, as specified in `setup.py`.

After installation, you can use the `phpserve` command from anywhere on your system.

Please note that you may need to use `sudo pip install .` if you're on a Unix-based system and you get a permissions error.

Also, Python and pip must be installed on your system to use this setup.

Absolutely! Here's an updated section of the README to include the required libraries for PHP compilation:

---

## Requirements

`phpserve` requires the following:

- Python 3
- Pip (Python package installer)
- Necessary tools and libraries to build PHP from source

Before running `phpserve`, please ensure that you have the necessary libraries to compile PHP. Here's a list of the essential tools and libraries:

- `autoconf`
- `automake`
- `libtool`
- `re2c`
- `bison`
- `flex`
- `libxml2-dev`
- `libsqlite3-dev`
- `libssl-dev`
- `libcurl4-openssl-dev`
- `libpng-dev`
- `libjpeg-dev`
- `libfreetype6-dev`
- `libonig-dev`
- `libzip-dev`

You can usually install these with your system's package manager. For example, on a Debian-based system like Ubuntu, you can use the following command:

```bash
sudo apt-get install -y autoconf automake libtool re2c bison flex libxml2-dev libsqlite3-dev libssl-dev libcurl4-openssl-dev libpng-dev libjpeg-dev libfreetype6-dev libonig-dev libzip-dev
```

For macOS, you can use the following command with Homebrew:

```bash
brew install autoconf automake libtool re2c bison flex libxml2 libsqlite3 openssl@1.1 curl libpng jpeg freetype oniguruma libzip
```

Please note that the list of required libraries might differ depending on the PHP extensions you plan to use. This list covers the common libraries needed for a basic PHP installation.

---

Remember, it's always important to check the official PHP documentation or the documentation for the specific PHP extension you're trying to compile to ensure you have all necessary dependencies. The PHP manual provides an [excellent guide](https://www.php.net/manual/en/install.unix.php) on compiling PHP from source.

## Notes

This script is intended to be a simple solution for managing PHP environments for different projects. It doesn't handle every possible scenario or edge case. If you need to manage complex PHP environments, consider using a more advanced tool like Docker.

