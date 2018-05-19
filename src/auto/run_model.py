import logging
import sched, time

from src.auto.auto_model import AutoModel


day_length = 86400  # seconds
week_length = 7     # days


def wait_loop(model, seconds):
    if model.check():
        model.get_data()
    else:
        logger.info('Waiting for new round')
        time.sleep(seconds)
        wait_loop(model, 10)


def main():
    model = AutoModel()
    
    wait_loop(model, 10)
    model.train()
    model.predict()
    model.check()
    model.prepare()
    model.submit()
    model.stake()
    


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger()
    main()
