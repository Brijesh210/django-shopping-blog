class TestUser:
    # multiple model in signle user app
    # factory is tool to make test data for model
    # test real database, create the database layer, when test running, and mock out the complelate database,
    # factory pattern, make it fast and accurate...
    # it is integration test...
    def test_factory(self):
        user = UserFactory()

        assert user is not None