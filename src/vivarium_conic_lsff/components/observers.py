import vivarium_conic_lsff.globals as project_globals

class MockObserver:
    """
    Adds columns to ensure a complete output shell
    """
    @property
    def name(self):
        return 'mock_observer'

    def __init__(self):
        # As working observers are completed add the appropriate key to exclude the mocking behavior
        exclude_list = [
            'death',
            'ylls',
            'ylds',
        ]
        need_to_mock = [i for i in list(project_globals.COLUMN_TEMPLATES.keys()) if i not in exclude_list]
        mock_columns = []
        for col in need_to_mock:
            mock_columns.extend(project_globals.result_columns(col))
        self.mocks = {i: project_globals.MOCKED_COLUMN_VALUE for i in mock_columns}

    def setup(self, builder):
        builder.value.register_value_modifier('metrics', self.metrics)

    def metrics(self, index, metrics):
        metrics.update(self.mocks)
        return metrics

