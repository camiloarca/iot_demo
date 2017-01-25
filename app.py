import web
from web import form

urls = (
    '/','Index',
)

app = web.application(urls, globals())

render = web.template.render('templates', base = 'base')

class Index:

    db = web.database(dbn='mysql', host='localhost', db='arduino', user='root', pw='')

    control = form.Form(
        form.Button("Encender/Apagar", type="Submit", description="Sirve para apagar y encender")
    )


    def GET(self):
        formulario = self.control()
        data = self.db.select('data', order='id DESC', limit= 1)
        control = self.db.select('control', order='id DESC', limit= 1)[0]
        return render.index(data, control, formulario)

    def POST(self):
        formulario = self.control()
        if not formulario.validates():
            pass
        else:
            control = self.db.select('control', order='id DESC', limit= 1)[0]
            print control.value
            value = control.value
            if(value == 1):
                value = 0
            else:
                value = 1

            self.db.update('control', where='id=1', vars= locals(), value=value)
            raise web.seeother('/')


if __name__=='__main__':
    web.config.debug= True
    app.run()