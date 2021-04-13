import requests


class APIaccess:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def price(self, year, month, day, hour, minute):
        """ Send get request to server
        """
        req = f"{self.ip}:{self.port}/api/v1/price?" \
              + "year={year}&month={month}&day={day}&hour={hour}&minute={minute}"
        requests.get(req)

    def server_address(self, ip, port):
        """ Setter function for port and ip
        """
        self.ip = ip
        self.port = port

    def del_ticker(self, ticket_id):
        req = f"{self.ip}:{self.port}/api/v1/delete/{ticket_id}"
        requests.post(req)

    def add_ticker(self, ticket_id):
        req = f"{self.ip}:{self.port}/api/v1/add/{ticket_id}"
        requests.post(req)

    def reset(self):
        req = f"{self.ip}:{self.port}/api/v1/reset"
        requests.post(req)
