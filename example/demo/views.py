import aiohttp_jinja2
from aiohttp import web

from demo.models import sa_demo_test


async def json_view(request):
    name = request.match_info["name"]
    return web.json_response({"name": name})


class HelloView(web.View):

    async def get(self):
        name = self.request.match_info["name"]
        reverse_url = self.request.app.router.named_resources()[
            'hello'].url_for(name=name)
        return web.Response(
            text="Hello [{}], world\nreverse_url = [{}]".format(name,
                                                                reverse_url))


class IndexView(web.View):

    @aiohttp_jinja2.template('demo/index.html')
    async def get(self):
        name = self.request.match_info["name"]
        return {"name": name}


class InsertData(web.View):

    async def get(self):
        name = self.request.match_info["name"]
        async with self.request.app['db'].acquire() as conn:
            insert_sql = sa_demo_test.insert().prefix_with('IGNORE').values(
                name=name)
            await conn.execute(insert_sql)
            await conn.execute('commit')
        return web.json_response({"msg": "insert data over"})
