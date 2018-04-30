import logging
import my_module
import util
import os

util.setup_logging(
    default_path=os.path.join(
        os.path.dirname(__file__), '..', 'logging.json')
)


def main():
    logging.info("ok")
    logging.error("uh oh")
    c = my_module.ClassA('test')
    c.my_method()


if __name__ == "__main__":
    # execute only if run as a script
    main()
