from pydantic import BaseModel, Field, field_validator
from typing import Union
from datetime import datetime, time

class OrderFromSheet(BaseModel):
    created_at: datetime | None = Field(alias='Отметка времени')
    client_name: str | None = Field(alias='Имя Клиента')
    deliver_at: datetime = Field(alias='Дата заказа')
    adress: str | None = Field(alias='Адрес доставки')
    price_order: int = Field(alias='Сумма заказа')
    price_deliver: int | str = Field(alias='Сумма доставки', )
    pay_type: str | None = Field(alias='Оплата')
    info: str | None = Field(alias='Доп инфа к заказу')
    comment: str | None = Field(alias='Комментарий к заказу')
    client_phone: int = Field(alias='Телефон Клиента')
    client_from: str | None = Field(alias='Откуда заказчик')
    deadline_time: str | None = Field(alias='До какого часа доставка')
    client_is_new: str | None = Field(alias='Заказчик новый или старый?')
    self_pickup: bool | None = Field(default=False)

    @field_validator("created_at", "deliver_at", mode='before')
    @classmethod
    def from_str_datatime(cls, value):
        if isinstance(value, datetime):
            return value
        """Faster then strptime"""
        try:
            date_time = value.split(' ')
            day_s, mon_s, year_s = date_time[0].split('.')
            h, m, s = date_time[1].split(':')
            return datetime(int(year_s), 
                            int(mon_s), 
                            int(day_s), 
                            int(h), 
                            int(m), 
                            int(s))
        except ValueError:
            return None
    
    @field_validator("self_pickup", mode='before')
    @classmethod
    def set_self_pickup(cls, value):
        if value == "Самовывоз":
            return True

    # @field_validator("price_order", "price_deliver", mode='before')
    # @classmethod
    # def to_int(cls, value):
    #     if isinstance(value, int):
    #         return value
    #     if value is None:
    #         return 0
    #     return int(value)
        