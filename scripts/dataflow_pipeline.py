import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery

class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument('--input', type=str, help='Input file to process')
        parser.add_value_provider_argument('--output', type=str, help='Output BigQuery table to write results to')

# Function to filter out users under 18 years old
def filter_adults(user):
    name, age, email = user.split(',')
    if int(age) >= 18:
        return {'name': name, 'age': int(age), 'email': email}

def run():
    options = MyOptions()
    with beam.Pipeline(options=options) as p:
        (
            p
            | 'Read from GCS' >> beam.io.ReadFromText(options.input)
            | 'Filter Adults' >> beam.Map(filter_adults)
            | 'Remove None' >> beam.Filter(lambda x: x is not None)
            | 'Write to BigQuery' >> WriteToBigQuery(
                options.output,
                schema='name:STRING, age:INTEGER, email:STRING',
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
            )
        )

if __name__ == '__main__':
    run()
