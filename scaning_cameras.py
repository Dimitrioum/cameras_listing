from __future__ import print_function

import logging
import sys


import gphoto2 as gp

def main():
    logging.basicConfig(
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    gp.check_result(gp.use_python_logging())
    context = gp.gp_context_new()
    if hasattr(gp, 'gp_camera_autodetect'):
        # gphoto2 version 2.5+
        cameras = gp.check_result(gp.gp_camera_autodetect(context))
    else:
        port_info_list = gp.check_result(gp.gp_port_info_list_new())
        gp.check_result(gp.gp_port_info_list_load(port_info_list))
        abilities_list = gp.check_result(gp.gp_abilities_list_new())
        gp.check_result(gp.gp_abilities_list_load(abilities_list, context))
        cameras = gp.check_result(gp.gp_abilities_list_detect(
            abilities_list, port_info_list, context))
    n = 0
    for name, value in cameras:
        print('camera number', n)
        print('===============')
        print(name)
        print(value)
        print()
        n += 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
