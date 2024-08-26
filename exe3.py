# programção orientação a objetos

"""
Programção Orientada a Objetos
- flask e Django

Programção Estruturada com OO
- Flet

Programação Funcional
- Lambda

"""

class Aluno():
    def __init__(self,ch,faltas):
        self.ch = ch
        self.faltas = faltas
       
    def calcular_faltas(self):
        percent_ch = self.ch * (25/100)
        msg = ''
        if self.faltas >= percent_ch:
            msg = 'retido'
        else:
            msg = 'não retido'
        return f" faltas permitidas: {percent_ch} você faltou: {self.faltas} horas,reultado: {msg} por faltas" 
