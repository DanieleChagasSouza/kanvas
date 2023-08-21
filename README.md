# M5 - Projeto Final Kanvas

## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install -r requirements.txt
```
**IMPORTANTE**: As bibliotecas inicialmente listadas requirements.txt só dizem respeito aos testes, para a execução da sua aplicação você deve atualizá-lo adicionando todos os pacotes necessários.


## Execução dos testes:

Como este projeto se trata de uma refatoração, não terá divisão de testes por tarefa, pois o objetivo é que todos os testes continuem passando após a refatoração.
Deste modo, para rodar a bateria de todos os testes, utilize:
```shell
pytest --testdox -vvs
```
---

Caso você tenha interesse em rodar apenas um diretório de testes específico, utilize os comandos abaixo:

Accounts:
```python
pytest --testdox -vvs tests/accounts/
```

Contents:
```python
pytest --testdox -vvs tests/contents/
```

Courses:
```python
pytest --testdox -vvs tests/courses/
```

---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_user_login_without_required_fields".

```shell
pytest --testdox -vvs tests/accounts/tests_views.py::TestAccountView::test_login_without_required_fields
```