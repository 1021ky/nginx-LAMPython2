#!/usr/bin/env python
#
# Ansible managed file, do not edit directly
#
import os
def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    hostname = os.uname()[1]
    return [hostname]