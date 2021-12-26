from clickuz import ClickUz
from clickuz.views import ClickUzMerchantAPIView


class OrderCheckAndPayment(ClickUz):

    def check_order(self, order_id: str, amount: str):
        pass
        # try:
        #     order_models.Order.objects.get(id=order_id)
        #     return self.ORDER_FOUND
        # except order_models.Order.DoesNotExist:
        #     return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        pass


class ClickTransaction(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment


def create_click_url_via_order(order_id) -> str:
    pass
