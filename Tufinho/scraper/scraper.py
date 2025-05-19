import requests

def baixar_pagina():
        url = "https://gradenahora.com.br/utfpr/grade_na_hora.html#CODIGO_CURSO=04219"
        response = requests.get(url)
        if response.status_code == 200: 
                print("Sucesso!")
                return response.text
        else:
            print("Erro!", response.status_code)
            return None
