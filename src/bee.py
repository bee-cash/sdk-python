from requests import post


class Bee:

    def __init__(self, token):
        self._url = 'https://bee.cash/api/'

        self._headers = {
            'WWW-Authenticate': 'Token',
            'Authorization': 'Token {}'.format(token),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }


    def _execute(self, end_point, array = {}):
        return post(
            url=self._url+end_point,
            json=array,
            headers=self._headers
        ).json()


    def altcoin_address_create(self, array = {}):
        return self._execute('altcoin/address/create', array)


    def altcoin_withdrawal_create(self, array = {}):
        return self._execute('altcoin/withdrawal/create', array)


    def balance(self, coin = ''):
        return self._execute('balance', {'coin': coin})


    def bank_deposit_boleto_create(self, array):
        return self._execute('bank/deposit/boleto/create', array)


    def charge_boleto_create(self, array = {}):
        return self._execute('charge/boleto/create', array)


    def charge_boleto_receive_in_cash(self, boleto_id):
        return self._execute('charge/boleto/receive-in-cash', {'boleto_id': boleto_id})


    def charge_client_create(self, array = {}):
        return self._execute('charge/client/create', array)


    def coin_list(self):
        return self._execute('coin/list')


    def coin_info(self, coin = ''):
        return self._execute('coin/info', {'coin': coin})


    def transfer_create(self, array = {}):
        return self._execute('transfer/create', array)
