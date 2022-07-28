import random
from webbrowser import get
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from faker import Faker
import login

servico = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servico)

with open('./Main/escolas.txt') as banco:  # abrindo arquivo txt com as escolas
    escolas = banco.readlines()
for i in range(len(escolas)):
    escolas[i] = escolas[i].strip()

faker = Faker('pt_BR')


def run():
    # funcao principal de login
    driver.get("http://pjequitinhonha.ifalmenara.com.br/login")
    driver.find_element(By.XPATH, '//*[@id="cpf"]').send_keys(login.cpf)
    driver.find_element(
        By.XPATH, '//*[@id="password"]').send_keys(login.passWord)
    driver.find_element(
        By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]/form/div[3]/div/button').click()


def getEscola():
    # Funcao que entra na parte de comunidades
    driver.get('http://pjequitinhonha.ifalmenara.com.br/escolas/create')
    # nome
    driver.find_element(By.XPATH, '//*[@id="nome_escola"]').send_keys(
        escolas[random.randint(0, len(escolas) - 1)])
    # Rua
    driver.find_element(
        By.XPATH, '//*[@id="rua"]').send_keys(faker.street_name())
    # cnpj
    driver.find_element(By.XPATH, '//*[@id="cnpj"]').send_keys(faker.cnpj())
    # cep
    driver.find_element(By.XPATH, '//*[@id="cep"]').send_keys(faker.postcode())
    # numero
    driver.find_element(
        By.XPATH, '// *[@id="numero"]').send_keys(faker.building_number())
    # bairro
    driver.find_element(
        By.XPATH, '//*[@id="bairro"]').send_keys(faker.bairro())
    # telefone
    driver.find_element(
        By.XPATH, '//*[@id="telefone"]').send_keys(faker.phone_number())
    # funcionarios
    driver.find_element(
        By.XPATH, '//*[@id="quant_funcionarios"]').send_keys(faker.building_number())
    # quantidade de alunos
    driver.find_element(
        By.XPATH, '//*[@id="quant_alunos"]').send_keys(faker.building_number())
    # salvar informações
    driver.find_element(
        By.XPATH, '/html/body/div/div[3]/div/div/div[2]/form/div/div[4]/div/input').click()


def getEmpreasas():
    # entrando no campo de empresas
    driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div[2]/div[4]/a').click()
    # adcionar nova empreasa
    driver.find_element(
        By.XPATH, '/html/body/div/div[3]/div/div[2]/div[1]/div/div[2]/center/a').click()
    # nome
    driver.find_element(
        By.XPATH, '//*[@id="razaoSocial"]').send_keys(faker.company())
    # Rua
    driver.find_element(
        By.XPATH, '//*[@id="rua"]').send_keys(faker.street_name())
    # Cidade da empresa
    driver.find_element(By.XPATH, '//*[@id="cidade"]').send_keys(faker.city())
    # Numero_Telefone
    driver.find_element(
        By.XPATH, '//*[@id="telefone"]').send_keys(faker.phone_number())
    # cnpj
    driver.find_element(By.XPATH, '//*[@id="cnpj"]').send_keys(faker.cnpj())
    # numero_rua
    driver.find_element(
        By.XPATH, '//*[@id="numero"]').send_keys(faker.building_number())
    # bairro
    driver.find_element(
        By.XPATH, '//*[@id="bairro"]').send_keys(faker.bairro())
    # cep
    driver.find_element(By.XPATH, '//*[@id="cep"]').send_keys(faker.postcode())
    # telefone_celular
    driver.find_element(
        By.XPATH, '//*[@id="celular"]').send_keys(faker.phone_number())

    driver.find_element(
        By.XPATH, '/html/body/div/div[3]/div/div/div[2]/form/div/div[5]/div/input').click()

    if __name__ == '__main__':
        run()
