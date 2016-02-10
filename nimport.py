VCS_LIST = ['github','bitbucket']

def nimport(mod):
    try:
        import(mod)
    except:
        vcs = mod.split('.')[0]
        if vcs in VCS_LIST:
            subprocess.call(git, clone, https://+vcs+mod.replace('.','/'))


