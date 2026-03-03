# -*- coding: utf-8 -*-
import sys

try:
    import httplib2

    # corregir temas de negociacion de SSL en algunas versiones de ubuntu:
    import platform

    monkey_patch = sys.version_info < (3, ) or httplib2._build_ssl_context.__module__ != "httplib2"
    needs_patch = platform.system() == 'Linux' or sys.version_info > (3, 10)
    if needs_patch and not monkey_patch:
        _build_ssl_context = httplib2._build_ssl_context

        def _build_ssl_context_new(*args, **kwargs):
            context = _build_ssl_context(*args, **kwargs)
            # fix ssl.SSLError: [SSL: DH_KEY_TOO_SMALL] dh key too small
            context.set_ciphers("DEFAULT@SECLEVEL=1")
            # context.set_ciphers("AES128-SHA")
            return context

        httplib2._build_ssl_context = _build_ssl_context_new

except ImportError:
    pass  # httplib2 not installed yet