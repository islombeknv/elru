from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz

from orders.models import OrderModel


class CheckOrder(Paycom):
    class CheckOrder(Paycom):
        def check_order(self, amount, account, *args, **kwargs):
            if 35 == account['order_id'] and 100.01 == amount:
                return self.ORDER_FOUND
            elif 35 == account['order_id'] and 100.01 != amount:
                return self.INVALID_AMOUNT
            return self.ORDER_NOT_FOND

        def successfully_payment(self, account, transaction, *args, **kwargs):
            print(account)

        def cancel_payment(self, account, transaction, *args, **kwargs):
            print(account)


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


# ----------------------------------------
class CheckOrderAndPayment(ClickUz):

    def check_order(self, order_id: str, amount: str):
        try:
            order = OrderModel.objects.get(order_id=order_id)
        except order.DoesNotExist:
            order = None
        if order.order_id == order_id and order.price == float(amount):
            return self.ORDER_FOUND
        elif order.order_id == order_id and order.price != float(amount):
            return self.INVALID_AMOUNT
        return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        try:
            order = OrderModel.objects.get(order_id=order_id)
        except order.DoesNotExist:
            order = None
        order.pay = 'click'
        order.save()


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = CheckOrderAndPayment
