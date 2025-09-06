import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_hello_world_get(self):
        """Test the GET / endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World')
    
    def test_log_message_post_success(self):
        """Test the POST /message endpoint with valid data"""
        test_data = {"message": "This is a test message"}
        response = self.app.post('/message', 
                                data=json.dumps(test_data),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['status'], 'success')
        self.assertEqual(response_data['message'], 'Message logged successfully')
    
    def test_log_message_post_missing_field(self):
        """Test the POST /message endpoint with missing message field"""
        test_data = {"not_message": "This won't work"}
        response = self.app.post('/message',
                                data=json.dumps(test_data),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertIn('error', response_data)
    
    def test_log_message_post_empty_body(self):
        """Test the POST /message endpoint with empty body"""
        response = self.app.post('/message',
                                data=json.dumps({}),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertIn('error', response_data)

if __name__ == '__main__':
    unittest.main()
