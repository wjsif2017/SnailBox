# This file is not meant for public use and will be removed in SciPy v2.0.0.
# Use the `scipy.spatial` namespace for importing the functions
# included below.

# from utils.scipy._lib.deprecation import _sub_module_deprecation
import warnings
from importlib import import_module

__all__ = [  # noqa: F822
    'Rotation',
    'Slerp',
]


def __dir__():
    return __all__


def __getattr__(name):
    return _sub_module_deprecation(sub_package="spatial.transform", module="rotation",
                                   private_modules=["_rotation"], all=__all__,
                                   attribute=name)


def _sub_module_deprecation(*, sub_package, module, private_modules, all,
                            attribute, correct_module=None):
    """Helper function for deprecating modules that are public but were
    intended to be private.

    Parameters
    ----------
    sub_package : str
        Subpackage the module belongs to eg. stats
    module : str
        Public but intended private module to deprecate
    private_modules : list
        Private replacement(s) for `module`; should contain the
        content of ``all``, possibly spread over several modules.
    all : list
        ``__all__`` belonging to `module`
    attribute : str
        The attribute in `module` being accessed
    correct_module : str, optional
        Module in `sub_package` that `attribute` should be imported from.
        Default is that `attribute` should be imported from ``scipy.sub_package``.
    """
    if correct_module is not None:
        correct_import = f"scipy.{sub_package}.{correct_module}"
    else:
        correct_import = f"scipy.{sub_package}"

    if attribute not in all:
        raise AttributeError(
            f"`scipy.{sub_package}.{module}` has no attribute `{attribute}`; "
            f"furthermore, `scipy.{sub_package}.{module}` is deprecated "
            f"and will be removed in SciPy 2.0.0."
        )

    attr = getattr(import_module(correct_import), attribute, None)

    if attr is not None:
        message = (
            f"Please import `{attribute}` from the `{correct_import}` namespace; "
            f"the `scipy.{sub_package}.{module}` namespace is deprecated "
            f"and will be removed in SciPy 2.0.0."
        )
    else:
        message = (
            f"`scipy.{sub_package}.{module}.{attribute}` is deprecated along with "
            f"the `scipy.{sub_package}.{module}` namespace. "
            f"`scipy.{sub_package}.{module}.{attribute}` will be removed "
            f"in SciPy 1.14.0, and the `scipy.{sub_package}.{module}` namespace "
            f"will be removed in SciPy 2.0.0."
        )

    warnings.warn(message, category=DeprecationWarning, stacklevel=3)

    for module in private_modules:
        try:
            return getattr(import_module(f"scipy.{sub_package}.{module}"), attribute)
        except AttributeError as e:
            # still raise an error if the attribute isn't in any of the expected
            # private modules
            if module == private_modules[-1]:
                raise e
            continue