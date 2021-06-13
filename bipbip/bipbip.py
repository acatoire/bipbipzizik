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

    def __init__(self, parameters: dict):
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
        """
        self.parameters = parameters
        self._execution_log = []

    def _parameter(self, param_name:str) -> str or None:
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
