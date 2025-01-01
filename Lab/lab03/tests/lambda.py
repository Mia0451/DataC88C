test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '33f12afaac551f1fc306d52148ff938c',
          'choices': [
            'A lambda expression does not automatically bind the function that it returns to a name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following statements describes a difference between a def statement and a lambda expression?'
        },
        {
          'answer': 'b02f8059d9aa9a9ea464c5d1133728aa',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many formal parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': '332099405b006382d5733a5f9c17843b',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> lambda x: x  # A lambda expression with one parameter x
          409d225c8d71bdae383b166e754adf05
          # locked
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          ba2ed30ea3c5a7b76de99e472ac02833
          # locked
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          c66c489c94f153ccc42909baf6da3202
          # locked
          >>> b = lambda x, y: lambda: x + y # Lambdas can return other lambdas!
          >>> c = b(8, 4)
          >>> c
          409d225c8d71bdae383b166e754adf05
          # locked
          >>> c()
          92a76d8eea7c8a672069b14010ed69c0
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          ea822daf458252683b5a70f567b3cdab
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          9ee30c0bb2642a554fb2198e3b73feb1
          # locked
          >>> higher_order_lambda(g)(2)
          ad741b000d1cc7ef3beaaf650d8f371b
          # locked
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          c66c489c94f153ccc42909baf6da3202
          # locked
          >>> print_lambda = lambda z: print(z) # When is the return expression of a lambda expression executed?
          >>> print_lambda
          409d225c8d71bdae383b166e754adf05
          # locked
          >>> one_thousand = print_lambda(1000)
          600c395cb51f2701749f4d41adc442ab
          # locked
          >>> one_thousand # What did the call to print_lambda return? If it displays nothing, write Nothing
          fef9a0b77f7c83478c249aedcc62186d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
