Scalizer Unit Tests
===================

This module helps to manage unit tests on Odoo.sh platform.

This is a technical module. This requires a custom module to inherit it.

## Table of contents

* [Usage](#usage)
  * [Skip failing python unit tests](skip-failing-python-unit-tests)
  * [Avoid warnings on fields](avoid-warnings-on-fields)
* [Contributors](#contributors)
* [Maintainers](#maintainers)

## Usage

### Create a custom module

Create a custom module (s6r_my_project_unit_tests for example) add `s6r_unit_tests` in the dependencies. 

In the manifest, set `'auto_install': True`


### Skip failing python unit tests

In the custom module, in `tests` directory, add a file `runner.py` and override the `get_excluded_tests` function like in the example bellow.

- `class` can take the value `all` to skip all the test classes of the module.
- `method` can take the value `all` to skip all the test methods of the class.

```python
from odoo.addons.s6r_unit_tests.tests.runner import OdooTestResult
def get_excluded_tests():
    return [
        {'module': 'auth_totp', 'class': 'TestTOTP', 'method': 'test_totp'},
        {'module': 'website', 'class': 'Crawler', 'method': 'all'},
    ]

OdooTestResult.get_excluded_tests = get_excluded_tests
```


### Avoid warnings on fields

In the custom module, in `models` directory, add a file `logging.py` and override the `get_fields_message_to_skip` function like in the example bellow.

`msg` must be contained in the warning message to skip. 

```python
from odoo.fields import _logger as fields_logger
def get_fields_message_to_skip():
    return [{
        'msg': "overrides existing selection; use selection_add instead",
        'fields': ['res.partner.my_selection_field',
                   'sale.order.other_selection_field']
    }]

fields_logger.get_fields_message_to_skip = get_fields_message_to_skip
```


### Avoid warning or error messages from Chrome browser tests

In the custom module, in `tests` directory, add a file `common.py` and override the `get_console_message_to_skip` function like in the example bellow.

`type` can be 'warning' or 'error'. 
`msg` must be contained in the browser message to skip. 

```python
from odoo.addons.s6r_unit_tests.tests.common import ChromeBrowser
def get_console_message_to_skip(self)::
    return [
        {'type': 'warning',
         'msg': 'Smartlook is stopped'}
    ]

ChromeBrowser.get_console_message_to_skip = get_console_message_to_skip
```

## Authors

* Scalizer

## Contributors

* Michel Perrocheau ([Github](https://github.com/myrrkel))

## Maintainers

This module is maintained by [Scalizer](https://www.scalizer.fr).

![Scalizer](./static/description/logo.png)


