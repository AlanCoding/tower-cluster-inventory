DOCUMENTATION = r'''
    name: Tower Cluster Inventory
    plugin_type: inventory
    author:
      - Alan Rominger (@AlanCoding)
      - Will Tome (@willtome)
    short_description: Dynamic inventory plugin for an Ansible Tower cluster.
    version_added: "2.10"
    description:
        - The "tower" inventory plugin returns inventory content from an
          inventory in Ansible Tower.
        - This inventory plugin returns inventory for the Ansible Tower
          inventory plugin itself.
    options:
        host:
            description: The network address of your Ansible Tower host.
            type: string
            required: True
'''

EXAMPLES = r'''
# example tower_cluster.yml file using no authentication
plugin: tower_cluster
host: http://localhost:8013/
'''

from ansible.errors import AnsibleError, AnsibleParserError

from ansible.module_utils.six.moves.urllib.parse import urljoin

from ansible.plugins.inventory import BaseInventoryPlugin

import requests


class InventoryModule(BaseInventoryPlugin):

    NAME = 'tower_cluster'

    def verify_file(self, path):
        super(InventoryModule, self).verify_file(path)
        return path.endswith(('tower_cluster.yml', 'awx.yml'))

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)
        host = self.get_option('host')
        ping_url = urljoin(host, 'api/v2/ping')
        r = requests.get(ping_url)
        data = r.json()

        for instance_data in data['instances']:
            self.inventory.add_host(instance_data['node'])
            self.inventory.set_variable(
                instance_data['node'], 'capacity', instance_data['capacity']
            )

        for group_data in data['instance_groups']:
            group_name = self.inventory.add_group(group_data['name'])
            self.inventory.set_variable(
                group_name, 'group_capacity', group_data['capacity']
            )
            for instance in group_data['instances']:
                self.inventory.add_child(group_name, instance)
