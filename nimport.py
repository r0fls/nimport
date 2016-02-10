import os

VCS_LIST = ['github','bitbucket']

def nimport(mod):
    m = mod.split('.')
    try:
        mod = '.'.join(m[1:])
        exec("mod = __import__(mod)")
    except Exception, e:
        vcs = m[0]
        m = '/'.join(m[1:])
        print(e)
        if vcs in VCS_LIST:
            os.system('git clone https://{0}.com/{1}'.format(vcs,m))
