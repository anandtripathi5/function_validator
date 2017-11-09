from functools import wraps

__author__ = "Anand Tripathi"
__version__ = "0.1"


def req_validator(param_name=None, err_description=None,
                  req=False, var_type=basestring, default_val=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                if req:
                    val = kwargs[param_name]
                else:
                    val = kwargs.get(param_name) if kwargs.get(param_name) else default_val
                    if val:
                        kwargs.update(param_name=val)
            except KeyError:
                raise KeyError(err_description)
            if type(val) == var_type:
                return fn(*args, **kwargs)
            elif isinstance(val, var_type) and val:
                return fn(*args, **kwargs)
            elif not val and (not req):
                return fn(*args, **kwargs)
            raise ValueError(err_description)
        return decorator
    return wrapper

