# EveryAI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/every-ai.svg)](https://badge.fury.io/py/every-ai)
[![EveryAI CI](https://github.com/tomusher/every-ai/actions/workflows/test.yml/badge.svg)](https://github.com/tomusher/every-ai/actions/workflows/test.yml)

EveryAI intends to provide a unified interface to multiple AI services, offering a single API that consuming applications can use without needing to know the specifics of the underlying service.

Currently the supported backends are:

- OpenAI (chat and embeddings)
- Anthropic (chat only)

## Usage

To reate an instance of an EveryAI backend, use the `init` function:

```python
import every_ai

backend = every_ai.init("openai")
```

Once you have a backend, you have access to methods depending on backend:

```python
response = backend.chat("Tell me a joke")
embedding = backend.embed(["Embed this content"])
```

### OpenAI

The OpenAI backend supports both chat completions and embeddings. It can be initialised with a dictionary containing the following settings:

- `api_key` (required) - Your OpenAI API key
- `chat_model` (default: `gpt-3.5-turbo`) - The OpenAI model to be used for chat completions, e.g. `gpt-4`, `gpt-3.5-turbo`.
- `embedding_model` (default: `text-embedding-ada-002`) - The OpenAI model to be used for embeddings.

For example, to customise the OpenAI backend to use GPT4:

```python
import every_ai

backend = every_ai.init("openai", api_key="foo-bar-baz", chat_model="gpt-4")
```

### Anthropic

The Antrophic backend only supports chat completions. It can be initialised with a dictionary containing the following settings:

- `api_key` (required) - Your Anthropic API key
- `chat_model` (default: `claude-instant-1`) - The Anthropic model to be used for chat completions, e.g. `claude-instant-1`, `claude-2`.

For example, to customise the Anthropic backend to use `claude-2`:

```python
import every_ai

backend = every_ai.init("anthropic", api_key="foo-bar-baz", chat_model="claude-2")
```

## Links

-   [Documentation](https://github.com/tomusher/every-ai/blob/main/README.md)
-   [Changelog](https://github.com/tomusher/every-ai/blob/main/CHANGELOG.md)
-   [Contributing](https://github.com/tomusher/every-ai/blob/main/CHANGELOG.md)
-   [Discussions](https://github.com/tomusher/every-ai/discussions)
-   [Security](https://github.com/tomusher/every-ai/security)

## Contributing

### Install

To make changes to this project, first clone this repository:

```sh
git clone https://github.com/tomusher/every-ai.git
cd every-ai
```

With your preferred virtualenv activated, install testing dependencies:

#### Using pip

```sh
python -m pip install --upgrade pip>=21.3
python -m pip install -e .[testing] -U
```

#### Using flit

```sh
python -m pip install flit
flit install
```

### pre-commit

Note that this project uses [pre-commit](https://github.com/pre-commit/pre-commit).
It is included in the project testing requirements. To set up locally:

```shell
# go to the project directory
$ cd every-ai
# initialize pre-commit
$ pre-commit install

# Optional, run all checks once for this, then the checks will run only on the changed files
$ git ls-files --others --cached --exclude-standard | xargs pre-commit run --files
```

### How to run tests

Now you can run tests as shown below:

```sh
tox
```

or, you can run them for a specific environment `tox -e python3.8` or specific test
`tox -e python3.9 every-ai.tests.test_file.TestClass.test_method`

To run the test app interactively, use `tox -e interactive`, visit `http://127.0.0.1:8020/admin/` and log in with `admin`/`changeme`.
