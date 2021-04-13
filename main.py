import sys
import controller, service, APIaccess


def command_line(cmd, args):
    # first argument is file name
    if cmd == "--price":
        controller.price(args)
    elif cmd == "--signal":
        controller.signal(args)
    elif cmd == "--server_address":
        controller.server_address(args)
    elif cmd == "--del_ticker":
        controller.del_ticker(args)
    elif cmd == "--add_ticker":
        controller.add_ticker(args)
    elif cmd == "--reset":
        controller.reset()
    else:
        raise ValueError("Illegal Arguments")


if __name__ == "__main__":
    # instantiate dependency chain
    aal = APIaccess.APIaccess(ip="127.0.0.1", port="8000")
    service = service.Service(APIaccess)
    controller = controller.Controller(service)

    args = sys.argv[1:]
    cmd = args[0]
    args = args[1:]
    command_line(cmd, args)


