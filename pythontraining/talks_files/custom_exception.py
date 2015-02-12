__author__ = 'talluri'

class InstanceCreationException(Exception):
    pass

class HyperVisorDownError(Exception):
    def __init__(self,id):
        self.id = id

def create_instance(*args, **kwargs):
    hypervisor = 20
    if kwargs['ram'] == '4GB':
        return Instance()
    else:
        raise HyperVisorDownError(hypervisor-1)


class Instance:
    pass

instanceObj = create_instance(ram='4GB')

try:
    create_instance(ram = '8GB')
    create_instance(rarm = '8GB')
except HyperVisorDownError as e:
    print 'Instance id : {} creation failed'.format(e.id)
except KeyError as f:
    print 'key error:'+ f.message


# i = InstanceCreationException(e)
# print i.id
print 'i have gone mad'
#raise HyperVisorDownError(26)