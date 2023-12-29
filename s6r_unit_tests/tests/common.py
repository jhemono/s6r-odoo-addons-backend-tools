# Copyright 2023 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import ChromeBrowser
_handle_console_origin = ChromeBrowser._handle_console


def get_console_message_to_skip(self):
    """
    Returns a list of dict of excluded Chrome browser console messages.
    [
        {'type': 'warning',
         'msg': 'Smartlook is stopped'},
    ]
    """
    return []


ChromeBrowser.get_console_message_to_skip = get_console_message_to_skip


def _handle_console(self, type, args=None, stackTrace=None, **kw):
    if args and isinstance(args[0], dict) and args[0].get('value'):
        for msg_to_skip in self.get_console_message_to_skip():
            if msg_to_skip['type'] == type:
                if msg_to_skip['msg'] in args[0].get('value'):
                    return
    _handle_console_origin(self, type, args, stackTrace, **kw)


ChromeBrowser._handle_console = _handle_console
