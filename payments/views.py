from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz

from orders.models import OrderModel


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        try:
            ord = OrderModel.objects.get(order_id=account['order_id'])
        except OrderModel.DoesNotExist:
            ord = None
        if not (ord):
            return self.ORDER_NOT_FOND
        else:
            if ord.status == 'created':
                if ord.price == amount:
                    return self.ORDER_FOUND
                else:
                    return self.INVALID_AMOUNT
            else:
                return self.ORDER_NOT_FOND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        try:
            ord = OrderModel.objects.get(order_id=transaction.order_key)
        except ord.DoesNotExist:
            ord = None
        ord.status = 'Kutilmoqda'
        ord.save()

    def cancel_payment(self, account, transaction, *args, **kwargs):

        try:
            ord = OrderModel.objects.get(order_id=transaction.order_key)
        except ord.DoesNotExist:
            ord = None
        ord.status = 'Kutilmoqda'
        ord.save()


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
