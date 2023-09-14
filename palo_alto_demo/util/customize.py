# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate the Resilient customizations required for palo_alto_demo"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the palo_alto_demo package
    """
    return {
        "package": u"palo_alto_demo",
        "message_destinations": [u"palo_alto_firewall_msg"],
        "functions": [u"fp_create_address", u"palo_alto_get_address", u"palo_alto_get_address_in_group", u"palo_alto_get_policy"],
        "workflows": [u"palo_alto_workflow"],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 49.1.52

    Contents:
    - Message Destinations:
        - palo_alto_firewall_msg
    - Functions:
        - fp_create_address
        - palo_alto_get_address
        - palo_alto_get_address_in_group
        - palo_alto_get_policy
    - Workflows:
        - palo_alto_workflow
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)