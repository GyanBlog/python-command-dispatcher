
class CommandDispatch:
    def __init__(self):
        # list of commands
        self.commands = {}

    """
    For registering commands
    """
    def for_command(self, cmd):
        def wrap(fn):
            self.commands[cmd] = fn
        return wrap

    """
    For registering invalid command handler
    """
    def invalid(self, fn):
        self.invalidfn = fn

    """
    For registering input method
    """
    def input(self, fn):
        self.inputfn = fn

    """
    Main event loop
    """
    def run(self):
        while True:
            args = self.inputfn()
            self.commands.get(args[0], self.invalidfn)(*args)