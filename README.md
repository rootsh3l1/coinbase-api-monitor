
# Coinbase Monitor
> Coinbase cryptocurrency price monitor.

[![](https://img.shields.io/badge/python-3.4+-blue.svg)](https://www.python.org/downloads/)

Simple cryptocurrency price monitor written in python using the Coinbase API.

![](unknown.png)

You can find the app ported in GOlang with a very cool TUI [here](https://github.com/Polliog/cryptocurrency-monitor).
<br>\- Credits to my mate Polliog :)

## Installation

OS X & Linux:

```sh
git clone https://github.com/rootsh3l1/coinbase-api-monitor.git && cd coinbase-api-monitor
```

Windows:

```sh
Coming soon...
```

## Usage

Once you run the program, you'll get choose from the available cryptocurrencies, you will then enter the amount of coins you have so you can track your current balance, and finally enter the refresh rate you prefer (personally recommend 10s to avoid any sort of rate-limit/ban).


## Deployment setup

```sh
pip3 install -r requirements.txt
python3 monitor.py
```

## Release History


* 0.1.0 - First release
## Meta

Distributed under the [AGPL-3.0](https://github.com/rootsh3l1/coinbase-api-monitor/blob/main/LICENSE) license. See ``LICENSE`` for more information.

[https://github.com/rootsh3l1/coinbase-api-monitor](https://github.com/rootsh3l1)

## Contributing

1. Fork it (<https://github.com/rootsh3l1/coinbase-api-monitor/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
