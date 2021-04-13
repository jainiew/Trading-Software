from datetime import datetime
from signal import Signal
import pandas as pd

class Service:
    def __init__(self, apia):
        self.apia = apia

    def price(self, dt):
        year, month, day, hour, minute = self.__datify(dt)
        return self.apia.price(year, month, day, hour, minute)

    def signal(self, dt):
        pd_dt = self.__pd_dt(dt)
        sig = Signal()
        return sig.strategy(pd_dt)

    def server_address(self, ip="127.0.0.1", port=8000):
        if not self.__validate_server_address(ip, port):
            raise ValueError("Invalid IP address or port number")
        return self.apia.server_address(ip, port)

    def del_ticker(self, ticket_id):
        return self.apia.del_ticket(ticket_id)

    def add_ticker(self, ticket_id):
        return self.apia.add_ticker(ticket_id)

    @staticmethod
    def __pd_dt(self, dt):
        """ validate datetime
        """
        try:
            return pd.to_datetime(dt)
        except ValueError:
            print("Invalid IP address or port number")

    @staticmethod
    def __validate_server_address(self, ip, port):
        try:
            return ip.count(".") == 3 and all(0 <= int(i) <= 255 for i in ip.split(".")) and port.isdigit()
        except ValueError:
            print("Invalid IP address or port number")

    @staticmethod
    def __datify(self, dt):
        dt_list = dt.split('-')
        year, month, day, t = dt_list
        t = t.split(':')
        return year, month, day, t[0], t[1]
