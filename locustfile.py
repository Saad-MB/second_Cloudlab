from locust import HttpUser, task

class NumericalIntegrationTest(HttpUser):
    @task
    def test_integration(self):
        self.client.get("/integrate?lower=0&upper=3.14159")
