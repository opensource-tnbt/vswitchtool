# Copyright 2015-2017 Intel Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Loader module definition.
"""

from conf import settings
from core.loader.loader_servant import LoaderServant
from vswitches.vswitch import IVSwitch

# pylint: disable=too-many-public-methods
class Loader(object):
    """Loader class - main object context holder.
    """
    _vswitch_loader = None

    def __init__(self):
        """Loader ctor - initialization method.

        All data is read from configuration each time Loader instance is
        created. It is up to creator to maintain object life cycle if this
        behavior is unwanted.
        """
        self._vswitch_loader = LoaderServant(
            settings.getValue('VSWITCH_DIR'),
            settings.getValue('VSWITCH'),
            IVSwitch)

    def get_vswitch(self):
        """Returns instance of currently configured vswitch implementation.

        :return: IVSwitch implementation if available, None otherwise.
        """
        return self._vswitch_loader.get_class()()

    def get_vswitch_class(self):
        """Returns type of currently configured vswitch implementation.

        :return: Type of IVSwitch implementation if available.
            None otherwise.
        """
        return self._vswitch_loader.get_class()

    def get_vswitches(self):
        """Returns dictionary of all available vswitches.

        :return: Dictionary of vswitches.
            - key: name of the class which implements IVSwitch,
            - value: Type of vswitch which implements IVSwitch.
        """
        return self._vswitch_loader.get_classes()

    def get_vswitches_printable(self):
        """Returns all available vswitches in printable format.

        :return: String containing printable list of vswitches.
        """
        return self._vswitch_loader.get_classes_printable()
