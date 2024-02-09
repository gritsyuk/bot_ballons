from enum import Enum 

class PaymentTypes(str, Enum):
    QR_CODE = "QR код"
    CASH = "Наличные"
    TERMINAL = "Терминал"
    TRANSFER = "Перевод"
    PAID = "Оплачен был"