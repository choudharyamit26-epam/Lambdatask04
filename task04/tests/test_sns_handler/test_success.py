from tests.test_sns_handler import SnsHandlerLambdaTestCase
import json


class TestSuccess(SnsHandlerLambdaTestCase):

    def test_success(self):
        sns_event = {
            "Records": [
                {
                    "Sns": {
                        "Message": "Test SNS message"
                    }
                }
            ]
        }

        expected_response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'SNS message processed successfully'})
        }

        response = self.HANDLER.handle_request(sns_event, dict())

        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], expected_response['body'])
