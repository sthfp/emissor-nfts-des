#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#O código abaixo possibilita a inserção da escrituração de notas fiscais no sistema DES

rom selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()
driver.get("http://des.cambe.pr.gov.br:8081/des/login.xhtml")
#fazendo o login
driver.find_element_by_xpath('//*[@id="tela-login-txtcnpj"]').send_keys({CNPJ})
driver.find_element_by_xpath('//*[@id="tela-login-txtusuario"]').send_keys({"login"})
driver.find_element_by_xpath('//*[@id="tela-login-txtsenha"]').send_keys({"senha"})
driver.find_element_by_xpath('//*[@id="tela-login-btnentrar"]').click()
sleep(2)
driver.get("http://des.cambe.pr.gov.br:8081/des/declaracao/tomador/index.xhtml")
#inserindo as informações do Contribuinte
##essa etapa deve ser realizada apenas para a primeira nota fiscal
driver.find_element_by_xpath('//*[@id="panel_selec_txt_contribuinte_panel_contribuinte_txt_nome"]').send_keys({cnpjContribuinte})
sleep(2)
driver.find_element_by_xpath('//*[@id="panel_selec_txt_contribuinte_panel_contribuinte_txt_nome"]').send_keys(Keys.TAB)
driver.find_element_by_xpath('//*[@id="panel_selec_btn_pesquisar"]').click()
sleep(2)
##
#inserindo as informações da nota fiscal
driver.find_element_by_xpath('//*[@id="nao_selecionado"]').send_keys({"nomeFornecedor"})
driver.find_element_by_xpath('//*[@id="nao_selecionadocpf"]').send_keys({cnpjFornecedor})
driver.find_element_by_xpath('//*[@id="nao_selecionado"]').send_keys(Keys.TAB)
sleep(2)
driver.find_element_by_xpath('//*[@id="panel_selec_cnaeee_txt_banco1_panel_contribuinte_txt_nome"]').send_keys({"CNAE"})
sleep(2)
driver.find_element_by_xpath('//*[@id="panel_selec_cnaeee_txt_banco1_panel_contribuinte_txt_nome"]').send_keys(Keys.TAB)
sleep(2)
driver.find_element_by_xpath('//*[@id="panel_selec_cnaeee_btn_pesquisar1"]').click()
driver.find_element_by_xpath('//*[@id="ds_nrnota"]').send_keys({numNf})
driver.find_element_by_xpath('//*[@id="dt_credito"]').send_keys({"dd/mm/aaaa"})
sleep(2)
driver.find_element_by_xpath('//*[@id="valor_nota"]').send_keys({valorNf})
sleep(2)
driver.find_element_by_xpath('//*[@id="dsaliq"]').send_keys({aliquota})
sleep(2)
#finalizando
driver.find_element_by_xpath('//*[@id="confirmar_dlg"]').click()
sleep(4)
driver.find_element_by_xpath('//*[@id="btn_fechar_dlg_mensagem"]').click()

