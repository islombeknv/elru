from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz

from orders.models import OrderModel


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        amount = amount / 100
        order_id = account['order']
        try:
            order = OrderModel.objects.get(order_id=order_id)
            if order.price != amount:
                return self.INVALID_AMOUNT
            return self.ORDER_FOUND
        except OrderModel.DoesNotExist:
            return self.ORDER_NOT_FOND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        order = OrderModel.objects.get(order_id=transaction.order_key)
        order.pay = 'payme'
        order.save()

    def cancel_payment(self, account, transaction, *args, **kwargs):
        order = OrderModel.objects.get(order_id=transaction.order_key)
        order.pay = 'cancelled'
        order.save()


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


# ----------------------------------------
class CheckOrderAndPayment(ClickUz):

    def check_order(self, order_id: str, amount: str):
        try:
            order = OrderModel.objects.get(order_id=order_id)
            if order.order_id == order_id and order.price == float(amount):
                return self.ORDER_FOUND
            if order.order_id == order_id and order.price != float(amount):
                return self.INVALID_AMOUNT
            return self.ORDER_NOT_FOUND
        except:
            return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        order = OrderModel.objects.get(order_id=order_id)
        order.pay = 'click'
        order.save()


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = CheckOrderAndPayment
