# Repositório para testes automatizados em python usando github actions

Baseado em na template de [programmingwithalex](https://github.com/programmingwithalex)
Vindo seguinte vídeo [YouTube video](https://www.youtube.com/watch?v=rY-igT2N8zU&list=PL0dOL8Z7pG3J6t1pqRQiNarBGY-ZnIJcq&index=2).

## Descrição
Repositório para integração contínua através de testes automatizados em Python

The linting is handled by a custom GitHub Action [`pylinters`](https://github.com/marketplace/actions/pylinters) written by myself. The testing is handled by pytest.

## Conteúdo

* `.py` simplistic files to lint with the GitHub Action `pylinters` and test with `pytest`
* `tests/` directory which contains the various `pytest` tests to run
* `requirements.txt` which contains the necessary packages to run the CI
