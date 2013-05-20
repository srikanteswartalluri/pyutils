#!/usr/bin/env python
#https://fedorahosted.org/cobbler/wiki/CobblerXmlrpc
#https://github.com/cobbler/cobbler/wiki/Cobbler%20web%20interface

import xmlrpclib
remote =  xmlrpclib.Server("https://10.147.40.145/cobbler_api")
token = remote.login("cobbler","password")
systems = remote.get_systems()
for system in systems:
    remote.remove_system(system['name'],token)
remote.sync(token)
# remote.modify_distro(distro_id, 'name',   'example-distro',token)
# remote.modify_distro(distro_id, 'kernel', '/opt/stuff/vmlinuz',token)
# remote.modify_distro(distro_id, 'initrd', '/opt/stuff/initrd.img',token)
# remote.save_distro(distro_id,token)

