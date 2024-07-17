
Feature: Envio de dados ao formulário 
    Scenario: Envio de dados com o assunto quero ser facilitador

    Como usuário do site do Instituto Joga Junto 
    Quero preencher o formulário de contato
    Para enviar o formulário preenchido 
    
    Given que estou na página do Instituto Joga Junto 
    When preenchido o formulário
    And aperto o botão de enviar 
    Then o dado é enviado com sucesso 

