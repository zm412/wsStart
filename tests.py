from unittest import IsolatedAsyncioTestCase
from calculate_factorial import get_factorial

class Test(IsolatedAsyncioTestCase):

    async def test_functionality(self):
        result = await get_factorial(5)
        print(result, 'result')
        self.assertEqual(120, result)

    async def test_functionality1(self):
        result = await get_factorial(20)
        print(result, 'result')
        self.assertEqual(2432902008176640000, result)

    async def test_functionality2(self):
        result = await get_factorial(0)
        print(result, 'result')
        self.assertEqual(1, result)


