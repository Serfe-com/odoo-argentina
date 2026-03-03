# -*- coding: utf-8 -*-
import sys

try:
    import httplib2
    import platform

    # Only patch if not already patched
    if getattr(httplib2, "_patched_ssl_context", False) is False:
        _orig_build_ssl_context = httplib2._build_ssl_context

        def _patched_build_ssl_context(disable_ssl_certificate_validation, ca_certs):
            ctx = _orig_build_ssl_context(disable_ssl_certificate_validation, ca_certs)
            # reduce SSL security level to avoid "DH_KEY_TOO_SMALL"
            ctx.set_ciphers("DEFAULT@SECLEVEL=1")
            return ctx

        httplib2._build_ssl_context = _patched_build_ssl_context
        httplib2._patched_ssl_context = True

except ImportError:
    pass  # httplib2 not installed yet