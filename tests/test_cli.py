try:
    from unittest import mock
except ImportError:
    import mock

from ballistics import cli


def test_main():
    assert cli.main([]) == 0


def test_module_main():
    from ballistics import __main__ as module
    with mock.patch.object(module, "main", return_value=42):
        with mock.patch.object(module, "__name__", "__main__"):
            with mock.patch.object(module.sys, 'exit') as mock_exit:
                module.module_main()
                assert mock_exit.call_args[0][0] == 42
