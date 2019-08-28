### tower-cluster-inventory
An Ansible inventory plugin to return the inventory of a live Tower cluster

Use `ansible-inventory` to view the contents that the inventory produces.

```
ansible-inventory -i tower_cluster.yml --list --export --playbook-dir=.
```

#### View Plugin Documentation

Use `ansible-doc` to view the documentation.
The search path must be set for this to work. That's due to some very technical
historical issues related to bootstrapping the search paths without a playbook
directory available.

```
ANSIBLE_INVENTORY_PLUGINS=inventory_plugins ansible-doc -t inventory tower_cluster
```

#### Run Playbook Against Inventory

Run a playbook with this inventory.

```
ansible-playbook -i tower_cluster.yml playbook.yml
```

#### Inventory Parsing Failures

This is what happens when you run a playbook and all the parsers failed
to parse the inventory.

```
ansible-playbook -i bad.tower_cluster.yml playbook.yml
```

Make it a failure:

```
ANSIBLE_INVENTORY_ANY_UNPARSED_IS_FAILED=True ansible-playbook -i bad.tower_cluster.yml playbook.yml
```

