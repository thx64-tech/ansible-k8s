#! /usr/bin/env python3.11
# -*- coding: UTF-8 -*-

import toml
print("Test modif file")

# Load the TOML file into a dictionary
with open('/etc/containerd/config.toml', 'r') as f:
    config = toml.load(f)

# Update the value of SystemdGroup to true
config['plugins']['io.containerd.grpc.v1.cri']['containerd']['runtimes']['runc']['options']['SystemdCgroup'] = True

# Write the updated configuration back to the TOML file
with open('/etc/containerd/config.toml', 'w') as f:
    toml.dump(config, f)
