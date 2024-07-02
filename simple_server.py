from aiohttp import web

async def handle(request):
    return web.Response(text="200 OK")

app = web.Application()
app.router.add_get('/healthz', handle)

if __name__ == '__main__':
    port = 8000
    print(f'Запуск сервера на порту {port}......')
    web.run_app(app, port=port)
