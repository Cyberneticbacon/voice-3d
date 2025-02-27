from talon import Module, Context, actions
import xmlrpc.client
mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def send_rpc_message(message: str):
        """Send a message to the RPC"""
        proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
        print(proxy.parse_command(message))
