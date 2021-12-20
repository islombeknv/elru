from paycomuz import Paycom

paycom = Paycom()
url = paycom.create_initialization(amount=5.00, order_id='197', return_url='https://example.com/success/')
print(url)