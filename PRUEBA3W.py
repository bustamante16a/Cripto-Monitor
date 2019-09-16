#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SEGUNDO.py
#  
#  Copyright 2019 Andres Bustamante <andres@andres-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#ESTO ME LLAMA LA RUTINA PARA REALIZAR EL LLAMADO HTTP
import requests

#ESTO HACE QUE PUEDA TRABAJAR CON JSON
import json

#ESTO AYUDA CON EL TEXTO
import string

#PARA INCLUIR FECHA
import datetime
from datetime import date
from datetime import datetime

#ESTO ME DA EL DIA
today = date.today()

#ESTO DEBERIA HACER LA PETICION POST A LA API PRICE
url= 'https://petroapp-price.petro.gob.ve/price/'
payload = {'coins': ['PTR'], 'fiats': ['USD','BS','EUR','CNY','RUB']}
headers={'Content-type': 'application/json',}
r = requests.post(url, headers=headers, data = json.dumps(payload))

#ESTO ME MUESTRA LOS DATOS EN BRUTO
#print r.json()

#ESTO CREA UNA VARIABLE DICCIONARIO CON EL JSON
data_dict = r.json()

#DESDE AQUI DESGLOSO LOS DICCIONERIOS QUE HAY EN EL JSON	

data1_dict = data_dict["data"]

data2_dict = data1_dict["PTR"]

bolivar = data2_dict["BS"]
euro = data2_dict["EUR"]
dolar = data2_dict["USD"]
rublo = data2_dict["RUB"]
yuan = data2_dict["CNY"]

#ESTO DEBERIA HACER LA PETICION2 POST A LA API PRICE
url= 'https://petroapp-price.petro.gob.ve/price/PTR'
payload = {'coins': ['ETH','DASH','BTC','LTC']}
headers={'Content-type': 'application/json',}
r1 = requests.post(url, headers=headers, data = json.dumps(payload))


#CON ESTO VUELVO EL JSON UN DICCIONARIO
dataX_dict = r1.json()

dataX1_dict = dataX_dict["data"]

#CON BTC
dataXBTC_dict = dataX1_dict["BTC"]

btc_ptr = dataXBTC_dict["BTC"]
ptr_btc = dataXBTC_dict["PTR"]

#CON ETH
dataXETH_dict = dataX1_dict["ETH"]

eth_ptr = dataXETH_dict["ETH"]
ptr_eth = dataXETH_dict["PTR"]

#CON LTC
dataXLTC_dict = dataX1_dict["LTC"]

ltc_ptr = dataXLTC_dict["LTC"]
ptr_ltc = dataXLTC_dict["PTR"]

#CON DASH
dataXDASH_dict = dataX1_dict["DASH"]

dash_ptr = dataXDASH_dict["DASH"]
ptr_dash = dataXDASH_dict["PTR"]

#ESTO DEBERIA HACER LA PETICION GET A LA API PRICE
url= 'https://criptolago.io/api/tasas'
headers={'Content-type': 'application/json',}
r2 = requests.get(url, headers=headers)

#ESTO CREA UNA VARIABLE DICCIONARIO CON EL JSON
clagodata_dict = r2.json()

#print(json.dumps(data_dict))

clago_BTC_VES_compra = clagodata_dict["btc_ves"]

clago_BTC_VES_venta = clagodata_dict["ves_btc"]

clago_PTR_VES_compra = clagodata_dict["ptr_ves"]

clago_PTR_VES_venta = clagodata_dict["ves_ptr"]

clago_PTR_BTC_compra = clagodata_dict["ptr_btc"]

clago_PTR_BTC_venta = clagodata_dict["btc_ptr"]

#AHORA LA GUI
from prueba3 import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label_fecha.setText(str(today))
        self.label_valorbs.setText(str(bolivar))
        self.label_valoreur.setText(str(euro))
        self.label_valorusd.setText(str(dolar))
        self.label_valorcny.setText(str(yuan))
        self.label_valorrub.setText(str(rublo))
        self.label_btcptr.setText(str(ptr_btc))
        self.label_ptrbtc.setText(str(btc_ptr))
        self.label_ethptr.setText(str(ptr_eth))
        self.label_ptreth.setText(str(eth_ptr))
        self.label_ltcptr.setText(str(ptr_ltc))
        self.label_ptrltc.setText(str(ltc_ptr))
        self.label_dashptr.setText(str(ptr_dash))
        self.label_ptrdash.setText(str(dash_ptr))
        self.label_cptrventa.setText(str(clago_PTR_VES_venta))
        self.label_cptrcompra.setText(str(clago_PTR_VES_compra))
        self.label_cptr1venta.setText(str(clago_PTR_BTC_venta))
        self.label_cptr1compra.setText(str(clago_PTR_BTC_compra))
        self.label_cbtcventa.setText(str(clago_BTC_VES_venta))
        self.label_cbtccompra.setText(str(clago_BTC_VES_compra))
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
