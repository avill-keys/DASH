# VNET to VNET 

The SoNiC-DASH testbed provides a common test platform to examine an extensive collection of test cases and allow ease of duplication and modification.  The directory structure is arranged for configuring a variety of test SKUs and to reduce testing design time.

The files found within this directory serve the following purpose:
1. Define a guide for expanding DASH test scenarios.
2. Generate two test outcomes using separate traffic generation tools and collecting results using one testing framework: PyTest.
3. Demonstrate testbed setup requires minimum configuration as the test platform provides tools and configuration out of the box.
4. Test one seeks to find the maximum capability of the device under test to measure the raw bandwidth by identifying the Packets Per Second.
5. Test two's goal is to discover the maximum number of functioning connections that can be established per second.


# test cases

| Test case                                      | Description                                               |
| ---------------------------------------------- | --------------------------------------------------------- |
| [vxlan_1eni_1ip](./one-ip/README.md)           | minimum posible config                                    |
| [vxlan_8eni_48k_ips](./48k-ips/README.md)      | medium sized config                                       |
| [vxlan_8eni_hero](./hero/README.md)            | full "Hero" test config                                   |



# minimum posible config
1 src ip , 1dst ip, 1 udp port, 1 eni ...... 1-2 flow(s)

Intent here is to create the smalles most basic config that will get udp traffic to pass through in both directions.

This will prove the basic functionality is there.

Based on the design of the implementation this test will usualy be able to give us also the best or the worst performance numbers.

obtain PPS and latency numbers

# minimum posible config, add few udp ports
This builds on top of the previous test.

Intent here is to get closer to reality where we will have more than 1 flow at a time.

For higly paralel implementations have 1 flow per procesing unit and it should provide the best performance numbers. 

obtain PPS and latency numbers

# minimum posible config, with random src and dest udp ports
builds on top of minimum posible config, but since we have 65K posible source and 65K posible destination ports, we can generate 4 bilion unique flows.

this test can be ran in 2 ways.

keep the flow expiration timer at 1 sec and see what is the device flow install rate.

keep the flow expiration timer at `big number` and see how many flows can be installed before device starts misbehaving.

  - is performance slowly degrading ?
  - is performance all of a suden degrading drasticaly?
  - will the device crash?
  - will the device recover and return to good performance/functionality once the flows expire and flow tables are not full anymore?

# minimum posible config, cps test
TBD