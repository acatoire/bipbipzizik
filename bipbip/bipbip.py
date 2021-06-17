"""
Bip bip object class
"""
import logging
import time

logger = logging.getLogger("bipbip")


class BipBip:
    """
    The generic bipbip class
    """

    def __init__(self, parameters: dict, multi_read_timeout: int or float = 3):
        """
        :param parameters: Parameter dict, each BipBip can implement its own parameters
                  Generic parameters are:
                        name: The BipBip (card) Name
                        ids: list of ids that will run this BipBip
                        comment: BipBip comment
                        mode:
                        action: type of action to be executed
                        data: extra data related to the action
                        user: allowed user for the card
        :param multi_read_timeout: (optional) Value to consider a multi read, default 3s
        """
        self.parameters = parameters
        self.multi_read_timeout = multi_read_timeout
        self._execution_log = []

        self.locked = False

    def _parameter(self, param_name: str) -> str or None:
        try:
            return self.parameters[param_name]
        except KeyError:
            logger.error("The bipbip object doesn't have any parameter named %s.", param_name)
            return None

    @property
    def name(self) -> str or None:
        """
        Name of the bipbip
        :return:
        """
        return self._parameter("name")

    @property
    def ids(self) -> list[str] or None:
        """
        Ids of the bipbip
        :return:
        """
        return self._parameter("ids")

    @property
    def comment(self) -> str or None:
        """
        Comment of the bipbip
        :return:
        """
        return self._parameter("comment")

    @property
    def mode(self) -> str or list[str] or None:
        """
        Mode of the bipbip
        :return:
        """
        return self._parameter("mode")

    @property
    def action(self) -> str or None:
        """
        Action of the bipbip
        :return:
        """
        return self._parameter("action")

    @property
    def data(self) -> str or None:
        """
        Data of the bipbip
        :return:
        """
        return self._parameter("data")

    @property
    def user(self) -> str or None:
        """
        User of the bipbip
        :return:
        """
        return self._parameter("user")

    @property
    def execution_log(self) -> list or None:
        """
        Execution log of the bipbip
        :return:
        """
        return self._execution_log

    def execute(self):
        """
        Execute of the bipbip
        :return:
        """
        self._execution_log.append(time.time())
        logger.info("Execute the bipbip: %s", self.name)

        if len(self.execution_log) > 1:
            last_time_period = (self.execution_log[-1] - self.execution_log[-2])
            if last_time_period < self.multi_read_timeout:
                self.locked = True
            else:
                self.locked = False

        self.start()

    def start(self):
        """
        Action of the bipbip to be overwritten by the child class
        :return:
        """

        ####################################################
        # ## Cancel conditions sample
        ####################################################
        if self.locked:
            logger.warning("Action canceled because of the %ds multi read protection.", self.multi_read_timeout)
            return

        logger.info("ACTION")
