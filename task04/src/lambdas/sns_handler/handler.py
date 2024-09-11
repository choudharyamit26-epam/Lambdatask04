import json

from commons.abstract_lambda import AbstractLambda
from commons.log_helper import get_logger

_LOG = get_logger('SnsHandler-handler')


class SnsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        print("===============>>>", event)
        try:
            # Assuming SNS message format, extract message details
            sns_message = event.get('Records')[0]['Sns']['Message']
            _LOG.info(f"Incoming SNS message: {sns_message}")

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'SNS message processed successfully'})
            }
        except KeyError as e:
            _LOG.error(f"Invalid SNS message format: {event}")
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid SNS message format'})
            }
        except Exception as e:
            _LOG.error(f"Error processing SNS message: {str(e)}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Internal Server Error'})
            }


HANDLER = SnsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
