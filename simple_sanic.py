from sanic import Sanic
from sanic import response
from sanic.log import logger as logging
from dask.distributed import Client

app = Sanic(__name__)

fileTime = 3
MAXWORKER = 10

class FileHandlerProcess:
    def __init__(self,time, workers):
        self.time = time
        self.workers = workers
        self.client = Client(asynchronous=True)

@app.listener('before_server_start')
async def setup_connection(app, loop):
    app.handler = FileHandlerProcess(fileTime, MAXWORKER)
    logging.info('Server started')


@app.route("/")
async def test(request):
    return response.json({"test": True})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)