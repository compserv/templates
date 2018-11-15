#!/usr/bin/env python3

from __future__ import unicode_literals

import json
import os
import sys
import shutil

TEMPLATE_DIR = "templates"
WWW_DIR = os.path.expanduser("~/public_html")
WWW_TEMPLATE_DIR = os.path.join(WWW_DIR, TEMPLATE_DIR)

def main():
    # Add template file names to base page
    with open('templates.html.tmpl') as f:
        content = f.read().replace(
            '{templates}',
            json.dumps(sorted(filter(
                lambda name: not name.startswith('.'),
                os.listdir(TEMPLATE_DIR),
            )))
        )

    # Create main page
    with open(os.path.join(WWW_DIR, 'templates.html'), 'w') as f:
        f.write(content)

    print("created: {}".format(os.path.join(WWW_DIR, 'templates.html')))

    # Sync template directory
    shutil.rmtree(WWW_TEMPLATE_DIR)
    print("rm -r {}".format(WWW_TEMPLATE_DIR))

    shutil.copytree(TEMPLATE_DIR, WWW_TEMPLATE_DIR)
    print("cp -r {} {}".format(TEMPLATE_DIR, WWW_TEMPLATE_DIR))

if __name__ == '__main__':
    sys.exit(main())
