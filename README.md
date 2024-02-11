```                                                                               
BBBBBBBBBBBBBBBBB   UUUUUUUU     UUUUUUUUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF 
B::::::::::::::::B  U::::::U     U::::::UF::::::::::::::::::::FF::::::::::::::::::::F 
B::::::BBBBBB:::::B U::::::U     U::::::UF::::::::::::::::::::FF::::::::::::::::::::F 
BB:::::B     B:::::BUU:::::U     U:::::UUFF::::::FFFFFFFFF::::FFF::::::FFFFFFFFF::::F 
  B::::B     B:::::B U:::::U     U:::::U   F:::::F       FFFFFF  F:::::F       FFFFFF 
  B::::B     B:::::B U:::::D     D:::::U   F:::::F               F:::::F              
  B::::BBBBBB:::::B  U:::::D     D:::::U   F::::::FFFFFFFFFF     F::::::FFFFFFFFFF      
  B:::::::::::::BB   U:::::D     D:::::U   F:::::::::::::::F     F:::::::::::::::F    
  B::::BBBBBB:::::B  U:::::D     D:::::U   F:::::::::::::::F     F:::::::::::::::F    
  B::::B     B:::::B U:::::D     D:::::U   F::::::FFFFFFFFFF     F::::::FFFFFFFFFF    
  B::::B     B:::::B U:::::D     D:::::U   F:::::F               F:::::F              
  B::::B     B:::::B U::::::U   U::::::U   F:::::F               F:::::F              
BB:::::BBBBBB::::::B U:::::::UUU:::::::U FF:::::::FF           FF:::::::FF            
B:::::::::::::::::B   UU:::::::::::::UU  F::::::::FF           F::::::::FF            
B::::::::::::::::B      UU:::::::::UU    F::::::::FF           F::::::::FF            
BBBBBBBBBBBBBBBBB         UUUUUUUUU      FFFFFFFFFFF           FFFFFFFFFFF
  
Basic Utility for Finding Faults (in an AWS Account)
```
#### requirements:  
* aws cli
* aws credentials configured
* aws permissions to query the resources
* pip3
* python3
  * argparse 
  * boto3
  * botocore.exceptions

#### usage:  
`buff.py [-h] [-s3] [-ami] [-sg] [-all]`

#### arguments:  
  `-h`                 show this help message and exit  
  `-s3`                checks for publicly accessible S3 buckets  
  `-ami`               checks for publicly accessible AMIs  
  `-sg`                checks for Security Groups with inbound source rules for 0.0.0.0/0  
  `-all`              performs all available checks  

#### to-do list:  
* write a function that checks iam policies for desired permissions
