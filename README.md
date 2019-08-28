# tower-cluster-inventory
An Ansible inventory plugin to return the inventory of a live Tower cluster

Use `ansible-inventory` to view the contents that the inventory produces.

```
ansible-inventory -i tower_cluster.yml --list --export --playbook-dir=.
```

Use `ansible-doc` to view the documentation.
The search path must be set for this to work. That's due to some very technical
historical issues related to bootstrapping the search paths without a playbook
directory available.

```
ANSIBLE_INVENTORY_PLUGINS=inventory_plugins ansible-doc -t inventory tower_cluster
```

Run a playbook with this inventory.

```
ansible-playbook -i tower_cluster.yml playbook.yml
```

