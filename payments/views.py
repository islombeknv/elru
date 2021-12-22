from paycomuz.views import MerchantAPIView
from paycomuz import Paycom

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


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder
