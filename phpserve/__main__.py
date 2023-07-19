#!/usr/bin/env python3

import os
import json
import sys
import subprocess
from urllib.request import urlretrieve
import tarfile

class PHPServe:
    def __init__(self, config_path='phpserve.json'):
        self.config_path = config_path
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as config_file:
                self.config = json.load(config_file)
        else:
            self.config = {}

    def init(self):
        php_version = input("Enter the PHP version your project requires (e.g., 8.2.0): ")
        extensions = [
                   "bcmath", "bz2", "calendar", "ctype", "curl", "dom", "exif", "fileinfo",
                   "ftp", "gettext", "iconv", "imap", "intl", "json", "mbstring", "mysqli",
                   "openssl", "pcntl", "pdo", "pdo_mysql", "pdo_pgsql", "pdo_sqlite", "pgsql",
                   "phar", "posix", "readline", "shmop", "simplexml", "soap", "sockets", "sodium",
                   "sqlite3", "sysvmsg", "sysvsem", "sysvshm", "tokenizer", "xml", "xmlreader",
                   "xmlwriter", "xsl", "zip", "zlib"
               ]

        print("Here are some common PHP extensions you might want to enable:")
        for i, extension in enumerate(extensions, start=1):
            print(f"{i}. {extension}")

        selected_extensions_indices = input("Enter the numbers of the extensions you want to enable, separated by commas: ")
        selected_extensions_indices = map(int, selected_extensions_indices.split(","))
        selected_extensions = [extensions[i-1] for i in selected_extensions_indices]

        port = input("Enter the port number you want to use for the server (default: 8000): ")

        self.config['php_version'] = php_version
        self.config['extensions'] = selected_extensions
        self.config['port'] = port if port else '8000'
        self.config['endpoint'] = '.'

        with open(self.config_path, 'w') as config_file:
            json.dump(self.config, config_file, indent=2)

        print(f'Configuration file "{self.config_path}" has been created.')

    def build(self):
        php_version = self.config.get('php_version')
        if php_version is None:
            raise Exception('"php_version" not found in the configuration file.')

        php_tar_gz = f'php-{php_version}.tar.gz'
        php_tar_gz_url = f'https://www.php.net/distributions/{php_tar_gz}'

        # Download and extract PHP
        print(f'Downloading {php_tar_gz_url}')
        urlretrieve(php_tar_gz_url, php_tar_gz)

        with tarfile.open(php_tar_gz, 'r:gz') as tar:
            tar.extractall()

        # Configure, make, and install PHP
        os.chdir(f'php-{php_version}')

        # you might want to customize the ./configure command to suit your needs
        subprocess.check_call(['./configure', '--prefix=' + os.path.join(os.getcwd(), '../.phpserve'), '--enable-bcmath', '--with-pdo-mysql'])
        subprocess.check_call(['make'])
        subprocess.check_call(['make', 'install'])

        os.chdir('..')

    def run(self):
        server_port = self.config.get('port', '8000')
        endpoint = self.config.get('endpoint', '.')

        # execute the PHP server
        subprocess.check_call(['.phpserve/bin/php', '-S', f'localhost:{server_port}', '-t', endpoint])

def main():
    if len(sys.argv) < 2:
        print("Usage: phpserve [init|build|run]")
        sys.exit(1)
    command = sys.argv[1]
    php_serve = PHPServe()
    if command == "init":
        php_serve.init()
    elif command == "build":
        php_serve.build()
    elif command == "run":
        php_serve.run()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
