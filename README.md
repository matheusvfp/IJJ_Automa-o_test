# Projeto de Teste de Automação com Behave e Selenium

Este projeto utiliza a combinação de Behave (uma biblioteca de BDD para Python) e Selenium WebDriver para automatizar o teste de um formulário no site do Instituto Joga Junto.

## Estrutura do Projeto

- **Features**: Diretório que contém os arquivos `.feature` escritos em Gherkin.
- **Steps**: Diretório que contém a implementação dos passos em Python.
- **Environment**: Configurações globais para o Behave.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado:

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (para usar com o Firefox)

Você também precisará instalar as seguintes bibliotecas Python:

```sh
pip install behave selenium
```
## Estrutura do Código

### Arquivo de Features (`.feature`)

O arquivo `.feature` define o comportamento esperado para o envio de dados ao formulário do Instituto Joga Junto.

```gherkin
Feature: Envio de dados ao formulário 
    Scenario: Envio de dados com o assunto quero ser facilitador

    Como usuário do site do Instituto Joga Junto 
    Quero preencher o formulário de contato
    Para enviar o formulário preenchido 
    
    Given que estou na página do Instituto Joga Junto 
    When preenchido o formulário
    And aperto o botão de enviar 
    Then o dado é enviado com sucesso
```

## Implementação dos Steps (steps.py)
### O arquivo `.steps` contém a implementação dos passos definidos no arquivo .feature.

```python
from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que estou na página do Instituto Joga Junto')
def step_entrar_na_pagina(context):
    title = context.browser.title
    assert 'Instituto Joga Junto' in title, "Titulo não encontrado"

@when(u'preenchido o formulário')
def step_impl(context):
    context.browser.find_element(By.NAME, "nome").send_keys("Matheus Vinícius Ferreira Pinheiro")
    context.browser.find_element(By.NAME, "email").send_keys("matheusvfp@gmail.com")
    context.browser.find_element(By.NAME, "body").send_keys("Automação final com behave")
    
    select_subjectcs = context.browser.find_element(By.NAME, 'assunto')
    select = Select(select_subjectcs)
    select.select_by_visible_text("Ser facilitador")

@when(u'aperto o botão de enviar')
def step_impl(context):
    context.browser.find_element(By.XPATH,'//*[@id="Contato"]/div[1]/form/button').submit()

@then(u'o dado é enviado com sucesso')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    assert 'Dados recebidos!' in alert.text, "Dados não recebidos"
```


## Executando os Testes
### Para executar os testes, use o comando:
``` behave
behave
```
#### Certifique-se de que o Selenium WebDriver (por exemplo, geckodriver para Firefox) esteja no seu PATH ou no mesmo diretório do seu projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

