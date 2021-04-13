class Controller:
    def __init__(self, service):
        """ Controller Object
        """
        self.service = service

    def price(self, dt):
        """
        """
        if self.__validate_date(dt):
            return self.service.price(dt)
        else:
            raise ValueError("Invalid date and time")

    def signal(self, dt):
        """
        """
        if self.__validate_date(dt):
            return self.service.signal(dt)
        else:
            raise ValueError("Invalid date and time")

    def server_address(self, args):
        """ Connect to a server
        if not specified, default to
        127.0.0.1:8000
        """
        server = args.split(':')
        ip, port = server
        return self.service.server_address(ip, port)

    def del_ticker(self, args):
        """ Delete ticker
        """
        ticket = args[0]
        return self.server.del_ticker(ticket)

    def add_ticker(self, args):
        """ Add ticket
        """
        ticket = args[0]
        return self.server.del_ticker(ticket)

    def reset(self):
        """ Reset all data.
        """
        return self.server.reset()


    @staticmethod
    def __validate_date(self, dt):
        """ Validate date from CLI
        raise ValueError if invalid
        """
        dt_list = dt.split('-')
        t = dt_list[-1]
        t = t.split(':')
        if len(dt_list) != 4 or len(t) != 2:
            return False
        else:
            return True


