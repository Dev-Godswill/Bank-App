from django import forms
from . models import Deposit, Withdrawal, Transfer


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields= ('account_id','amount','reference')


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields= ('account_id','amount','reference')


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields= ('sender_id','receiver_id','amount','reference')

