import logging
import os


def configure_logging(app):
    """
    Configure application logging.
    """

    log_folder = "logs"

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logging.basicConfig(
        filename=os.path.join(log_folder, "app.log"),
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    app.logger.info("Application Started")