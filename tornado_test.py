import sys
import threading
import logging
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.log
import tornado.options

logger = logging.getLogger("tornado.application")


class IndexHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.write("Hello, world")
        self.finish()


def make_app():
    logger.info("Making app...")
    args = sys.argv
    args.append("--log_file_prefix=app.log")
    tornado.options.parse_command_line(args)
    return tornado.web.Application(
        [
            (r"/", IndexHandler),
        ],
        autoreload=True)


def start_app():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    logger.info("Starting app...")
    tornado.ioloop.IOLoop.instance().start()
    logger.info("App stopped.")


def stop_app():
    ioloop = tornado.ioloop.IOLoop.instance()
    logger.info("Add stop callback.")
    ioloop.add_callback(ioloop.stop)
    logger.info("Maybe app stopping...")


if __name__ == "__main__":
    thread = threading.Thread(target=start_app)
    thread.start()
    thread.join()
