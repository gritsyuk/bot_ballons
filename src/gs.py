import gspread_asyncio
from src.settings import config
import logging
from src.utils import (
    from_str_datatime,
    get_index_today,
)
from src.model import OrderFromSheet
from typing import Iterator, List

from google.oauth2.service_account import Credentials


class googleSheetsClient(object):
    def __init__(self, *, credentials_file: str, spread_sheet_id: str, sheet_name: str):
        self.credentials_file = credentials_file
        self.spread_sheet_id = spread_sheet_id
        self.sheet_name = sheet_name
        self.agcm = gspread_asyncio.AsyncioGspreadClientManager(self._get_creds)

    def _get_creds(self):
        creds = Credentials.from_service_account_file(self.credentials_file)
        scoped = creds.with_scopes([
            "https://www.googleapis.com/auth/spreadsheets",
        ])
        return scoped

    async def get_today_orders(self) -> Iterator[List[OrderFromSheet]]:
        agc = await self.agcm.authorize()
        ss = await agc.open_by_key(self.spread_sheet_id)
        sheet = await ss.worksheet(self.sheet_name)
        deliveries_date_col = await sheet.col_values(3)
        deliveries_date_col = deliveries_date_col[1:]
        deliveries_date = list(map(from_str_datatime, deliveries_date_col))

        index_date = get_index_today(deliveries_date)

        data = await sheet.get_all_records()
        result_orders = [data[i] for i in index_date]
        logging.debug(result_orders)

        return map(lambda el:
                   OrderFromSheet.model_validate(el),
                   result_orders)

    async def get_order_by_row(self, row: int) -> List[OrderFromSheet]:
        agc = await self.agcm.authorize()
        ss = await agc.open_by_key(self.spread_sheet_id)
        sheet = await ss.worksheet(self.sheet_name)
        header_values = await sheet.row_values(1)
        data_values = await sheet.row_values(row)
        while len(data_values) < len(header_values):
            data_values.append(None)
        result_dict = dict(zip(header_values, data_values))
        print(result_dict)
        result = [OrderFromSheet.model_validate(result_dict)]
        print(result)
        return result


google_client = googleSheetsClient(credentials_file=config.GOOGLE_CREDENTIALS_FILE,
                                   spread_sheet_id=config.DB_SPREAD_SHEET_ID,
                                   sheet_name=config.DB_SHEET_NAME)

# async def example():
#     google_client = googleSheetsClient(credentials_file=config.GOOGLE_CREDENTIALS_FILE,
#                                        spread_sheet_id=config.DB_SPREAD_SHEET_ID,
#                                        sheet_name=config.DB_SHEET_NAME)
#
#     res = await google_client.get_order_by_row(2140)
#     print(res)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     asyncio.run(example(), debug=True)
