import aiohttp
from aiohttp import web

# A simple handler for the / endpoint
async def handle(request):
    return web.json_response({'message': 'Hello, World!'})

# Another endpoint with a dynamic route
async def greet(request):
    name = request.match_info.get('name', "Anonymous")
    return web.json_response({'message': f'Hello, {name}!'})

# Application setup
app = web.Application()

# Define routes
app.router.add_get('/', handle)
app.router.add_get('/greet/{name}', greet)

# Running the application
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
