from .format import diff, patch, file_diff, file_patch, file_patch_inplace, diff_raw

__version__ = '1.1.6'


def test(verbosity=1):
    from .test_all import run
    return run(verbosity=verbosity)
