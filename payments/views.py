from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz
from paycomuz.views import MerchantAPIView
from paycomuz import Paycom


class CheckOrderAndPayment(ClickUz):

    def check_order(self, order_id: str, amount: str):
        if order_id == '1' and amount == '100':
            return self.ORDER_FOUND
        if order_id == '1' and amount != '100':
            return self.INVALID_AMOUNT
        return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        if order_id != '1':
            raise ValueError


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = CheckOrderAndPayment


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        return self.ORDER_FOUND


def successfully_payment(self, account, transaction, *args, **kwargs):
    print(account)


def cancel_payment(self, account, transaction, *args, **kwargs):
    print(account)


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder

