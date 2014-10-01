# ==============================================================================
# DebugLogger.py
#
# Mildly useful debugging decorator.
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from datetime import datetime


# ------------------------------------------------------------------------------
# Decorators
# ------------------------------------------------------------------------------

def debug_logging(func):
    """
    Decorator to print function name before and after calling, arguments, return
    value, and execution time.

    Arguments:
        func<Function> -- Funtion being decorated.

    Returns:
        Wrapped function to call into the decorated function.
    """

    def call_inside(*args, **kwargs):
        """
        Calls into the function being decorated.

        Arguments:
            args<()>   -- Positional arguments to decorated function.
            kwargs<{}> -- Keyword arguments to decorated function.

        Returns:
            Result of the decorated function's execution.
        """
        print '[DEBUG] Entering %s(). ARGS=%s, KWARGS=%s.' % (func.__name__,
            args,
            kwargs)

        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()

        elapsed = end - start

        print '[DEBUG] Exited %s(). Return value=%s. Time=%s' % (func.__name__,
            result,
            elapsed)

        return result

    return call_inside
