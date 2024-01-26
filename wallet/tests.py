from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Wallet, Transaction


class WalletTests(APITestCase):
    def setUp(self):
        self.wallet_data = {
            'label': 'Test Wallet', 'balance': 100.0
        }
        self.wallet = Wallet.objects.create(**self.wallet_data)
        self.wallet_url = reverse('wallet-list-create')

    def test_create_wallet(self):
        response = self.client.post(self.wallet_url, self.wallet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.last().label, 'Test Wallet')

    def test_get_wallet_list(self):
        response = self.client.get(self.wallet_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), Wallet.objects.count())

    def test_get_wallet_detail(self):
        wallet_detail_url = reverse('wallet-detail', args=[self.wallet.id])
        response = self.client.get(wallet_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], str(self.wallet.id))
        self.assertEqual(response.data['data']['attributes']['label'], 'Test Wallet')


class TransactionTests(APITestCase):
    def setUp(self):
        self.wallet = Wallet.objects.create(label='Test Wallet', balance=100.0)

        self.transaction_data = {
            'wallet': self.wallet.id,
            'txid': '123456',
            'amount': 50.0
        }

        self.transaction = Transaction.objects.create(**self.transaction_data)

        self.transaction_url = reverse('transaction-list-create')

    def test_create_transaction(self):
        response = self.client.post(self.transaction_url, self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.last().txid, '123456')

    def test_get_transaction_list(self):
        response = self.client.get(self.transaction_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), Transaction.objects.count())

    def test_get_transaction_detail(self):
        transaction_detail_url = reverse('transaction-detail', args=[self.transaction.id])
        response = self.client.get(transaction_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], str(self.transaction.id))
        self.assertEqual(response.data['data']['attributes']['txid'], '123456')
