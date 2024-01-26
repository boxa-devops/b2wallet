from django.urls import path
from .views import WalletListCreateView, WalletDetailView, TransactionListCreateView, TransactionDetailView

urlpatterns = [
    path('wallets/', WalletListCreateView.as_view(), name='wallet-list-create'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),

    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
]
