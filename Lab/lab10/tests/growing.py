test = {
  'name': 'growing',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM growing;
          Bud|29.3
          Bird|25.3
          Pumpkin|25.3
          Tom|26.8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
