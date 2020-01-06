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
            params=array,
            headers=self._headers
        ).json()


    def altcoin_address_create(self, array = {}):
        return self._execute('altcoin/address/create', array)


    def altcoin_withdrawal_create(self, array = {}):
        return self._execute('altcoin/withdrawal/create', array)


    def balance(self, coin = ''):
        return self._execute('balance', {'coin': coin})


    def coin_list(self):
        return self._execute('coin/list')


    def coin_info(self, coin = ''):
        return self._execute('coin/info', {'coin': coin})


    def invoice_create(self, array = {}):
        return self._execute('invoice/create', array)


    def invoice_pay(self, array = {}):
        return self._execute('invoice/pay', array)


    def invoice_view(self, array = {}):
        return self._execute('invoice/view', array)


    def transfer_create(self, array = {}):
        return self._execute('transfer/create', array)


    def user_info(self, username = ''):
        return self._execute('user/info', {'username': username})
