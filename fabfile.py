from fabric.api import *
from fabric.colors import green, red

def server() :
    """This pushes to the EC2 instance defined below"""
    # The Elastic IP to your server
    env.host_string = ''
    # your user on that system
    env.user = 'ubuntu' 
    # Assumes that your *.pem key is in the same directory as your fabfile.py
    env.key_filename = '~/.ssh/deployment.pem'

def install() :
    # path to the directory on the server where your vhost is set up
    path   = "/var/www"
    domain = ""
    repo   = ""
    # name of the application process
    process = "staging"

    print(red("Beginning Deploy:"))
    print(green("Checking for dist directory"))
    run("[[ -d %s/%s ]] || sudo mkdir -p %s/%s" % (path, domain, path, domain))
    run("sudo chown %s %s/%s" % (env.user, path, domain))
    run("sudo chgrp %s %s/%s" % (env.user, path, domain))

    with cd("%s/%s" % (path, domain)) :
        run("pwd")
        print(green("Pulling master from GitHub..."))
        run("git clone %s ." % repo)
    print(red("DONE!"))

def staging() :
    # path to the directory on the server where your vhost is set up
    path = "/var/www"
    domain = ""
    # name of the application process
    process = "staging"

    print(red("Beginning Deploy:"))
    print(green("Checking for dist directory"))

    with cd("%s/%s" % (path, domain)) :
        run("pwd")
        print(green("Pulling master from GitHub..."))
        run("git pull origin master")
        print(green("Checking for dist directory"))
        run("[[ -d dist ]] || mkdir dist")
        print(green("Executing grunt file"))
        run("npm install; grunt")
        print(green("Creating distribution"))
        run("cp -R css fonts js *.html dist")
    print(red("DONE!"))