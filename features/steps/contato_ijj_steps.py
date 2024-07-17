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
    wait = WebDriverWait(context.browser,10)
    
    alert = wait.until(EC.alert_is_present())
    assert 'Dados recebidos!' in alert.text, "Dados não recebidos"