# GCP Data Pipeline Project

## Project Overview
This project demonstrates a data pipeline built using Google Cloud Platform services, including Cloud Storage, Dataflow, and BigQuery.

## Technology Stack
- Google Cloud Platform
- Apache Beam
- Python

## Setup Instructions
1. Clone this repository to your local machine.
2. Ensure you have the necessary permissions on your GCP account.
3. Set up Google Cloud SDK and authenticate.
4. Install required Python packages:
   ```bash
   pip install apache-beam[gcp]

   
Running the Pipeline
To run the pipeline, use the following command in the terminal:

python scripts/dataflow_pipeline.py \
    --runner=DataflowRunner \
    --project=data-pipeline-project-438123 \
    --region=us-central1 \
    --staging_location=gs://my-data-pipeline-bucket/staging \
    --temp_location=gs://my-data-pipeline-bucket/temp \
    --input=gs://my-data-pipeline-bucket/users.csv \
    --output=data-pipeline-project-438123:user_data.filtered_users \
    --job_name=my-data-pipeline-job-$(date +%Y%m%d%H%M%S)



https://github.com/jyot9998/GCP-Data-Pipeline-Project/blob/main/resources/Screenshot%20(5878).png
