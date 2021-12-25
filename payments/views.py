from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        return self.ORDER_FOUND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        print(account)

    def cancel_payment(self, account, transaction, *args, **kwargs):
        print(account)


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


# ----------------------------------------
class CheckOrderAndPayment(ClickUz):

    def check_order(self, order_id: str, amount: str):
        return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        print(order_id)


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = CheckOrderAndPayment
