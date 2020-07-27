from requests import Request


class Bee:

    def __init__(self, token):
        self._url = 'https://bee.cash/api/'

        self._headers = {
            'WWW-Authenticate': 'Token',
            'Authorization': 'Token {}'.format(token),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }


    def _execute(self, end_point, array = {}, method = 'post'):
        return Request(method,
            url=self._url+end_point,
            json=array,
            headers=self._headers
        ).json()


    def altcoin_address(self, array = {}):
        return self._execute('altcoin/address', array)


    def altcoin_withdrawal(self, array = {}):
        return self._execute('altcoin/withdrawal', array)


    def balance(self, coin = ''):
        return self._execute(f'balance/{coin}', method='get')


    def bank_deposit_boleto(self, array):
        return self._execute('bank/deposit/boleto', array)


    def charge_boleto(self, array = {}):
        return self._execute('charge/boleto', array)


    def charge_boleto_receive_in_cash(self, boleto_id):
        return self._execute(f'charge/boleto/{boleto_id}/receive-in-cash')


    def charge_client(self, array = {}):
        return self._execute('charge/client', array)


    def coin(self, coin = ''):
        return self._execute(f'coin/{coin}', {}, 'get')


    def transfer(self, array = {}):
        return self._execute('transfer', array)
