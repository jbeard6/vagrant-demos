import web

import subprocess

urls = (
    '/', 'Index'
)

render = web.template.render('templates', base='base')


class Index:

    def hit(self):
        try:
            file_in = open("/vagrant/count.txt", "r")
            count = int(file_in.readline())     # it *is* a text file
            file_in.close()                     
        except:
            open("/vagrant/count.txt", "w").write("0")   # so we don't choke on the first
            open("/vagrant/count.txt", "r").close()      # request
            count = 0     

        file_out = open("/vagrant/count.txt", "w")
        count += 1
        file_out.write(str(count))

        return count

    def GET(self):
        hostname = subprocess.check_output("/bin/hostname").rstrip('\n')
        #hostname = "vagrant"
        hits = self.hit()
        return "%d hits on %s" % (hits, hostname)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
