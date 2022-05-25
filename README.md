# A15-Disaster-recovery-mechanism-with-active-storage-replication-and-DNS-failover-in-cloud-VM

# Project Title

DISASTER RECOVERY MECHANISM WITH ACTIVE STORAGE REPLICATION AND DNS FAILOVER IN CLOUD VIRTUAL MACHINE 


# About the Project

The Domain Name Service (DNS) is a vital service on the Internet. The problem arises where a particular DNS is not able to point an IP address of the server because of heavy traffic, DDoS attack, system crash and much more reasons such as if multiple request is sent to the server then the server cant handle everything at same this leads to network traffic so the crash in server takes place. During this period there are huge chances for an organization to be a victim of huge, valuable data loss and have downtime for a certain period. This will cause a billion dollar business impact and risk of losing data and loss of network connectivity so may not be able to find the information or carry out the actions they need. To overcome this we come up with an approach of DNS Failover with active Replication which is a solution designed to help keep the services online and prevent the servers from Data losses. When systems and services go down DNS failover is used to direct the users to another resource with little to no disruption which has active replication of Data with the current prod Server ie., a database contains two servers if one is failed then another will work with same data without any data loss. The backup server/Replicating server is named as Contingency server (CNR) which has an active storage replication with the Production server preventing Data loss and the other server is backup server which will replicate the data from the active server when any updation takes place in the active server.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

Hardware Requirements

```
Processor 	 : core i5/17/i8
RAM 	 : 4GB
CPU 	 : 2 x 64-bit 2.8GHZ 8.00 GT/s
Disk 	storage : 500 GB.
NAS based Virtual Storage Disk (AZURE)

```
Software Requirements

```
Operating 	system : Windows 7/8/10(64bit) / Unix/ Linux 	
Additional 	:  Shell Scripting, Django, python, Postgresql, Azure VM

```

### Installation
