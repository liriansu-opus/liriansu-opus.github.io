---
title: "Software Engineering Practice: Subnet Management"
date: 2020-12-13T21:48:22+08:00
zhUrl: /software-engineering-vpc
aliases:
  - /software-engineering-vpc-en
---

The Software Engineering Practice series of articles
focuses on how software is collaboratively developed in real engineering projects.
This article mainly introduces how to plan, build, and manage subnets.

<!--more-->

# outline

This article includes:

- concepts: subnet concepts are all very basic
  - ip/cidr: IP is the point of a service, CIDR is the surface that describes it
  - vpc/subnet: VPC is the tool cloud services provide to divide subnets
- boundary: the core of subnet design is boundary division
  - scene: divide by scene dimension, distinguishing dev, test, prod environments
  - network: divide by network dimension, distinguishing external network, internal network
- example: examples from real development
  - ipsec: a common tool for VPC peering
  - openvpn: a common tool for connecting to internal networks
- conclusion


# Concepts

In our daily development,
as long as we use networks we'll definitely deal with various subnets.
Often subnets, as stable infrastructure,
we don't notice them.
But some knowledge about subnets and networks
is indeed something to consider during software engineering.

## IP and CIDR

In modern networks,
IP is the point of a service, and CIDR is the surface that describes it.

![ip][ip]

> IPv4 class classification

To list some IPs that come to mind:
`127.0.0.1` the agreed-upon local address;
`8.8.8.8`/`8.8.4.4` Google-provided DNS addresses;
`59.78.3.25` the IP address of SJTU's East 3rd Building...

CIDR is the modifier describing a series of IP addresses.

For example `59.78.3.25/32` represents the IP address segment where the first 32 binary bits are strictly equal to `59.78.3.25` (i.e., specifically this address).
Similarly, `10.0.0.0/16` is the IP address segment starting with `10.0.`.


## VPC and subnet

AWS as the ancestor of cloud services
pioneered the VPC service letting users configure their own subnets,
later VPC also gradually became standard for cloud services.

VPCs can be isolated or peered with each other.
(Here isolation and peering refer to software-level.)
Generally VPC is used to distinguish production and development environments.

For example we can open two VPCs on a cloud service,
production environment CIDR is `10.0.0.0/16`,
development environment CIDR is `10.1.0.0/16`.

Under VPCs you can split subnets,
subnets need more specific CIDRs,
like production environment subnets might be `10.0.0.0/24`, `10.0.10.0/24`.


# Boundary

The core of subnets is boundary division.
The purpose of well-dividing subnets
has both security considerations
and high-availability disaster recovery via geographic distribution.

## Scene

Cloud services generally set up data centers in major cities worldwide,
each data center has multiple zones,
our subnet boundaries should at least be drawn at this level.

For example online services deploy cross-zone,
distributed across multiple subnets,
when some zone has an accident like a janitor unplugging power to plug in a vacuum (generally doesn't happen),
the service can stay highly available.

Subnet-level can also configure network traffic ingress/egress permissions.
This feature can be used to plan internal network permissions.

For example we can divide "external network in and out," "external network out only no in," "external network inaccessible (only internal accessible)" three kinds of subnets,
to deploy services with different traits (load balancer, regular business, database).

## Network

Whether network traffic goes through internal or external network is also a factor worth considering.

Besides security factors,
general cloud service providers price external network traffic at 1 yuan/GB,
the price factor is also a point to consider.

Most of the time, dev can strictly follow the principle of layering,
all frontend definitely goes through external network APIs,
all backend definitely goes through internal network APIs,
only load balancer, gateway layer considers internal/external network conversion issues.

Some other times, you can automatically configure traffic network via DNS.
For example by default `api.liriansu.com` points to the load balancer's external address,
but modifying internal DNS makes it point to the load balancer's internal address.


# Example

Finally let me append some examples from real development.

## IPsec

Once businesses become complex,
you encounter cross-cloud-provider development scenes.
Cross-cloud-provider internal network peering
generally uses the IPsec tool.
The VPN services cloud services themselves provide are also based on this.
The essence of IPsec is starting two servers that can communicate over the external network,
forwarding traffic to each other.

For example to configure Aliyun and Amazon Cloud peering, the steps roughly include:

- Build VPC/subnet on both sides (CIDR non-overlapping)
- Each side spins up a machine with public access address, install ipsec
  - Configure ipsec certificate, keys etc.
  - Enable ip forwarding, configure iptables firewall rules
  - AWS, remember to turn off the machine's source/dest check
- Configure subnet routing table to jump to the ipsec machine
- Open security groups on both sides for mutual access
  - `traceroute` command can be used to detect jumps

## OpenVPN

Another scene we encounter
is connecting development environments into the internal network for development.

This can generally be done with tools like OpenVPN,
but since we're currently still using the manual traffic forwarding approach,
let's share it in a future article when it becomes relevant :)


# Conclusion

- Subnet management is infrastructure closely related to development, best to plan well early
- The core of subnet planning is boundary division, mainly considering security and high availability
- Cloud service basic concepts are similar, need to consider cross-cloud-service, dev/test/prod multi-dimensional subnets
- Complex factors of internal/external network traffic can be shielded via layering or DNS

(End)


[ip]: /assets/pics/ip_types.jpg
