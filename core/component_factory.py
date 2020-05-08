# Copyright 2015-2018 Intel Corporation., Tieto
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

"""Functions for creating controller objects based on deployment or traffic
"""

from core.vswitch_controller_clean import VswitchControllerClean
from core.vswitch_controller_p2p import VswitchControllerP2P
from core.vswitch_controller_pxp import VswitchControllerPXP
from core.vswitch_controller_op2p import VswitchControllerOP2P
from core.vswitch_controller_ptunp import VswitchControllerPtunP


def __init__():
    """Finds and loads all the modules required.

    Very similar code to load_trafficgens().
    """
    pass

def create_vswitch(deployment_scenario, vswitch_class, traffic,
                   tunnel_operation=None):
    """Return a new IVSwitchController for the deployment_scenario.

    The returned controller is configured with the given vSwitch class.

    Deployment scenarios: e.g. 'p2p', 'pvp', 'pvpv12', etc.

    :param deployment_scenario: The deployment scenario name
    :param vswitch_class: Reference to vSwitch class to be used.
    :param traffic: Dictionary with traffic specific details
    :param tunnel_operation encapsulation/decapsulation or None
    :return: IVSwitchController for the deployment_scenario
    """
    # pylint: disable=too-many-return-statements
    deployment = deployment_scenario.lower()
    if deployment.startswith("p2p"):
        return VswitchControllerP2P(deployment, vswitch_class, traffic)
    elif deployment.startswith("pvp"):
        return VswitchControllerPXP(deployment, vswitch_class, traffic)
    elif deployment.startswith("pvvp"):
        return VswitchControllerPXP(deployment, vswitch_class, traffic)
    elif deployment.startswith("pvpv"):
        return VswitchControllerPXP(deployment, vswitch_class, traffic)
    elif deployment.startswith("op2p"):
        return VswitchControllerOP2P(deployment, vswitch_class, traffic, tunnel_operation)
    elif deployment.startswith("ptunp"):
        return VswitchControllerPtunP(deployment, vswitch_class, traffic)
    elif deployment.startswith("clean"):
        return VswitchControllerClean(deployment, vswitch_class, traffic)
    else:
        raise RuntimeError("Unknown deployment scenario '{}'.".format(deployment))
