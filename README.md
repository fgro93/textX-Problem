# textX-Problem and Solution
I used python 3.7, textX 1.7.1

```
Traceback (most recent call last):
  File "...\textX-Problem\Main.py", line 39, in <module>
    f = f_mm.model_from_file("main.fmodel")
  File "...\textx-1.7.1-py3.7.egg\textx\metamodel.py", line 505, in model_from_file
    return self.internal_model_from_file(file_name, encoding, debug)
  File "...\textx-1.7.1-py3.7.egg\textx\metamodel.py", line 542, in internal_model_from_file
    is_main_model=is_main_model)
  File "...\textx-1.7.1-py3.7.egg\textx\model.py", line 260, in get_model_from_file
    is_main_model=is_main_model, encoding=encoding)
  File "...\textx-1.7.1-py3.7.egg\textx\model.py", line 285, in get_model_from_str
    is_main_model=is_main_model, encoding=encoding)
  File "...\textx-1.7.1-py3.7.egg\textx\model.py", line 636, in parse_tree_to_objgraph
    m._tx_reference_resolver.resolve_one_step()
  File "...\textx-1.7.1-py3.7.egg\textx\model.py", line 747, in resolve_one_step
    obj, attr, crossref)
  File "...\textX-Problem\Main.py", line 11, in __call__
    if port.interface.name == obj_ref.obj_name:
AttributeError: 'NoneType' object has no attribute 'name'
```
Solution: Using [Postponed](https://textx.readthedocs.io/en/stable/scoping/#technical-aspects-and-implementation-details)
For more details: https://github.com/igordejanovic/textX/issues/83
