# function_validator
Function Validator library comes with a req_validator decorator that validates the function keyword argument against its datatype, keyword name, required and logs the keyerror that you provide in the error description.



Installation Instruction!
===================

>- Activate your Virtual Environment.
>- pip install function-validator

----------

**function-validator** is library having req_validator decorator that validates the request parameters.

# Usage

 1. Import function logger library
	 -  `from function_validator import req_validator`

# Example

```python
from function_validator import req_validator

@req_validator(param_name="age", err_description="int not found", req=True, var_type=int)
@req_validator(param_name="name", err_description="string not found", req=True, var_type=basestring)
@req_validator(param_name="quality", err_description="dict not found", req=True, var_type=dict)
@req_validator(param_name="friend_list", err_description="list not found", req=True, var_type=list)
def test_function(**kwargs):
    print kwargs


if __name__ == '__main__':
    test_function(age = 23, name = "Anand", quality = {"height": 172}, friend_list = ["anand"])
```
