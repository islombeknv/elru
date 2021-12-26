from orders.models import OrderModel
from payment_system.views import MerchantAPIView
from payment_system import Paycom
from payment_system import status


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        try:
            order = OrderModel.objects.get(order_id=account['order'])
            if order.price != amount:
                return status.INVALID_AMOUNT
            return status.ORDER_FOUND
        except:
            return status.ORDER_NOT_FOND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        pass

    def cancel_payment(self, account, transaction, *args, **kwargs):
        pass


class PayMeView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


def create_pay_me_url_via_order(order_id) -> str:
    try:
        order = OrderModel.objects.get(order_id=order_id)
        payme = Paycom()
        url = payme.create_initialization(amount=order.price, order_id=str(order.order_id), return_url='https://tutto.uz/')
        return url
    except order.DoesNotExist:
        return 'https://tutto.uz/'
