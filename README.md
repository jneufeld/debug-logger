Python Debug Logger
===================

What
----
A mildly useful debug decorator for Python. Prints useful things like a
function's execution time, its arguments and return value, and its name.

How
---
Import the module and decorate!

```
from DebugLogging import debug_logging

@debug_logging
def add(x, y):
    return x + y
```

Hopefully it looks something like this:

```
[DEBUG] Entering add(). ARGS=(2, 3), KWARGS={}.
[DEBUG] Exited add(). Return value=5. Time=0:00:00.000029
```

Why
---
On most projects, at some point I find myself mucking with print and doing
the leg work manually. This will probably prove handy.
