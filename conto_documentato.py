#!/usr/bin/env python3
## @file conto_documentato.py
# @brief Implementazione di un semplice conto bancario.


## @brief Gestisce un conto bancario con intestatario e saldo.
class ContoBancario:

    ## @brief Crea un nuovo conto con saldo a 0.
    # @param intestatario Nome del titolare del conto.
    def __init__(self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0

    ## @brief Aggiunge denaro al conto.
    # @param importo Somma da depositare.
    def deposita(self, importo):
        self.saldo += importo

    ## @brief Preleva denaro dal conto se il saldo è sufficiente.
    # @param importo Somma da prelevare.
    # @raises ValueError Se il saldo è inferiore all'importo richiesto.
    def preleva(self, importo):
        if self.saldo < importo:
            raise ValueError('Saldo insufficiente')
        else:
            self.saldo -= importo

    ## @brief Restituisce i dati del conto in formato testo.
    # @return Stringa con intestatario e saldo attuale.
    def __str__(self):
        return f'Conto di {self.intestatario} saldo: {self.saldo}'


## @brief Funzione di test per la classe ContoBancario.
def main():
    conto = ContoBancario("Mario Rossi")
    print(conto)
    conto.deposita(200)
    conto.preleva(50)
    conto.preleva(25)
    print(conto)
    try:
        conto.preleva(700)
    except ValueError as e:
        print('Operazione rifiutata:', e)


if __name__ == "__main__":
    main()