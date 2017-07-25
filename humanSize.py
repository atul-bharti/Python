#this
suffixes = {1000:['KB','MB','GB','TB'],
            1024:['KiB','MiB','GiB','TiB']}
is_size_in_1024 = True

def readableSize(size,is_size_in_1024=True):
    '''Hi This is test Python Programm'''
    if size < 0:
        raise ValueError('number must be non-negative')
    multiple = 1024 if is_size_in_1024 else 1000
    for suffix in suffixes[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError("Size is too Big")

str = 'asdfg'
 
if __name__ == '__main__':
    print (readableSize(1000000000000,False))
    print (readableSize(100))