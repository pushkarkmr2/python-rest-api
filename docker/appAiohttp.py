import aiohttp
from aiohttp import web, BasicAuth


#Routes################################
routes=web.RouteTableDef()

async def web_on_startup(app):
    # app['session'] = aiohttp.ClientSession(auth=BasicAuth(os.getenv('username'), os.getenv('password')))
    print("Create session on app startup!")

async def web_on_cleanup(app):
    try:
        #await app['session'].close()
        print("Cleanup the session!")
    except:
        pass

@routes.get('/health')
def health(request):
    return web.json_response({"status":"UP"})

if __name__ == '__main__':
    try:
        app = web.Application()
        #app.on_startup.append(web_on_startup)
        #app.on_cleanup.append(web_on_cleanup)
        app.add_routes(routes)
        web.run_app(app, port=8080)
    except Exception as ex:
        print(ex)