from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorAdiario(Mapeador):
    name = "mapeadoradiario"

    def column(self):
        return "ADIARIO"

    def backup_column(self):
        return "VALID_ADIARIO"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.buriticupu.ma.gov.br/diariooficial
        # https://transparencia.cordeiro.rj.gov.br/jornal.php

        lista = [
            f"{protocol}://www.{city}.{state_code}.gov.br/diariooficial",
            f"{protocol}://transparencia.{city}.{state_code}.gov.br/jornal.php",
        ]

        return lista

    def validation(self, response):
        if "assesi.com.br" in response.text:
            return True
        return False
