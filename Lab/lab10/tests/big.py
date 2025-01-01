test = {
  'name': 'big',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT name, ROUND(pounds, 2) FROM big;
          Flappy|40.48
          Pumpkin|42.46
          Tom|58.96
          Waddle|48.62
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
