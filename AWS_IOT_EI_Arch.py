# -*- coding: utf-8 -*-
"""
Created on Thursday Aug 4 10:11:12 2022
@author: Akram Sheriff
AWS IOT Cloud Architecture  Diagram with different components  in "IOT Cloud  Data lake implementation".
IOT  telemetry data is published by 'MQTT  Client' running  at the edge in a Cisco IOT gateway  (within IOX_CAF) to the
MQTT broker running on AWS IOT Core or Azure IOT Hub side.
"""
from diagrams import Cluster,Diagram
from diagrams.aws.iot import IotCore
from diagrams.aws.iot import IotAnalytics
from diagrams.aws.iot import IotMqtt
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.iot import IotDeviceGateway
from diagrams.aws.iot import IotGreengrassConnector
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.aws.analytics import DataPipeline
from diagrams.aws.iot import IotDeviceManagement
from diagrams.aws.iot import IotRule
from diagrams.aws.analytics import Quicksight
from diagrams.aws.analytics import Athena
from diagrams.aws.analytics import GlueCrawlers
from diagrams.aws.analytics import Glue
from diagrams.aws.analytics import GlueDataCatalog
from diagrams.aws.analytics import LakeFormation
from diagrams.aws.storage import S3

with Diagram("AWS_IOT_CLOUD_DATA_LAKE_ARCHITECTURE WITH MQTT BASED IOT TELEMETRY DATA", show=False):

    with Cluster('IOT Edge Gateway Stack'):
        MQTT_Client = IotDeviceManagement('MQTT Client')
        device = IotDeviceGateway('Gateway')
        source = IotMqtt('Incoming MQTT Messages')
        green_connect = IotGreengrassConnector("Green Grass SDK Connector")

    with Cluster('IOT Core Data Ingestion'):
        dest_iot = IotCore("IOT Core")
        iot_rules = IotRule("IOT Rules_Engine")

    with Cluster("AWS IOT Data Processing Pipeline"):
        raw_data = SimpleStorageServiceS3Bucket("RAW:BRONZE DATA")
        s3_pipline = DataPipeline("Raw Data Pipeline")
        sil_s3_bucket =SimpleStorageServiceS3Bucket("PROCESSED:SILVER S3")
        s3_gold_pipeline = DataPipeline("Final Pipeline")
        gold_s3_bucket = SimpleStorageServiceS3Bucket("REFINED:GOLD S3")
        Dev_Data = SimpleStorageServiceS3('Device Specs Data.csv')
        Glue_craw = GlueCrawlers('AWS Glue Crawler')
        Glue_catalog = GlueDataCatalog('AWS Glue Catalog')

    with Cluster("Analytics Visualization Tools"):
        vis = IotAnalytics('Data Visualization')
        quick_sight = Quicksight('Quicksight Data Plots')
        athena = Athena("Athena Fed -SQL analysis")
        LakeForm = LakeFormation('AWS Lakeformation Tools (Optional)')

    ''' Data Flow pipelines and  mapping Table Logic within the IOT Data lake  architecture '''

    device  >> source >> dest_iot >> iot_rules >> raw_data  >> s3_pipline >> sil_s3_bucket >> s3_gold_pipeline \
    >> gold_s3_bucket

    sil_s3_bucket >> Glue_craw
    Dev_Data >> Glue_craw

    Glue_craw >> Glue_catalog

    gold_s3_bucket >> quick_sight
    Glue_catalog >> athena
    athena >> quick_sight
    quick_sight >> vis








