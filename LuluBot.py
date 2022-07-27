import random
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from faker import Faker
import login

servico = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servico)

with open('./escolas.txt') as banco:  # abrindo arquivo txt com as escolas
    escolas = banco.readlines()
for i in range(len(escolas)):
    escolas[i] = escolas[i].strip() 

faker = Faker('pt_BR') 


def run(): 
    #funcao principal de login
    driver.get("http://pjequitinhonha.ifalmenara.com.br/login")
    driver.find_element(By.XPATH, '//*[@id="cpf"]').send_keys(login.cpf)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(login.passWord)
    driver.find_element(
        By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]/form/div[3]/div/button').click()

def getEscola(): 
    #Funcao que entra na parte de comunidades 
    driver.get('http://pjequitinhonha.ifalmenara.com.br/escolas/create')
    #nome
    driver.find_element(By.XPATH, '//*[@id="nome_escola"]').send_keys(escolas[random.randint(0,len(escolas) - 1)])
    #Rua
    driver.find_element(By.XPATH, '//*[@id="rua"]').send_keys(faker.street_name())
    #cnpj 
    driver.find_element(By.XPATH, '//*[@id="cnpj"]').send_keys(faker.cnpj()) #
    #cep
    driver.find_element(
        By.XPATH, '//*[@id="cep"]').send_keys(random.randint(100000000, 10000000000))
    #numero
    driver.find_element(
        By.XPATH, '// *[@id="numero"]').send_keys(random.randint(1, 100))
    #bairro
    driver.find_element(By.XPATH, '//*[@id="bairro"]').send_keys(faker.district())
    #telefone
    driver.find_element(
        By.XPATH, '//*[@id="telefone"]').send_keys(random.randint(100000000, 10000000000))
    #funcionarios
    driver.find_element(
        By.XPATH, '//*[@id="quant_funcionarios"]').send_keys(random.randint(1, 100))
    #quantidade de alunos
    driver.find_element(
        By.XPATH, '//*[@id="quant_alunos"]').send_keys(random.randint(1, 1000))
    #salvar informações
    driver.find_element(
        By.XPATH, '/html/body/div/div[3]/div/div/div[2]/form/div/div[4]/div/input').click()

def getEmpreasas(): 
    #entrando no campo de empresas
    driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div[2]/div[4]/a').click() 
    #adcionar nova empreasa
    driver.find_element(
        By.XPATH, '/html/body/div/div[3]/div/div[2]/div[1]/div/div[2]/center/a').click() 
    #nome
    driver.find_element(
        By.XPATH, '//*[@id="razaoSocial"]').send_keys(faker.company())
    #Cidade da empresa
    driver.find_element(
        By.XPATH, '//*[@id="cidade"]').send_keys(faker.city())
    #Numero_Telefone
    driver.find_element(
        By.XPATH, '//*[@id="telefone"]').send_keys(faker.phone_number())   
    #cnpj
    driver.find_element(By.XPATH, '//*[@id="cnpj"]').send_keys(faker.cnpj())

    



    
while(True):
    print('='*10)
    print("o que deseja?")
    print("0 - Sair")
    print("1 - login")
    print("2 - escolas")
    print("3 - empresas ")
    print('='*10)


    opcao = int(input())
   
    print('='*10)




    if(opcao == 0):
        driver.close()
        print("...saindo")
        break
    
    elif opcao == 3:
        getEmpreasas() 

    elif opcao == 1:
        run()

    elif opcao == 2: 
        opcao2 = int(input("Quantos ciclos deseja?"))
        
        for i in range(opcao2): 
            getEscola()
