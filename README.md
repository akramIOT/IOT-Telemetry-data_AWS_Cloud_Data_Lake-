[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/akramIOT/IOT-Telemetry-data_AWS_Cloud_Data_Lake)

# IOT-Telemetry-data_AWS_Cloud_Data_Lake-
End to End  architecture  and  Implementation of a  Data ingestion  Pipeline in AWS Cloud for  build  Data lake 

For  Reference on AWS IOT Device side Python SDK, kindly follow the  below link and clone from it.

https://github.com/aws/aws-iot-device-sdk-python


Please check the  following  while using  AWS IOT Core Python SDK and  Boto3 with Python 3.x or Python 2.x versions in this following project.

On 2021-01-15, deprecation for Python 2.7 was announced and support was dropped on 2021-07-15. To avoid disruption, customers using Boto3 on Python 2.7 may need to upgrade their version of Python or pin the version of Boto3. For more information, see this blog post.https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-python-2-7-in-aws-sdk-for-python-and-aws-cli-v1/

On 2022-05-30, support for Python 3.6 was ended. This follows the Python Software Foundation end of support for the runtime which occurred on 2021-12-23. For more information, see this blog post.
https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/

Here is the  illustration of the  Complete architectural implementation of the AWS Cloud IOT  Data lake with IOT telemetry data coming from MQTT Client's
running on Cisco IOT  gateways. 

A) (IR1101 , IR829, IR 1800  series Cisco IOT  gateways could be used to run the MQTT Client) or 

B) A linux machine or Raspberry PI could be used to run a vanilla  MQTT Client  (code present in this repository) on it. 

C) Any Cisco Catalyst hardware supporting IOX_CAF  and AWS  Greengrass SDK  could be also leveraged  - Reference in link below.  https://developer.cisco.com/ecosystem/cpp/solutions/177022/

![aws_iot_cloud_data_lake_architecture_with_mqtt_based_iot_telemetry_data](https://user-images.githubusercontent.com/21118209/182935437-6e72613f-4568-4f33-84e7-ae0fbba7f388.png)


Prerequisites for this Project:
================================

1) Setting up the AWS IoT Analytics channel, pipeline, and data store
2 Ingesting MQTT  baaed sample pubSub data into the AWS IoT Core, then to the IOT data pipeline channel and then evnetually to the IOT data analytics, Visualisation toosl. 
Creating a dataset with dataset content delivery to different S3 buckets. Kinldy refer illustration above. 
3) Integrating IoT data with other data stored in your data lake on AWS IOT data pipeline channel. (Either by using Lakefromation tools or by using Glue Data catalog logic or by creating manual data pipelines).


Account Access, IAM access and other  Prerequisites:
====================================================

For this use case implemenation in the AWS Cloud make sure that you have access to the following resources:

1) An AWS account in the same AWS Region where AWS IoT Analytics is available. The idea is to reduce the  RTT for moving the data by selecting IOT  analytics and  S3 data storage buckets in same  region.
3) This project uses  a Cloudformation YAMl template which is in the US East (N. Virginia) Region. 
4) However, you can choose another AWS Region where AWS IoT Analytics is available.
5) The AdministratorAccess policy granted to your AWS account (for production, we recommend restricting this further).
6) The AWS CLI installed and configured to use with your AWS account, along with Privelege, PKI key pairs for  CLI access to your AWS Cloud account.
7) AWS IOT Python SDK and all the modules as defined in the  requirements.txt to be installed. 

