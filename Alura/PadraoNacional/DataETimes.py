from datetime import datetime,timedelta

class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_datetime()

    def mes_cadastro(self):
        meses_do_ano = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro',]
        mes_cadasto = meses_do_ano[self.momento_cadastro.month-1]
        return mes_cadasto

    def dia_da_semana(self):
        dias_da_semana = ['segunda','terça','quarta','quinta','sexta','sabado','domingo',]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def format_datetime(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - timedelta(days=1)
        return tempo_cadastro

dataetempo = DatasBR()
print(dataetempo.momento_cadastro)
print(dataetempo.format_datetime())
print(dataetempo.mes_cadastro())
print(dataetempo)
print(dataetempo.tempo_cadastro())