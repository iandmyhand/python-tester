import time


class C(object):

    async def heavy_stuff(self):
        await time.sleep(3)
        return {"something": "like that..."}

    async def get_something(self):
        result = await self.heavy_stuff()
        return result


if "__main__" == __name__:
    c = C()
    something = c.get_something()
    print(str(something))


